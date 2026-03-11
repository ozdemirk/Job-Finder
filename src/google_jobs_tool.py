import os
import json
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
from src.source_detector import detect_source

def extract_url_and_source(job):
    apply_options = job.get("apply_options", [])

    if not apply_options:
        return "", "unknown"

    # Strategy:
    # 1. Prefer LinkedIn if present
    # 2. Otherwise prefer company site (first link)
    
    for option in apply_options:
        link = option.get("link", "")
        if "linkedin.com" in link:
            return link, "linkedin"

    # fallback: first apply option
    first_link = apply_options[0].get("link", "")
    return first_link, detect_source(first_link)

def fetch_google_jobs(query="AI healthcare product"):
    api_key = os.getenv("SERPAPI_KEY")
    
    params = {
        "engine": "google_jobs",
        "q": query,
        #"location": "Istanbul, Turkey",   
        "google_domain": "google.com.tr",  # Turkey
        "hl": "en",
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    
    jobs = results.get("jobs_results", [])
    
    simplified = []
    for j in jobs:
        url, source = extract_url_and_source(j)

        simplified.append({            
            "title": j.get("title"),
            "company": j.get("company_name"),
            "location": j.get("location"),
            "url": url,
            "source": source,
            "desc": j.get("description", ""),
            "posted_at": j.get("detected_extensions", {}).get("posted_at"),
            "job_id": j.get("job_id")
        })

    print(f"Fetched {len(simplified)} Google Jobs results.")
    return simplified