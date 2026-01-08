from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def run_chatml(system_prompt: str, user_prompt: str):
    """
    CHATML SCHEMA DEMO
    - Demonstrates role-based message hierarchy
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    user_question = "Explain what a Python dictionary is."

    system_prompts = {
        "default": "You are a helpful assistant.",
        "strict": "You are a strict technical instructor. Be concise and precise.",
        "friendly": "You are a friendly tutor explaining to a beginner."
    }

    for label, sys_prompt in system_prompts.items():
        print(f"\n--- System Persona: {label.upper()} ---\n")
        output = run_chatml(sys_prompt, user_question)
        print(output)
