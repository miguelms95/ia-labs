import json
from transformers import pipeline

# model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
# model_id = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I love you", "I hate you"]

result = []
for item in data:
    result.append({"text": item, "sentiment": sentiment_pipeline(item)})

print(json.dumps(result, indent=2))
