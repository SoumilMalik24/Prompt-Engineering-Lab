import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()

def structured_output(text: str):
    """
    STRUCTURED OUTPUT PROMPTING
    - Forces strict JSON output
    - No free-form text
    """

    prompt = f"""
            Extract structured information from the text below.

            Return ONLY valid JSON.
            Do NOT include explanations or extra text.

            Required JSON schema:
            {{
            "topic": string,
            "summary": string,
            "difficulty_level": "beginner" | "intermediate" | "advanced"
            }}

            Text:
            \"\"\"{text}\"\"\"
            """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=200
    )

    raw_output = response.choices[0].message.content

    try:
        parsed = json.loads(raw_output)
        return parsed
    except json.JSONDecodeError:
        print("Model did not return valid JSON")
        print(raw_output)
        return None


if __name__ == "__main__":
    input_text = input("Enter text: ")
    result = structured_output(input_text)

    print("\n--- Structured Output ---\n")
    print(result)
