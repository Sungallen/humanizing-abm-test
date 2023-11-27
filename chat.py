from main import insert
import openai
from main import get_highest_score_url
from db import query_data, insert_data
from evaluator import memory_evaluator

openai.api_key = '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'


def student_response(text, question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a language model which talks like daily conversation"},
            {"role": "system", "content": "You are a college student"},
            {"role": "user", "content": "Here is the content related to message from other sources:" +
                "\n---\n" + text + "Response the message based on the above sources, the messsage:" + question}

        ],
        temperature=0,
        max_tokens=200
    )
   # print(response)
    return response


def researcher_response(text, question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a language model which talks like daily conversation"},
            {"role": "system", "content": "You are a researcher"},
            {"role": "user", "content": "Here is the knowledge you knew before:" +
                "\n---\n" + text + "Response a message based on the above knowledge, the knowledge is probably not related to the message, so you don't have to really use it, the messsage:" + question}

        ],
        temperature=0,
        max_tokens=200
    )
    # print(response)
    return response


question = 'who is Allens?'

for i in range(2):
    query_result_student1 = str(query_data(
        'student1', question)['documents'][0])
    if i == 0:
        student1_response = student_response(query_result_student1, question)
    else:
        student1_response = student_response(
            query_result_student1, question)
    print('===================================student1=================================')
    print(student1_response["choices"][0]["message"]["content"])
    print('============================================================================')
    memory_evaluation = memory_evaluator(
        student1_response["choices"][0]["message"]["content"], question)
    if memory_evaluation != '':
        insert_data(
            'student2', student1_response["choices"][0]["message"]["content"], 'student2')
        insert_data(
            'researcher', student1_response["choices"][0]["message"]["content"], 'researcher')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!inserted', memory_evaluation)
    query_result_student2 = str(query_data(
        'student2', question)['documents'][0])
    student2_response = student_response(
        query_result_student2, question)
    print('===================================student2=================================')
    print(student2_response["choices"][0]["message"]["content"])
    print('============================================================================')
    memory_evaluation = memory_evaluator(
        student2_response["choices"][0]["message"]["content"], question)
    if memory_evaluation != '':
        insert_data(
            'student1', student2_response["choices"][0]["message"]["content"], 'student1')
        insert_data(
            'researcher', student2_response["choices"][0]["message"]["content"], 'researcher')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!inserted', memory_evaluation)
    query_result_researcher = str(query_data(
        'researcher', question)['documents'][0])
    researcher1_response = researcher_response(
        query_result_researcher, question)
    print('==================================researcher================================')
    print(researcher1_response["choices"][0]["message"]["content"])
    print('============================================================================')
    memory_evaluation = memory_evaluator(
        researcher1_response["choices"][0]["message"]["content"], question)
    if memory_evaluation != '':
        insert_data(
            'student1', researcher1_response["choices"][0]["message"]["content"], 'student1')
        insert_data(
            'student2', researcher1_response["choices"][0]["message"]["content"], 'student2')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!inserted', memory_evaluation)
