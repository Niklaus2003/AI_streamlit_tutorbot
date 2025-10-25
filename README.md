🧠 AI Tutor App

AI-powered interactive learning assistant built with LangChain, Groq LLaMA 3.1, and Streamlit. This app allows students to ask academic questions, take quizzes, and track their learning progress in a conversational and intelligent interface.

Features

📘 Concept Explainer – Ask any academic question; the AI provides clear, easy-to-understand explanations.

🎯 Quiz Generator – Dynamically generates multiple-choice quizzes with instant feedback, explanations, and relevant YouTube help links.

🧩 Conversational Memory – Uses LangChain ConversationBufferMemory to remember past interactions, enabling follow-up questions.

📊 Progress Tracker – Saves quiz scores, topics, and timestamps locally for monitoring learning progress.

🌐 Streamlit Interface – Clean, user-friendly interface with modes: Ask a Question, Take a Quiz, and View Progress.

🔒 Local Data Storage – All quiz progress is stored in a JSON file; no external database required.

Tech Stack

Python

Streamlit

LangChain

Groq LLaMA 3.1

JSON-based progress tracking

Installation

Clone the repository:

git clone https://github.com/Niklaus2003/AI_streamlit_tutorbot.git


Navigate into the project folder and install dependencies:

cd AI_streamlit_tutorbot

Usage

Run the app with:

streamlit run app.py


Enter your name to begin.

Choose a mode from the sidebar: Ask a Question, Take a Quiz, or View Progress.

For quizzes, enter a topic and number of questions.

Ask academic questions to get detailed explanations, including follow-up questions remembered by the AI.

Your progress is automatically saved locally and displayed in the View Progress section.

Notes

Set your Groq API key in .env as GROQ_API_KEY.

Quiz questions are generated dynamically using LangChain + LLaMA, ensuring unique and diverse content.

Explanations can be followed by YouTube tutorials for enhanced learning.

Future Enhancements

🌐 Multilingual Support – AI explanations and quizzes in multiple languages.

☁️ Cloud Sync – Store user progress in cloud for cross-device access.

📱 Mobile-Friendly UI – Optimize Streamlit interface for mobile devices.

🤖 Adaptive Quizzes – Adjust quiz difficulty based on user performance.

📝 Custom Topics & Subjects – Allow users to create quizzes for specific subjects or chapters.

🎧 Voice Integration – Enable voice input and TTS for hands-free interaction.
