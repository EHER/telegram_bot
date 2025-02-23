import sys
from transformers import pipeline

def process_message(message):
    classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
    results = classifier(message)
    return str(results)

if __name__ == "__main__":
    print(process_message(sys.argv[1]))
