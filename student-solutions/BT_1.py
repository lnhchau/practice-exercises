# Initial:
import time
import openai
import os
# from .config import settings
openai.api_key  = "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"
def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def prompts(text):
    summarize_prompt = f"""
    Summarize the text delimited by triple backticks \ 
    into a single sentence using the language of it.
    ```{text}```
    """
    inffering_prompt = f"""
    Identify the following items from the review text: 
    - Sentiment (positive or negative)
    - Is the reviewer expressing anger? (true or false)
    - Item purchased by reviewer
    - Company that made the item

    The review is delimited with triple backticks. \
    Format your response as a JSON object with "Sentiment", "Anger", "Item" and "Brand" as the keys.
    If the information isn't present, use "unknown" \
    as the value.
    Make your response as short as possible using the language of it.
    Format the Anger value as a boolean.

    Review text: '''{text}'''
    """
    language_prompt = f"Tell me what language this is: ```{text}```"
    transforming_prompt = f"""
    Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". 
    Translate the text from slang to a business letter using the language of it.
    Don't use any punctuation around the text:
    ```{text}```
    """
    mail_reply_prompt = f""""""
    return {"summarize":summarize_prompt, "inffering":inffering_prompt, "Original language":language_prompt, "transforming":transforming_prompt, "mail_reply":mail_reply_prompt}

if __name__ == '__main__':
    # Writing prompt
    exercise = str(input("Number of the excercise that you want to check: "))
    text = str(input("The contents: "))
    prompt_dict = prompts(text)
    if "1" in exercise:
        response = get_completion(prompt_dict["summarize"])
        print("summarize response: ", response)
    elif "2" in exercise:
        for prompt in prompt_dict.keys():
            try:
                response = get_completion(prompt_dict[prompt])
            except:
                time.sleep(20) # Limit of chatgpt accounts allowed
                response = get_completion(prompt_dict[prompt])
            print(f"{prompt} response: ", response)
