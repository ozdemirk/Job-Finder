import os, json, openai
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import time
from huggingface_hub.errors import HfHubHTTPError

load_dotenv()

api_key=os.getenv("HUGGINGFACE_TOKEN")

#client = InferenceClient()

client = InferenceClient(
    model="openai/gpt-oss-120b",
    token=api_key
)

def explain_match(job, profile):
    prompt = f"""
    You are a career assistant. Explain briefly why this job might be a good fit for the person.

    Profile: {profile}
    Job: {job['title']} at {job['company']}
    Description: {job['desc'][:400]}
    """
    try:
        response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        )
        return response.choices[0].message.content.strip()
        
    except HfHubHTTPError as e:
        return "Rate limit hit in Huggingface. Cannot get explanation from AI model"


def generate_explanations():
    with open("data/jobs_filtered.json") as f:
        jobs = json.load(f)
    with open("data/my_profile.json") as f:
        profile = json.load(f)

    for job in jobs:
        job["reason"] = explain_match(job, profile)
    with open("data/jobs_filtered.json", "w") as f:
        json.dump(jobs, f, indent=2)
    print("Added GPT explanations.")

if __name__ == "__main__":
    generate_explanations()