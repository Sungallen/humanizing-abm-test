from transformers import AutoTokenizer, BertForQuestionAnswering
import torch
from transformers import pipeline

summarizer = pipeline(
    "summarization", model="facebook/bart-large-cnn", device=0)
tokenizer = AutoTokenizer.from_pretrained("deepset/bert-base-cased-squad2")
model = BertForQuestionAnswering.from_pretrained(
    "deepset/bert-base-cased-squad2")

question, text = "Who was Jim Henson?", "Based on the information you provided to me, I can't answer who Jim Henson was."


def memory_evaluator(content, question):
    summary = summarizer(content, max_length=130,
                         min_length=1, do_sample=False)
    inputs = tokenizer(question, summary[0]
                       ['summary_text'], return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    answer_start_index = outputs.start_logits.argmax()
    answer_end_index = outputs.end_logits.argmax()
    predict_answer_tokens = inputs.input_ids[0,
                                             answer_start_index: answer_end_index + 1]

    return tokenizer.decode(predict_answer_tokens, skip_special_tokens=True)
