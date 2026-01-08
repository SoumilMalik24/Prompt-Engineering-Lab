from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI()

def inst_prompt(system_prompt: str, user_prompt: str):
    """
    INST FORMAT PROMPTING
    - Manual instruction wrapping
    - Used by LLaMA-style models
    """

    prompt = f"""
<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{user_prompt} [/INST]
"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    system_prompt = "You are a strict Python instructor. Be concise."
    user_prompt = "Write a Python function to add n numbers."

    output = inst_prompt(system_prompt, user_prompt)

    print("\n--- INST Format Output ---\n")
    print(output)
