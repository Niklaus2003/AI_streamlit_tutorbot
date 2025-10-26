<h1 align="center">🧠 AI Tutor App</h1>
<p align="center">
  <i>An interactive AI-powered learning assistant built with <b>LangChain</b>, <b>Groq LLaMA 3.1</b>, and <b>Streamlit</b>.</i><br>
  Ask questions, take quizzes, and track your learning progress — all in one intelligent interface.
</p>

<hr>

<h2>✨ Overview</h2>
<p>
  The <b>AI Tutor App</b> transforms learning into an interactive experience. Using conversational memory, the AI can explain academic concepts, generate topic-based quizzes, and track user performance over time — all locally stored for privacy.
</p>

<hr>

<details open>
  <summary><h2>🚀 Features</h2></summary>

  <ul>
    <li>📘 <b>Concept Explainer</b> – Ask any academic question; the AI provides clear, easy-to-understand explanations.</li>
    <li>🎯 <b>Quiz Generator</b> – Dynamically creates multiple-choice quizzes with instant feedback, explanations, and relevant YouTube help links.</li>
    <li>🧩 <b>Conversational Memory</b> – Uses <b>LangChain ConversationBufferMemory</b> to remember past interactions and answer follow-up questions naturally.</li>
    <li>📊 <b>Progress Tracker</b> – Saves quiz scores, topics, and timestamps locally for learning analysis.</li>
    <li>🌐 <b>Streamlit Interface</b> – Minimal and user-friendly interface with modes: <b>Ask a Question</b>, <b>Take a Quiz</b>, and <b>View Progress</b>.</li>
    <li>🔒 <b>Local Data Storage</b> – Stores all progress in a JSON file without needing external databases.</li>
  </ul>
</details>

<hr>

<details open>
  <summary><h2>🧠 Tech Stack</h2></summary>

  <ul>
    <li>🐍 Python</li>
    <li>⚡ Streamlit</li>
    <li>🧩 LangChain</li>
    <li>🤖 Groq LLaMA 3.1</li>
    <li>🗂️ JSON-based progress tracking</li>
  </ul>
</details>

<hr>

<details open>
  <summary><h2>⚙️ Installation</h2></summary>

  <p><b>1️⃣ Clone the repository:</b></p>
  <pre><code>git clone https://github.com/Niklaus2003/AI_streamlit_tutorbot.git</code></pre>

  <p><b>2️⃣ Navigate into the project folder and install dependencies:</b></p>
  <pre><code>cd AI_streamlit_tutorbot
pip install -r requirements.txt</code></pre>
</details>

<hr>

<details open>
  <summary><h2>💻 Usage</h2></summary>

  <p><b>Run the app:</b></p>
  <pre><code>streamlit run app.py</code></pre>

  <ul>
    <li>Enter your name to begin.</li>
    <li>Select a mode: <b>Ask a Question</b>, <b>Take a Quiz</b>, or <b>View Progress</b>.</li>
    <li>Enter a topic and number of questions for quizzes.</li>
    <li>Ask academic questions for detailed explanations — follow-ups are remembered by the AI.</li>
    <li>All progress is saved locally and displayed in <b>View Progress</b>.</li>
  </ul>
</details>

<hr>

<details open>
  <summary><h2>📝 Notes</h2></summary>

  <ul>
    <li>Set your <code>GROQ_API_KEY</code> in a <b>.env</b> file before running.</li>
    <li>Quizzes are dynamically generated using <b>LangChain</b> + <b>LLaMA 3.1</b>.</li>
    <li>Explanations include YouTube tutorial links for deeper learning.</li>
  </ul>
</details>

<hr>

<details open>
  <summary><h2>🌟 Future Enhancements</h2></summary>

  <ul>
    <li>🌐 <b>Multilingual Support</b> – Enable AI explanations and quizzes in multiple languages.</li>
    <li>☁️ <b>Cloud Sync</b> – Store progress in the cloud for access across devices.</li>
    <li>📱 <b>Mobile-Friendly UI</b> – Optimize Streamlit interface for smaller screens.</li>
    <li>🤖 <b>Adaptive Quizzes</b> – Auto-adjust difficulty based on user performance.</li>
    <li>📝 <b>Custom Topics</b> – Allow personalized subject- or chapter-based quiz creation.</li>
    <li>🎧 <b>Voice Integration</b> – Add speech recognition and text-to-speech for hands-free learning.</li>
  </ul>
</details>

<hr>

<p align="center">
  🔗 <a href="https://github.com/Niklaus2003/AI_streamlit_tutorbot" target="_blank"><b>View Project on GitHub</b></a>
</p>
