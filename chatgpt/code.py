import openai
openai.api_key = "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"

student_1_description = "David Nguyen is a sophomore majoring in computer science at Stanford University. He is Asian American and has a 3.8 GPA. David is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after graduating."

prompt1 = f'''
Please extract the following information from the given text and return it as a JSON object:

name
major
school
grades
club

This is the body of text to extract the information from:
{student_1_description}
'''
# Generating response back from gpt-3.5-turbo
openai_response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': "Hello"}]
)
response_1 = openai_response['choices'][0]['message']['content']