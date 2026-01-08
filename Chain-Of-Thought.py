from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()


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


response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Hey write me a code to add n numbers in python"},
            {"role": "assistant", "content": json.dumps({ "step": "START", "content": "User wants a Python code to add n numbers." })},
            {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Determine the requirements for adding n numbers."})},
            {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "The program should allow the user to input n numbers."})},
            {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Use a loop to iterate up to n and accumulate the sum."})},
            {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Return or print the sum of the n numbers."})},
            ]    
        )
""" 
OUTPUT:
{"step": "OUTPUT", "content": "Here's a simple Python code to add n numbers:\n\n
```python\n
# Function to add n numbers\n\n
# def add_n_numbers(n):\n
#     total = 0\n
#     for _ in range(n):\n
#         num = float(input('Enter a number: '))\n
#         total += num\n
#     return total\n\n
# # Main program\n\n
# n = int(input('How many numbers do you want to add? '))\n
# sum_of_numbers = add_n_numbers(n)\n
# print(f'The sum of the {n} numbers is: {sum_of_numbers}')\n
# ```"} 
"""

print(response.choices[0].message.content)

