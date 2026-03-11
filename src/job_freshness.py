import re

def parse_posted_time(posted_text):
    if not posted_text:
        return None

    posted_text = posted_text.lower()

    hours_match = re.search(r"(\d+)\s*hour", posted_text)
    days_match = re.search(r"(\d+)\s*day", posted_text)

    if hours_match:
        return int(hours_match.group(1))

    if days_match:
        return int(days_match.group(1)) * 24

    return None

def filter_fresh_jobs(jobs, max_age_hours=72):
    fresh_jobs = []

    for job in jobs:
        posted_text = job.get("posted_at")

        hours = parse_posted_time(posted_text)
        
        print(f"Posted text: {posted_text} -> Hours: {hours}")

        if hours is None:
            continue

        if hours <= max_age_hours:
            fresh_jobs.append(job)

    return fresh_jobs