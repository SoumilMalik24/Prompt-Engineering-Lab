from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def few_shot_classify(text: str):
    """
    FEW-SHOT PROMPTING
    Task: Text classification using examples
    """

    prompt = f"""
            Classify the following user message into one of the categories:
            - BUG
            - FEATURE_REQUEST
            - GENERAL_QUERY

            Examples:

            Message: The app crashes when I click the submit button.
            Category: BUG

            Message: Can you add dark mode to the app?
            Category: FEATURE_REQUEST

            Message: How do I reset my password?
            Category: GENERAL_QUERY

            ---

            Message: {text}
            Category:
            """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    user_text = input("Enter user message: ")
    category = few_shot_classify(user_text)

    print("\n--- Predicted Category ---\n")
    print(category)
