import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import sys

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv:
         if  not arg.startswith("--"):
              args.append(arg)

    if not args:
        raise Exception("Error! No input provided!")
    user_prompt = " ".join(args)
    
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    if verbose:
        print(f"User prompt: {user_prompt}")
    
    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
        response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)

        if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("Response: ")
        print(response.text)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(1)
