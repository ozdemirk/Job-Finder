import requests, json

def fetch_jobs():
    url = "https://remotive.com/api/remote-jobs"
    resp = requests.get(url)
    jobs = resp.json().get("jobs", [])
    simplified = [
        {
            "title": j["title"],
            "company": j["company_name"],
            "desc": j["description"],
            "url": j["url"],
            "location": j["candidate_required_location"]
        }
        for j in jobs
    ]
    with open("data/jobs_raw.json", "w") as f:
        json.dump(simplified, f, indent=2)
    print(f"Fetched {len(simplified)} jobs.")
    return simplified

if __name__ == "__main__":
    fetch_jobs()