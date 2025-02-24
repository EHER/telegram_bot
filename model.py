import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME")
PIPELINE_TYPE = os.getenv("PIPELINE_TYPE")

chatbot = pipeline(PIPELINE_TYPE, model=MODEL_NAME)

def process_message(message: str) -> str:
    response = chatbot(message)
    return response[0]['generated_text']

if __name__ == "__main__":
    import sys
    print(process_message(sys.argv[1]))
