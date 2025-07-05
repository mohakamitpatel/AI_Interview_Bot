# 🤖 AI Interview Bot

An intelligent AI-powered virtual interviewer that simulates real-time interview sessions. Built using Python, LLMs (Groq), and optional voice interaction, it evaluates candidate responses, provides helpful feedback, and assigns a performance grade — making it a powerful tool for interview preparation.

---

## 🔥 Features

- 🎯 Role-based interviews (Technical, HR, Behavioral)
- 🎤 Supports both **text** and **voice** input/output
- 💬 LLM-generated feedback and dynamic scoring
- 📊 Performance grading with curved scoring logic
- 🧠 Avoids repeated questions with memory
- 📁 Session history saved in `.json` and `.csv`
- 🧩 Modular question bank via `full_interview_questions_dataset.csv`
- 🔐 Secure API integration using `.env`

---

## ⚙️ Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/AI_Interview_Bot.git
   cd AI_Interview_Bot
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

4. Create a `.env` file from the `.env.example` and add your Groq API key  
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## 🗂 Project Structure

```
📦 AI_Interview_Bot/
├── run.py                          → Entry point for running the bot
├── core/
│   ├── answer_rating.py
│   ├── feedback_generator.py
│   ├── memory.py
│   ├── performance_tracker.py
│   ├── question_selector.py
│   └── voice_input.py
│
├── utils/
│   └── helpers.py
│
├── data/
│   └── full_interview_questions_dataset.csv
│
├── sessions/
│   └── session_*.json             → Detailed transcripts per run (optional)
├── session_log.csv                → Overall session performance (optional)
├── .env                           → Your Groq API key (excluded via .gitignore)
├── .env.example                   → Template for setting up your own `.env`
├── .gitignore
├── requirements.txt
├── test_feed.py                   → (Optional) test script
├── Checkenv.py                    → (Optional) env checker
└── README.md
```

---

## ▶️ How to Use

1. Run the bot  
   ```bash
   python run.py
   ```

2. Choose:
   - Interview type: `technical`, `hr`, or `behavioral`
   - Mode: `text` or `voice`

3. Answer 5 questions, with LLM-generated feedback and a per-answer score

4. At the end:
   - Total score and grade are displayed
   - Feedback is saved in `.json` and `.csv`

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

Each question is scored out of 5 and curved slightly using a custom scale.

---

## 📦 Dependencies

- `requests`  
- `python-dotenv`  
- `SpeechRecognition` *(for voice mode)*  
- `pyttsx3` *(for voice output)*  
- `pyaudio` *(required for microphone input)*  
- `openai` *(optional if switching LLM providers)*

> All are listed in `requirements.txt`

---

## 🚀 Future Ideas

- 🧑‍💻 Resume-based question customization  
- 🎙️ TTS voices with emotion support  
- 📊 Performance tracking over time (charts, graphs)
- 🌍 Multi-language support  
- 🌐 Streamlit/Flask-based web UI  
- 🤖 Gemini/GPT dynamic follow-up and realism

---

## 🤝 Contributing

Contributions are welcome!  
To contribute:

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Open a pull request  

⭐ Don’t forget to star the repo if you find it helpful!

✌️ Peace out. Built with code, not caffeine — Mohak
---

## 📝 License

Licensed under the MIT License.  
Feel free to use, modify, and share with credit.
