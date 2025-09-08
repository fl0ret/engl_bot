from generate import chat_with_ai

def get_grammar_prompt(topic: str) -> str:
    return f"Объясни грамматическую тему '{topic}' на английском языке простыми словами и с примерами."

def get_word_definition_prompt(word: str) -> str:
    return f"Explain the meaning of the word '{word}' in simple English and provide an example sentence."

def get_translation_prompt(text: str) -> str:
    return f"Translate the following text to English or Russian, depending on input: {text}"

def get_conversation_prompt() -> str:
    return "Ты дружелюбный англоговорящий собеседник. Общайся естественно, задавай встречные вопросы. Если пользователь использует сленг, используй его тоже. Так же если пользователь обладает высоким уровнем англиского, общайся соответственно."

def generate_daily_words_via_ai():
    prompt = (
        "Сгенерируй 5 полезных английских слов для изучения с переводом на русский и примером использования. "
        "Формат: слово - перевод - пример."
    )
    return chat_with_ai(prompt)