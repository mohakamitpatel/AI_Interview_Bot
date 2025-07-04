# 🤖 AI Interview Bot

An intelligent AI-powered virtual interviewer that simulates real-time interview sessions. Built using Python, LLMs, and optional voice interaction, it evaluates candidate responses, provides helpful feedback, and assigns a performance grade — making it a powerful tool for interview preparation.

---

## 🔥 Features

- 🎯 Role-based interviews (Technical, HR, Behavioral)
- 🎤 Supports both **text** and **voice** input/output
- 💬 LLM-generated feedback and dynamic scoring
- 📊 Performance grading with curved scoring logic
- 🧠 Avoids repeated questions with memory
- 📁 Session history saved in `.json` and `.csv`
- 🧩 Modular question bank via `questions.csv`
- 🔐 Secure API integration using `.env`

---

## ⚙️ Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/ai-interview-bot.git
   cd ai-interview-bot
   ```

2. (Optional) Create and activate a virtual environment  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your Groq API key  
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## 🗂 Project Structure

```
📦 ai-interview-bot/
├── main.py                      → Entry point for running the bot
├── core/
│   ├── question_selector.py     → Chooses non-repeating questions
│   └── feedback_generator.py    → Handles Groq API feedback and scoring
├── questions.csv                → Customizable interview questions
├── sessions/
│   └── session_*.json           → Saved detailed session transcripts
├── session_log.csv              → Summary log of all interview attempts
├── .env                         → Stores your Groq API key
└── README.md                    → You're reading it!
```

---

## ▶️ How to Use

1. Run the bot  
   ```bash
   python main.py
   ```

2. Choose:
   - Interview type: `technical`, `hr`, or `behavioral`
   - Mode: `text` or `voice`

3. Answer 5 questions (asked based on role & difficulty)

4. After each answer:
   - You'll receive feedback from a Groq-powered LLM
   - A score from 0–5 is assigned

5. At the end:
   - You'll see your total score, average per question, and a final grade

6. Logs:
   - JSON transcript saved in `sessions/`
   - Summary saved in `session_log.csv`

---

## 💡 Example Interaction

```text
🧠 Welcome to the AI Interview Bot!
Choose interview category (e.g., Technical, HR): technical
Choose mode - 'text' or 'voice': text

Q1: [medium] Describe a time you debugged a difficult issue.
Your answer: I had a race condition...
💬 Feedback: Good example! You could elaborate on tools used.

...

🎉 Interview complete. You answered 5 question(s).
Total Score: 18.25 / 25
Average per Question: 3.65 / 5
Grade: Good
🗂️ Session saved to sessions/session_2025_07_04_190122.json
```

---

## 📊 Grading Scale

| Score (%) | Grade               |
|-----------|---------------------|
| 90–100%   | 🌟 Excellent         |
| 70–89%    | 👍 Good              |
| 50–69%    | ⚖️ Average           |
| Below 50% | 🚧 Needs Improvement |

Each question is scored out of 5, and the total score is curved and scaled accordingly.

---

## 📦 Dependencies

- `requests`  
- `python-dotenv`  
- `SpeechRecognition` *(for voice mode)*  
- `pyttsx3` *(for voice output)*  
- `pyaudio` *(required for microphone input)*  
- `openai` *(optional if switching models)*

> All are listed in `requirements.txt`

---

## 🎥 Demo Preview

[![Watch the video](https://github.com/mohakamitpatel/heart-disease-predictor/blob/main/assets/Screenshot%202025-06-18%20190147.png)](https://www.youtube.com/watch?v=n2kXr99IVzU)  
*Click the image to watch a demo of the AI Interview Bot in action.*

---

## 🚀 Future Ideas

- 🧑‍💻 Resume-based question customization  
- 🎙️ TTS voices with emotion support  
- 📊 Performance tracking over time (charts, graphs)
- 🌍 Multi-language question/answer support  
- 🌐 Web interface with Streamlit or Flask  
- 🤖 OpenAI/Gemini dynamic follow-up questions

---

## 🤝 Contributing

Contributions are welcome!  
To contribute:

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Open a pull request  

⭐ Don’t forget to star the repo if you find it helpful!

---

## 📝 License

Licensed under the MIT License.  
Feel free to use, modify, and share with credit.
