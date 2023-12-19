# purpose: functionality testing of Dalia chatbot with the openai api

# first load virtual env with: source openai-env/bin/activate
# then: source ~/.zshrc (to load the interactive shell)
# to confirm shell has loaded your key: echo $OPENAI_API_KEY
import openai
import time
from openai import OpenAI
# Initialize the OpenAI client to interact with the OpenAI API
client = OpenAI()

# Initialize the flag variable
chat_session_initiated = False

print(f"Sending request to OpenAI API...")
# The main input is the 'messages' parameter. Messages must be an array of message 
  # objects, where each object has a role (either "system", "user", or "assistant") and content.
messages=[
    # Conversations can be as short as one message or many back and forth turns.
    # Typically, a conversation is formatted with a system message first, 
    # followed by alternating user and assistant messages.

    # The "system" message helps set the behavior of the assistant such as "You are a helpful assistant."
    {"role": "system", "content": "You are Dalia, a knowledgeable and friendly AI assistant to Alex, your sole client."},
    {"role": "system", "content": "Dalia is well-versed in technology, philosophy, career development, and offers practical life advice."},
    {"role": "system", "content": "Dalia is consistently interested in how Alex's day is going and what he has been up to."},
    {"role": "system", "content": "Dalia responds to Alex in a helpful and thoughtful manner, providing concise responses that are generally less than 30 tokens long."},
    ]
# print the time delay and text received only if the chat session is not already initiated

while True:
  if not chat_session_initiated:
    print(f"Success! Chat session with Dalia initialized\nGo ahead. When you want to end the chat, type 'exit'.")
    print(f"============================================================================\n")
  chat_session_initiated = True # set the flag to True after the message is printed once

  user_input = input("Alex: ")
  if user_input.lower() == 'exit':
      print("\n============================================================================")
      print("That's the end of this chat!\nExiting...")
      break
    # Add the user's message to the conversation history
  messages.append({"role": "user", "content": user_input})

  try:
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=messages,
          temperature=1,
          max_tokens=30,
      )
      reply_content = response.choices[0].message.content
      print(f"Dalia: {reply_content}")
      # Add Dalia's response to the conversation history
      messages.append({"role": "assistant", "content": reply_content})

    # error messages to be printed if api key is not loaded
  except openai.APIError as e:
    #Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")
    break
  except openai.APIConnectionError as e:
    #Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")
    break
  except openai.RateLimitError as e:
    #Handle rate limit error (we recommend using exponential backoff)
    print(f"OpenAI API request exceeded rate limit: {e}")
    break





