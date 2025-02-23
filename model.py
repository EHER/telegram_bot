import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME", "mistralai/Mistral-7B-Instruct")
PIPELINE_TYPE = os.getenv("PIPELINE_TYPE", "text-generation")

chatbot = pipeline(PIPELINE_TYPE, model=MODEL_NAME)

def process_message(message: str) -> str:
    response = chatbot(message, max_length=150, do_sample=True, temperature=0.7)
    return response[0]['generated_text']

if __name__ == "__main__":
    import sys
    print(process_message(sys.argv[1]))
