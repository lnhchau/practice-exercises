# Initial:
import openai
import os
from .config import settings
openai.api_key  = "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"
def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def prompts():
    summarize_prompt = f"""
    Summarize the text delimited by triple backticks \ 
    into a single sentence. Use the language of the text
    ```{text}```
    """
    inffering_prompt = f"""
    Identify the following items from the review text: 
    - Sentiment (positive or negative)
    - Is the reviewer expressing anger? (true or false)
    - Item purchased by reviewer
    - Company that made the item

    The review is delimited with triple backticks. \
    Format your response as a JSON object with \
    "Sentiment", "Anger", "Item" and "Brand" as the keys.
    If the information isn't present, use "unknown" \
    as the value.
    Make your response as short as possible.
    Format the Anger value as a boolean.

    Review text: '''{text}'''
    """
    transforming_prompt = f""""""
    mail_reply_prompt = f""""""
    return {"summarize":summarize_prompt, "inffering":inffering_prompt, "transforming":transforming_prompt, "mail_reply":mail_reply_prompt}

if __name__ == '__main__':
    # Writing prompt
    prompt_dict = prompts()
    exercise = str(input("Number of the excercise that you want to check: "))
    text = str(input("The contents: "))
    if "1" in exercise:
        response = get_completion(prompt_dict["summarize"])
        print("summarize response: ", response)
    elif "2" in exercise:
        for prompt in prompt_dict.keys():
            response = get_completion(prompt_dict[prompt])
            print(f"{prompt} response: ", response)