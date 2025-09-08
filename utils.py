
def clean_text(text: str) -> str:
    return text.strip()

def detect_command(text: str) -> str:
    lowered = text.lower()
    if lowered.startswith("/translate"):
        return "translate"
    elif lowered.startswith("/define"):
        return "define"
    elif lowered.startswith("/grammar"):
        return "grammar"
    elif lowered.startswith("/chat"):
        return "chat"
    return ""
