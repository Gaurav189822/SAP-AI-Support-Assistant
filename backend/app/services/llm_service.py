import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(
    query,
    retrieved_context
):

    print("\nGenerating AI response...")

    prompt = f"""
    You are an SAP support assistant.

    User Query:
    {query}

    Retrieved SAP Knowledge:
    {retrieved_context}

    Instructions:
    - Answer only from retrieved knowledge
    - Be concise and technical
    - Mention SAP modules if possible
    - Suggest troubleshooting steps
    - Avoid hallucinations
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response = completion.choices[0].message.content

    return response