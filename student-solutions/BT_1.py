# Initial:
import openai
import os
from .config import settings
openai.api_key  = settings.OPENAI_API_KEY
def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

if __name__ == '__main__':
    # Writing prompt
    text = str(input("The contents: "))
    prompt = f"""
    Summarize the text delimited by triple backticks \ 
    into a single sentence. Use the language of the text
    ```{text}```
    """
    response = get_completion(prompt, model="gpt-3.5-turbo")
    print(response)