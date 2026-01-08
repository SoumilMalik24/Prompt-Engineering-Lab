from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()


def render_step(parsed_result):
    step = parsed_result.get("step")
    content = parsed_result.get("content")

    if step == "START":
        print(f"\nSTART: {content}")
        return "continue"

    if step == "PLAN":
        print(f"PLAN: {content}")
        return "continue"

    if step == "OUTPUT":
        print(f"\nOUTPUT:\n{content}")
        return "break"



SYSTEM_PROMPT = f"""
You're an expert AI Assistant in resolving user queries using chain of thought.
You work in START, PLAN, and OUTPUT steps.

Rules:
- Strictly follow the given JSON output format
- Only run one step at a time
- The sequence is START → PLAN (multiple) → OUTPUT

Output JSON Format:
{{ "step": "START" | "PLAN" | "OUTPUT", "content": "string" }}

Example:
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN: {{ "step": "PLAN", "content": "User wants to solve a math problem" }}
PLAN: {{ "step": "PLAN", "content": "Apply BODMAS rule" }}
PLAN: {{ "step": "PLAN", "content": "Compute 5 / 10 = 0.5" }}
PLAN: {{ "step": "PLAN", "content": "Equation becomes 2 + 3 * 0.5" }}
PLAN: {{ "step": "PLAN", "content": "Compute 3 * 0.5 = 1.5" }}
PLAN: {{ "step": "PLAN", "content": "Equation becomes 2 + 1.5" }}
OUTPUT: {{ "step": "OUTPUT", "content": "3.5" }}
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Hey write me a code to add n numbers in python"}
]

while True:
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=messages   
            )

    raw = response.choices[0].message.content
    parsed_result = json.loads(raw)

    action = render_step(parsed_result)

    messages.append(
        {"role": "assistant", "content": raw}
    )

    if action == "break":
        break