from main import get_highest_score_url
import openai

openai.api_key = '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'

text = 'what is your name?'
embedding = openai.Embedding.create(
    input=text,
    model='text-embedding-ada-002'
)

print(get_highest_score_url(embedding['data'][0]['embedding']))
