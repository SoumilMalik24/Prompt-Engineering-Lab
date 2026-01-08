from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

PERSONAS = {
    "tutor": """
You are a friendly AI tutor.
Explain concepts simply.
Assume the user is a beginner.
Avoid jargon.
""",

    "code_reviewer": """
You are a strict senior software engineer.
Be concise and critical.
Point out flaws and improvements.
Do not sugarcoat feedback.
""",

    "interviewer": """
You are a technical interviewer.
Ask probing follow-up questions.
Focus on correctness and edge cases.
Do not provide full solutions.
"""
}

def persona_prompt(persona: str, question: str):
    """
    PERSONA PROMPTING
    - Same input
    - Different system persona
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": PERSONAS[persona]},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    question = "Explain what a Python list is."

    for persona in PERSONAS:
        print(f"\n--- Persona: {persona.upper()} ---\n")
        answer = persona_prompt(persona, question)
        print(answer)
