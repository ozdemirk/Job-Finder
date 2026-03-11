from src.scrape_jobs import fetch_jobs as fetch_remotive
from src.google_jobs_tool import fetch_google_jobs

def fetch_from_source(source, query):
    if source == "remotive":
        return fetch_remotive()
    elif source == "google_jobs":
        return fetch_google_jobs(query)
    else:
        raise ValueError("Unknown source")