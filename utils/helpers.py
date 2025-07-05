# utils/helpers.py

def clean_text(text):
    """Strip and lowercase user input."""
    return text.strip().lower()

def is_valid_role(role, valid_roles):
    """Check if entered role is supported."""
    return role.lower() in [r.lower() for r in valid_roles]
