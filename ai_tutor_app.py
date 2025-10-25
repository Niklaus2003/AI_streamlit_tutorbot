import os
import json
import random
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory

# === API SETUP ===
key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7, api_key=key)
output_parser = StrOutputParser()

# === SESSION STATE ===
if "username" not in st.session_state:
    st.session_state.username = ""

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

PROGRESS_FILE = "progress.json"

# === JSON PROGRESS STORAGE ===
def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return []
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def save_progress(record):
    data = load_progress()
    data.append(record)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_user_progress(username):
    return [entry for entry in load_progress() if entry["username"] == username]

# === LLM CONCEPT EXPLAINER ===
def explain_concept(query):
    memory = st.session_state.memory
    history = memory.chat_memory.messages
    prompt = PromptTemplate.from_template(
        "You are an educational AI tutor helping with any subject.\n"
        "Conversation so far:\n{history}\n\n"
        "Student's question: {query}"
    )
    chain = prompt | llm | output_parser
    return chain.invoke({
        "query": query,
        "history": "\n".join([f"{m.type.capitalize()}: {m.content}" for m in history])
    })

# === QUIZ FUNCTION ===
def run_quiz(topic, num_questions=5):
    st.subheader(f"🎯 Quiz on: {topic}")
    
    # Initialize quiz data if not exists or if starting new quiz
    if "quiz_data" not in st.session_state or st.session_state.get("quiz_topic") != topic:
        st.session_state.quiz_data = []
        st.session_state.quiz_submitted = False
        st.session_state.quiz_topic = topic
        asked = set()

        for _ in range(num_questions):
            for _ in range(5):  # Try up to 5 times to get a unique question
                style = random.choice(["", " with interesting facts", " with clear answers"])
                quiz_prompt = (
                    f"Generate 1 unique multiple-choice question on '{topic}'{style}.\n"
                    "Include:\nQuestion: <text>\nA) ...\nB) ...\nC) ...\nD) ...\nAnswer: <A/B/C/D>\nExplanation: <...>"
                )
                chain = PromptTemplate.from_template("{instruction}") | llm | output_parser
                qa = chain.invoke({"instruction": quiz_prompt})

                lines = qa.splitlines()
                question = next((l.split(":", 1)[-1].strip() for l in lines if l.lower().startswith("question:")), "")
                options = [l.strip() for l in lines if l.startswith(("A)", "B)", "C)", "D)"))]
                answer = next((l.split(":")[-1].strip()[0].upper() for l in lines if l.lower().startswith("answer:")), "")
                explanation = next((l.split(":", 1)[-1].strip() for l in lines if l.lower().startswith("explanation:")), "")
                if question and options and answer and question not in asked:
                    st.session_state.quiz_data.append({
                        "question": question,
                        "options": options,
                        "answer": answer,
                        "explanation": explanation,
                        "user_answer": None
                    })
                    asked.add(question)
                    break

    # Check if quiz is already submitted to show results
    if st.session_state.get("quiz_submitted", False):
        # Show results
        score = 0
        st.markdown("### 🧾 Quiz Results")

        for i, q in enumerate(st.session_state.quiz_data):
            correct = q["answer"]
            selected = q["user_answer"][0] if q["user_answer"] else ""

            st.markdown(f"**Q{i+1}: {q['question']}**")
            
            # Display all options
            for option in q["options"]:
                st.write(option)
            
            # Check if answer is correct and show explanation + YouTube help for all questions
            if selected == correct:
                st.success(f"✅ Correct! You chose {selected}")
                score += 1
            else:
                st.error(f"❌ Incorrect. You chose {selected}, correct answer is {correct}")
            
            # Always show explanation and YouTube help for every question
            st.info(f"**Explanation:** {q['explanation']}")
            st.markdown(f"🔗 [YouTube Help](https://www.youtube.com/results?search_query={q['question'].replace(' ', '+')}+for+beginners)")
            st.markdown("---")

        # Show final score at the end
        st.success(f"🎯 Final Score: {score}/{len(st.session_state.quiz_data)}")
        
        if st.button("Take Another Quiz"):
            # Clear quiz data to start fresh
            del st.session_state.quiz_data
            del st.session_state.quiz_submitted
            del st.session_state.quiz_topic
            st.rerun()
        
        return  # Exit function to prevent showing form again

    # === Display Quiz Form ===
    with st.form("quiz_form"):
        for i, q in enumerate(st.session_state.quiz_data):
            st.markdown(f"**Q{i+1}: {q['question']}**")
            user_answer = st.radio(
                "Choose an option:",
                q["options"],
                key=f"ans_{i}",
                index=None  # No default selection
            )
            st.session_state.quiz_data[i]["user_answer"] = user_answer
            st.markdown("---")

        submitted = st.form_submit_button("✅ Submit Quiz")

    # === Evaluation ===
    if submitted:
        # Check if all questions are answered
        unanswered = [i+1 for i, q in enumerate(st.session_state.quiz_data) if q["user_answer"] is None]
        if unanswered:
            st.error(f"Please answer all questions. Unanswered questions: {', '.join(map(str, unanswered))}")
            return
        
        score = 0
        st.session_state.quiz_submitted = True
        
        # Calculate score
        for q in enumerate(st.session_state.quiz_data):
            correct = q[1]["answer"]
            selected = q[1]["user_answer"][0] if q[1]["user_answer"] else ""
            if selected == correct:
                score += 1

        # Save progress with proper timestamp formatting
        save_progress({
            "username": st.session_state.username,
            "topic": topic,
            "score": score,
            "total": len(st.session_state.quiz_data),
            "percentage": round((score/len(st.session_state.quiz_data))*100, 2),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # Rerun to show results
        st.rerun()

# === APP START ===
st.set_page_config(page_title="AI Tutor", layout="wide")
st.title("🧠 AI Tutor App")

# === USER LOGIN ===
if not st.session_state.username:
    st.session_state.username = st.text_input("Enter your name to begin:")
    if not st.session_state.username:
        st.stop()

# === SIDEBAR ===
st.sidebar.title(f"👤 {st.session_state.username}")
view = st.sidebar.radio("Choose a mode:", ["Ask a Question", "Take a Quiz", "View Progress"])

# === MAIN LOGIC ===
if view == "Ask a Question":
    query = st.text_input("📝 Type your academic question:")
    if query:
        st.session_state.memory.chat_memory.add_user_message(query)
        reply = explain_concept(query)
        st.session_state.memory.chat_memory.add_ai_message(reply)
        st.markdown("📘 **Explanation:**")
        st.info(reply)

elif view == "Take a Quiz":
    topic = st.text_input("🎯 Enter a topic for the quiz:", value="Python")
    num_qs = st.slider("Number of questions", 1, 10, 5)
    if st.button("Start Quiz") or "quiz_data" in st.session_state:
        run_quiz(topic, num_qs)

elif view == "View Progress":
    progress = get_user_progress(st.session_state.username)
    if not progress:
        st.info("No progress found yet.")
    else:
        # Format progress data for better display
        formatted_progress = []
        for entry in progress:
            formatted_entry = {
                "Topic": entry["topic"],
                "Score": f"{entry['score']}/{entry['total']}",
                "Percentage": f"{entry.get('percentage', round((entry['score']/entry['total'])*100, 2))}%",
                "Date & Time": entry["timestamp"]
            }
            formatted_progress.append(formatted_entry)
        
        st.markdown("### 📊 Your Quiz History")
        st.table(formatted_progress)