# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv(
#         "OPENAI_API_KEY"
#     )
# )

# def generate_response(
#     question,
#     context
# ):

#     prompt = f"""
#     You are an AI assistant for an electronic shop.

#     Answer only from provided context.

#     Context:
#     {context}

#     User Question:
#     {question}
#     """

#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return response.choices[0].message.content

######Gemini

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
conversation_history = []
def generate_response(question, context):
    global conversation_history

    history_text = "\n".join(conversation_history[-4:])

    prompt = f"""
You are a professional AI assistant for an electronics shop.

Your job is to help customers naturally and professionally.

Rules:
- Answer like a real customer support executive.
- Give short, clear, human-friendly answers.
- NEVER mention:
  - context
  - provided information
  - AI limitations
  - missing data
- NEVER say:
  "I don't have information"
  "Based on provided context"
  "I can only answer from context"

If the shop does not provide a product/service,
reply naturally like:
- "Sorry, we currently do not provide that service."
- "Currently this product is not available."
- "We don't offer that facility at the moment."

If product/service exists:
- answer confidently
- be helpful
- sound natural
Previous Conversation:
    {history_text}

    Context:
    {context}

    User Question:
    {question}
    """

    # response = client.models.generate_content(
    #    # model="gemini-2.5-flash",
    #     model="gemini-2.0-flash",
        
    #     contents=prompt
    # )

    # #return response.text
    # answer = response.text 
    # # store user question
    # conversation_history.append( f"User: {question}" ) 
    # # store assistant answer 
    # conversation_history.append( f"Assistant: {answer}" ) 
    # return answer
    try: 
        response = client.models.generate_content( model="gemini-2.5-flash", contents=prompt ) 
        answer = response.text
    except Exception as e: 
        print("Gemini Error:", e) 
        answer = ( "Sorry, the AI assistant is currently busy. " "Please try again after some time." ) 
        # store user question 
        conversation_history.append( f"User: {question}" )
        # store assistant answer 
        conversation_history.append( f"Assistant: {answer}" ) 
    return answer