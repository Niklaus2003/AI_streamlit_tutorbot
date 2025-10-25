🧠 AI Tutor App

An interactive learning assistant powered by LangChain, Groq LLaMA 3.1, and Streamlit.
This AI Tutor can explain academic concepts, generate quizzes, track progress, and even remember past questions to provide context-aware learning — making studying more personalized and engaging.

🚀 Features

💬 Concept Explainer – Ask any academic question and get detailed, AI-generated explanations.

🧩 Smart Quiz Generator – Creates unique multiple-choice quizzes on any topic.

📈 Progress Tracker – Saves and displays your quiz history, scores, and timestamps.

🧠 Conversational Memory – Uses LangChain memory to handle follow-up questions seamlessly.

🔍 YouTube Help Links – Auto-suggests relevant beginner-friendly YouTube resources for each question.

🧰 Tech Stack

LangChain – for prompt management and conversational memory

Groq LLaMA 3.1 (8B-Instant) – for intelligent response generation

Streamlit – for the interactive web interface

Python – as the core programming language

JSON – for storing quiz progress and history

⚙️ Setup Instructions

Clone the repository

git clone https://github.com/yourusername/ai-tutor-app.git
cd ai-tutor-app


Install dependencies

pip install -r requirements.txt


Add your Groq API key
Create a .env file in the project directory and add:

GROQ_API_KEY=your_api_key_here


Run the app

streamlit run app.py

🧑‍🏫 How It Works

The app starts by asking your name to personalize your learning experience.

You can ask questions, take quizzes, or view progress from the sidebar.

The AI dynamically generates quizzes with explanations and YouTube help links.

All your quiz data is saved locally in progress.json.

🏅 Learning Outcomes

Hands-on experience with LLM integration using LangChain

Implementation of conversational memory in real-world learning apps

Combining AI reasoning, education, and data tracking in a single Streamlit interface

💡 Future Enhancements

Add leaderboards and performance analytics

Support for subject-based adaptive quizzes

Integration with speech-to-text and text-to-speech for voice-based tutoring

📜 License

This project is open-source and available under the MIT License
.
