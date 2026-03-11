import requests

def fetch_remotive_jobs():

    url = "https://remotive.com/api/remote-jobs"

    resp = requests.get(url)
    jobs = resp.json().get("jobs", [])

    simplified = []

    for j in jobs:
        simplified.append({
            "title": j["title"],
            "company": j["company_name"],
            "desc": j["description"],
            "url": j["url"],
            "location": j["candidate_required_location"],
            "source": "remotive"
        })

    return simplified