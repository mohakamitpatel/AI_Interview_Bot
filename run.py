from core.question_selector import get_next_question, used_questions
from core.feedback_generator import generate_feedback_and_score
import pyttsx3
import speech_recognition as sr
import csv
import os
from datetime import datetime

# === Text-to-Speech Setup ===
tts = pyttsx3.init()

def speak(text):
    tts.say(text)
    tts.runAndWait()

# === Speech-to-Text Setup ===
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        answer = recognizer.recognize_google(audio) # type: ignore
        print("🗣️ You said:", answer)
        return answer
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return ""
    except sr.RequestError:
        print("❌ Could not request results from Google Speech Recognition service.")
        return ""

# === Grading Tier ===
def get_grade(score, total):
    if total == 0:
        return "N/A"
    percentage = (score / total) * 100
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 70:
        return "Good"
    elif percentage >= 50:
        return "Average"
    else:
        return "Needs Improvement"

# === Save session to log ===
def log_session(role, score, total, grade):
    filename = "session_log.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Role", "Score", "Total Questions", "Grade"])
        writer.writerow([datetime.now().isoformat(), role, score, total, grade])

# === Main Interview Logic ===
def run_interview(role, mode, max_questions=5):
    used_questions.clear()
    asked = 0
    score = 0
    max_score_per_question = 5  # Set your scoring scale here

    while asked < max_questions:
        result = get_next_question(role)
        if result is None:
            end_msg = "No more unique questions available. Interview finished early."
            print(f"\n✅ {end_msg}")
            if mode == "voice":
                speak(end_msg)
            break

        question, difficulty = result

        # Ask the question
        q_text = f"Question {asked+1}. Difficulty {difficulty}. {question}"
        if mode == "voice":
            speak(q_text)
        else:
            print(f"\nQ{asked+1}: [{difficulty}] {question}")

        # Capture the answer
        if mode == "voice":
            answer = listen()
        else:
            answer = input("Your answer: ")

        # Generate feedback and score
        feedback, partial_score = generate_feedback_and_score(answer, question)
        print(f"💬 Feedback: {feedback}")
        if mode == "voice":
            speak(feedback)

        score += partial_score
        asked += 1

    # Final summary
    max_possible_score = asked * max_score_per_question
    average_score = score / asked if asked > 0 else 0
    grade = get_grade(score, max_possible_score)

    closing = (
        f"Interview complete. You answered {asked} question(s).\n"
        f"Total Score: {score:.2f} / {max_possible_score}\n"
        f"Average per Question: {average_score:.2f} / {max_score_per_question}\n"
        f"Grade: {grade}"
    )
    print(f"\n🎉 {closing}")
    if mode == "voice":
        speak(closing)

    # Log session
    log_session(role, score, asked, grade)
if __name__ == "__main__":
    print("🧠 Welcome to the AI Interview Bot!")
    role = input("Choose interview category (e.g., Technical, HR): ").strip().lower()

    # Map aliases
    role_aliases = {
        "hr": "behavioral",
        "behavioural": "behavioral",
        "tech": "technical"
    }
    role = role_aliases.get(role, role)

    mode = input("Choose mode - 'text' or 'voice': ").strip().lower()
    if mode not in ['text', 'voice']:
        print("❌ Invalid mode. Defaulting to text.")
        mode = 'text'

    run_interview(role, mode)
