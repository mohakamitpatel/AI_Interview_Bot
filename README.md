# 🤖 AI Interview Bot

An intelligent AI-powered virtual interviewer built with Natural Language Processing and Machine Learning. It simulates real-time interview experiences, analyzes candidate responses, and provides actionable feedback to help users prepare effectively for job interviews.

## 🔥 Features

- 🧠 Simulates realistic HR, technical, and behavioral interviews  
- 🎤 Supports both text and optional voice input  
- 📊 Analyzes answers using sentiment analysis, keyword matching, and context relevance  
- ✍️ Provides personalized feedback and tips for improvement  
- 🗂️ Switch between different interview modes (HR, Technical, Behavioral)  
- 🧩 Modular and customizable question sets  
- 💾 Saves transcripts and performance logs for later review  

## ⚙️ Installation

1. Clone the repository:  
   `git clone https://github.com/yourusername/ai-interview-bot.git`  
   `cd ai-interview-bot`  

2. (Optional) Create and activate a virtual environment:  
   `python -m venv venv`  
   `source venv/bin/activate` *(Windows: `venv\Scripts\activate`)*  

3. Install the dependencies:  
   `pip install -r requirements.txt`  

## 🗂 Project Structure

```
📦 ai-interview-bot
├── 📁 data
│   └── 📄 questions.json             → Customizable question bank
├── 📁 models
│   └── 📄 sentiment_model.pkl        → Pretrained sentiment analysis model
├── 📁 utils
│   └── 📄 feedback_engine.py         → Evaluation and feedback logic
├── 📁 transcripts
│   └── 📄 *.txt                      → Saved interview transcripts
├── 📄 app.py                         → Main application logic
├── 📄 requirements.txt              → Python dependencies
└── 📄 README.md                     → Project documentation
```

## ▶️ How to Use

1. Run the bot using: `python app.py`  
2. Choose your preferred interview mode (HR, Technical, Behavioral)  
3. Answer each question via text (or voice input if enabled)  
4. Receive instant feedback and improvement tips  
5. View saved transcripts in the `transcripts/` folder  

## 💡 Example Usage

User selects "Technical Interview" → Bot asks coding-related questions → User types response → Bot analyzes the sentiment, relevance, and completeness → Feedback like "Try elaborating on the time complexity" is shown.  

## 📦 Dependencies

- Python 3.8+  
- NLTK  
- Scikit-learn  
- SpeechRecognition (optional for voice input)  
- TextBlob or VADER for sentiment analysis  

All dependencies are listed in `requirements.txt`  

## 🎥 Demo Preview

[![Watch the demo](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)  
Click the image to watch a demo of the AI Interview Bot in action.

## 🚀 Future Ideas

- Add voice synthesis for speaking the questions  
- Integrate OpenAI GPT for more dynamic conversations  
- Web interface with Streamlit or Flask  
- Resume analysis and personalized question generation  
- Multi-language support  

## 🤝 Contributing

Pull requests are welcome! If you’d like to contribute:  
1. Fork the repo  
2. Create a new branch  
3. Make your changes  
4. Submit a pull request  

Don’t forget to ⭐ the repo if you found it helpful!
