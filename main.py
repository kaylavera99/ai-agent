import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function
from prompts import system_prompt
from config import MAX_ITERS
import sys


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) have been reached.")
            sys.exit(1)

        try:
            result = generate_content(client, messages, verbose) 
            if result:
                print("Final response: ", result)
                break

            
        except Exception as e:
            print("Error:", e)
            break


def generate_content(client, messages, verbose):
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        # Add candidate content to messages
        for candidate in response.candidates:
            if candidate.content:
                function_call_candidates = candidate.content
                messages.append(function_call_candidates)

    if not response.function_calls:
        return response.text

    function_responses = []

    # Execute any requested functions
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        
        function_response_text = function_call_result.parts[0].function_response.response
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

       
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    messages.append(types.Content(role="user", parts=function_responses))




    

if __name__ == "__main__":
    main()
