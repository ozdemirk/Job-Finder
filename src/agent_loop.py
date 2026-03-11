import json
import datetime
import hashlib
from src.job_tools import fetch_from_source
from src.match_jobs import rank_jobs
from src.explain_matches import generate_explanations
from src.query_builder import build_queries
from src.job_freshness import filter_fresh_jobs
from src.memory import load_memory, save_memory, filter_new_jobs


def generate_job_id(job):

    base = (
        job.get("title","") +
        job.get("company","") +
        job.get("url","")
    )

    return hashlib.md5(base.encode()).hexdigest()

def choose_source(profile):
    # Simple logic for now (we'll make this LLM-based later)
    if "Remote" in profile["locations"]:
        return "remotive"
    return "google_jobs"

def agent_cycle(profile):
    print("🤖 Running Job Agent...")

    # with open("data/my_profile.json") as f:
    #     profile = json.load(f)

    source = choose_source(profile)
    print(f"Selected source: {source}")

    query = " ".join(profile["desired_roles"])
    
    queries = build_queries(profile)
    
    print(f"Queries: {queries}")
    
    all_jobs = []
    
    seen_ids = load_memory()

    for q in queries:
        jobs = fetch_from_source(source,q)
        all_jobs.extend(jobs)
        
    new_jobs = filter_new_jobs(all_jobs, seen_ids)
    seen_ids.update([j["job_id"] for j in new_jobs])
    save_memory(seen_ids)
    
    # jobs = fetch_from_source(source, query)
    # allowed_locations = [
    # "Turkey",
    # "UAE",
    # "Saudi Arabia",
    # "Qatar",
    # "Remote"
    # ]
    # filtered_jobs = [
    #     j for j in all_jobs
    #     if any(loc in j.get("location","") for loc in allowed_locations)
    # ]

    # all_jobs = filter_fresh_jobs(all_jobs, max_age_hours=144)

    with open("data/jobs_raw.json", "w") as f:
        json.dump(all_jobs, f, indent=2)

    rank_jobs()
    generate_explanations()

    print("✅ Agent cycle complete.")
    print(datetime.datetime.now())

if __name__ == "__main__":

    agent_cycle()



