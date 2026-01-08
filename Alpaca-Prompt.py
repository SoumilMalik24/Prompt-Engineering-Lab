from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def alpaca_prompt(instruction: str, input_text: str | None = None):
    """
    ALPACA PROMPTING
    - Instruction-tuned prompt format
    - No chat roles
    """

    if input_text:
        prompt = f"""
### Instruction:
{instruction}

### Input:
{input_text}

### Response:
"""
    else:
        prompt = f"""
### Instruction:
{instruction}

### Response:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    instruction = "Write a Python function to add n numbers."
    input_text = "The numbers should be taken from user input."

    output = alpaca_prompt(instruction, input_text)

    print("\n--- Alpaca Prompt Output ---\n")
    print(output)
