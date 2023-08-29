import json
import time
import openai
import datetime

# from .config import settings

def get_completion_from_messages(messages, model="gpt-3.5-turbo"):
    openai.api_key  = "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"
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def collect_messages(context, prompt):
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    return response

def get_user_info(context):
    exit_flag = False
    response = ""
    while not exit_flag:
        prompt = input('You: ')
        try:
            response = collect_messages(context, prompt)
        except:
            time.sleep(20) # Limit of chatgpt accounts allowed
            response = collect_messages(context, prompt)
        print(f'OrderBot: {response}')
        exit_flag = True if "see you later" in response.lower() or "hẹn gặp lại bạn" in response.lower() else False
    return context

def get_order_info(context):
    messages = context.copy()
    messages.append(
    {'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\
    The fields should be 1) name of customer 2) The address of customer 3) list of pizzas, and the number of them   4) total price  5) the datetime of the order 6) The payment'},    
    )

    try:
        response = get_completion_from_messages(messages)
    except:
        time.sleep(20) # Limit of chatgpt accounts allowed
        response = get_completion_from_messages(messages)
    return response

def get_ordering_time(response):
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    response = json.loads(response)
    response["order_datetime"] = current_time
    response = json.dumps(response)
    return response

if __name__ == '__main__':
    context = [ {'role':'system', 'content':"""
        You are OrderBot, an automated service to collect orders for a pizza restaurant. \
        Using language of the menu. The menu includes \
        ```
        - Pizza type 1: Seafood, 2mm thick crust, 15cm diameter, price 3.5$
        - Pizza type 2: Sausage, meatball, 2mm thick crust, 15cm diameter, price 3$
        - Pizza type 3: Spicy, 2mm thick crust, 17cm diameter, price 4.5$.
        ```
        You first greet the customer, then collects the buyer's name, 
        then you ask for an address, \
        You give the menu for buyer then wait to collect the entire order, then summarize it and check for a final \
        time if the customer wants to add anything else. \
        Finally you collect the payment.\
        Make sure to clarify all options, extras and sizes to uniquely identify the item from the menu.\
        Once the order is confirmed, you will extract the current time and collect it along with the order details. \
        You respond in a short, very conversational friendly style. \
        At the end of the conversation, respond the text below without formatting or translating::
        ```See you later!``` \
        Note: Using the language of the buyer to respond.
        """} ] # accumulate messages
    context = get_user_info(context)
    response = get_order_info(context)
    final_response = get_ordering_time(response)
    print(final_response)