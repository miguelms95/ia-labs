from transformers import pipeline

# model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
# model_id = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

# pipe = pipeline(model="FacebookAI/roberta-large-mnli")
# data = ["I love you", "I hate you"]

pipe = pipeline(model="FacebookAI/roberta-large-mnli")
print(pipe("This restaurant is awesome"))
# [{'label': 'NEUTRAL', 'score': 0.7313136458396912}]

# print(pipe(data[0]))