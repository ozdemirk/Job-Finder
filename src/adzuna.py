import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_adzuna_jobs():

    app_id = os.getenv("ADZUNA_ID")
    app_key = os.getenv("ADZUNA_KEY")

    url = "https://api.adzuna.com/v1/api/jobs/tr/search/1"

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "what": "product manager",
        "where": "Turkey"
    }

    resp = requests.get(url, params=params)
    data = resp.json()

    jobs = []

    for j in data.get("results", []):

        job = {
            "title": j["title"],
            "company": j["company"]["display_name"],
            "desc": j["description"],
            "url": j["redirect_url"],
            "location": j["location"]["display_name"],
            "source": "adzuna"
        }

        jobs.append(job)
    print(f"Adzuna: {len(jobs)} jobs")
    return jobs