import random

def rate_answer(answer, question):
    """
    Dummy scoring logic for answer rating.
    Returns an integer score between 1 and 10.
    """
    length = len(answer.strip())

    if length < 20:
        return random.randint(2, 5)
    elif length < 50:
        return random.randint(5, 7)
    else:
        return random.randint(7, 10)
