from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

def one_shot_prompt(topic: str):
    """
    ONE-SHOT PROMPTING
    - One example is provided
    - Model learns format from demonstration
    """

    prompt = f"""
            You are a helpful tutor.

            Task:
            Explain a topic in the following format:

            Definition:
            <one sentence>

            Key Points:
            - point 1
            - point 2
            - point 3

            Example:

            Topic: Machine Learning

            Definition:
            Machine Learning is a subset of AI that learns patterns from data.

            Key Points:
            - Uses data to improve performance
            - Learns without explicit programming
            - Commonly used in predictions

            Now do the same for this topic:

            Topic: {topic}
            """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful tutor."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    topic = input("Enter a topic: ")
    output = one_shot_prompt(topic)

    print("\n--- One-Shot Output ---\n")
    print(output)
