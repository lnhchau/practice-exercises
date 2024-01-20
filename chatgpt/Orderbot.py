import os
import openai

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]
pizza_types = "The menu is written by csv format with the header: pizza type, cost. Here is the csv menu content: " \
              "pizza_1, 5$" \
              "pizza_2, 6$" \
              "pizza_3, 10$"
messages =  [  
# {'role':'system', 'content':f'You are order pizza chatbot. You need to show the table of menu from {pizza_types} for the user when they ask for order the pizza and collect the information of users: name, the destination address, ordered date, payment method and total prize. '
#                             f'Return the Json format: '+
#                             '{"name": name of user, "address": adress of user, "ordered_date": order date, "payment_method": method, "total_prize": total prize }'},
    {"role":"system","content":"You are order pizza chatbot and you need to do the following step: "
                               "1. Ask the user name"
                               "2. Show the menu which is "+pizza_types+" and ask for order"
                                "3.Ask for time, and day for order"
                                "4. Ask for payment method"
                                "5. Then calculate the total prize"
                                "6. Return the JSON content with the format "
                                "{'name':...,'order_product':...,'order_date':...,'payment_method':...,'total_prize':...}"},
{'role':'assistant', 'content':'Hi, there, I am a chatbot TMK, nice to meet you'}]

# Initial message: say hi of chatbot
print("Hi, there, I am a chatbot TMK, nice to meet you")
while True:
    user_input = input("System message: ")
    messages.append({"role":"system","content":user_input})
    bot_response = get_completion_from_messages(messages, temperature=1)
    print("Bot message: ",bot_response)
    messages.append({"role":"assistant","content":bot_response})