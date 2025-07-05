import pandas as pd
import random
import os

# Load dataset
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'full_interview_questions_dataset.csv'))
df = pd.read_csv(data_path)

# Normalize fields to prevent filtering issues
df['category'] = df['category'].astype(str).str.lower().str.strip()
df['difficulty'] = df['difficulty'].astype(str).str.lower().str.strip()
df['question'] = df['question'].astype(str).str.strip()

# Track used questions
used_questions = set()

def get_next_question(role=None, mode=None):
    """
    Returns the next unique question filtered by role (category) and mode (difficulty).
    If no matching question is available, returns None.
    """
    global used_questions

    filtered_df = df.copy()

    # Normalize input filters
    if role:
        role = role.lower().strip()
        filtered_df = filtered_df[filtered_df['category'] == role]

    if mode:
        mode = mode.lower().strip()
        filtered_df = filtered_df[filtered_df['difficulty'] == mode]

    # Remove already used questions
    available_df = filtered_df[~filtered_df['question'].isin(used_questions)]

    if available_df.empty:
        return None

    selected_row = available_df.sample(1).iloc[0]
    question = selected_row['question']
    difficulty = selected_row['difficulty']

    used_questions.add(question)
    return question, difficulty

# Optional debugging helper
if __name__ == "__main__":
    print("✅ Available categories:", df['category'].unique())
    print("✅ Available difficulties:", df['difficulty'].unique())
    print("✅ Sample question:", get_next_question("hr", "easy"))
