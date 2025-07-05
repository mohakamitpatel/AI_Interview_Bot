import json
from datetime import datetime

def save_session(session_data):
    """
    Save the interview session data to a timestamped JSON file.
    """
    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    filename = f"sessions/session_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(session_data, f, indent=4)

    print(f"\n🗂️ Session saved to {filename}")

def show_summary(session_data):
    """
    Display overall interview summary.
    """
    print("\n📊 Interview Summary:")
    total_score = sum([item['rating'] for item in session_data])
    avg_score = total_score / len(session_data)
    print(f"Average Rating: {avg_score:.2f}/10")

    if avg_score >= 8:
        print("Verdict: 🌟 Excellent performance!")
    elif avg_score >= 5:
        print("Verdict: 👍 Good effort, room to improve.")
    else:
        print("Verdict: 🚧 Needs more preparation.")
