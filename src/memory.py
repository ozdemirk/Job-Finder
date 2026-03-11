import json
import os

MEMORY_FILE = "data/seen_jobs.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return set()

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    return set(data.get("seen_job_ids", []))


def save_memory(job_ids):
    with open(MEMORY_FILE, "w") as f:
        json.dump({"seen_job_ids": list(job_ids)}, f)

def filter_new_jobs(jobs, seen_ids):

    new_jobs = []

    for job in jobs:
        job_id = job.get("job_id")

        if job_id not in seen_ids:
            new_jobs.append(job)

    return new_jobs