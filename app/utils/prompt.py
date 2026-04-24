def build_prompt(purpose, tone, details):

    return f"""
    Write a professional email.

    Type: {purpose}
    Tone: {tone}
    Details: {details}

    Include:
    - Subject
    - Greeting
    - Body
    - Closing
    """