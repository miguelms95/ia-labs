from transformers import pipeline

#model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
model_id = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

sentiment_pipe = pipeline("sentiment-analysis", model=model_id)

print(sentiment_pipe('i love you'))
