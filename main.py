import feedparser
import os
import pinecone
import numpy as np
import openai
import requests
from bs4 import BeautifulSoup

# OpenAI API key
openai.api_key = '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'

# get the Pinecone API key and environment
pinecone_api = 'd0faa6b9-5f2f-4e20-873c-8be45a594293'
pinecone_env = 'gcp-starter'

pinecone.init(api_key=pinecone_api, environment=pinecone_env)

# set index; must exist
index = pinecone.Index('chat-bot')


def insert(text, i):
    embedding = openai.Embedding.create(
        input=text,
        model='text-embedding-ada-002'
    )
    vector = embedding['data'][0]['embedding']
    response = index.upsert(vectors=[(str(i), vector, {"content": text})])
    print(response)
    return response


# vector created with OpenAI as well


def get_highest_score_url(vector):
    search_response = index.query(
        top_k=5,
        vector=vector,
        include_metadata=True
    )
    response = ''
    for i in search_response['matches']:
        response = response + \
            i['metadata']['content']
    return response
    # if highest_score_item["score"] > 0.8:
    #     return highest_score_item["metadata"]['url']
    # else:
    #     return ""
