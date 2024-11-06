from dotenv import load_dotenv
import os
import google.generativeai as genai
import pandas as pd
import argparse
parser = argparse.ArgumentParser()
     
# -db DATABASE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-p", "--prompt", help="prompt to send to ai")
# file name
parser.add_argument("-f", "--file", help="path to write AI response to")
parser.add_argument("-u", "--userfile", help="file to get user prompt from")
# parse_args will turn terminal flags into python dictionary (key value pairs)
args = parser.parse_args()
# prompt and file are individual entries in args dictionary
prompt = args.prompt
if "userfile" in args:
    print(args.userfile)
    file_from_user = open(args.userfile)
    prompt = file_from_user.read()
    file_from_user.close()
file = args.file
load_dotenv()

api_key = os.getenv("API_KEY")
os.environ['API_KEY'] = api_key
genai.configure(api_key=os.environ['API_KEY'])

def get_completion(prompt, model="gemini-1.5-flash", **kwargs):
    model = genai.GenerativeModel(model)
    
    # Create a generation_config dictionary with default values
    generation_config = {
        "temperature": 0.8,
        "max_output_tokens": 200
    }
    
    # Update generation_config with any provided kwargs
    generation_config.update(kwargs)
    
    response = model.generate_content(prompt, generation_config=generation_config)
    return response.text

# print(get_completion("Tell me about Forests"))
text = get_completion(prompt or "Say Something")
f = open(file if file else "ai.md", "w")
# f = open("simple.md", "w")
# f.write(f"Prompt: {(prompt or "say something")} \nResponse: \n {text}")

text = "\n".join(text.split('\n')[1:-1]) # removes first and last line of text
f.write(f"{text}")
f.close()