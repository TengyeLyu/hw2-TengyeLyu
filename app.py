import os
from google import genai

SYSTEM_PROMPT = """
You are a customer support assistant for an online retail company.

Write a polite, professional, and helpful email reply to the customer.

Rules:
- Be clear and concise.
- Stay calm, even if the customer is upset.
- Do not invent company policies.
- Do not promise refunds, compensation, or guarantees unless clearly confirmed.
- If the case is unclear or sensitive, say that the issue will be reviewed by a human support agent.
"""

TEST_CASES = [
    {
        "name": "Test Case 1: Normal case",
        "customer_input": "Hi, my order has not arrived yet. Can you tell me where it is?"
    },
    {
        "name": "Test Case 2: Normal case",
        "customer_input": "Hello, I forgot my password and cannot log into my account. Can you help me reset it?"
    },
    {
        "name": "Test Case 3: Edge case",
        "customer_input": "I returned my item two weeks ago but I still have not received my refund. I am very disappointed."
    },
    {
        "name": "Test Case 4: Human review case",
        "customer_input": "Your company is awful. I want a full refund, extra compensation, and I want you to guarantee this will never happen again."
    },
    {
        "name": "Test Case 5: Policy ambiguity case",
        "customer_input": "Can I return an item after three months if I already opened it?"
    }
]


def generate_reply(client, customer_input):
    full_prompt = f"""
{SYSTEM_PROMPT}

Customer message:
{customer_input}

Write the email reply below:
"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=full_prompt
    )
    return response.text


def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY is not set.")
        print("Please set your API key in the terminal before running this script.")
        return

    client = genai.Client(api_key=api_key)

    print("=" * 60)
    print("Customer Support Email Drafting Prototype")
    print("=" * 60)

    for case in TEST_CASES:
        print(f"\n{case['name']}")
        print("-" * 60)
        print("Customer Input:")
        print(case["customer_input"])
        print("\nModel Output:")
        try:
            reply = generate_reply(client, case["customer_input"])
            print(reply)
        except Exception as e:
            print(f"Error during API call: {e}")

        print("-" * 60)


if __name__ == "__main__":
    main()
