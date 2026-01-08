from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def zero_shot_prompt(topic: str):
    """
    Zero-shot prompting:
    - No examples
    - Only instructions and constraints
    """

    prompt = f"""
            Explain the topic "{topic}" clearly.

            Constraints:
            - Use exactly 3 bullet points
            - Each bullet must be at most 15 words
            - Do not include examples
            - Keep language simple
            """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    topic = input("Enter a topic: ")
    output = zero_shot_prompt(topic)

    print("\n--- Zero-Shot Output ---\n")
    print(output)