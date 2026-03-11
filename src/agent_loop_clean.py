import json
from src.aggregator import collect_jobs
from src.match_jobs import rank_jobs


def agent_cycle():

    jobs = collect_jobs()

    print(f"Collected {len(jobs)} jobs")

    # later you will add:
    # deduplication
    # freshness filtering
    # ranking
    with open("data/jobs_raw.json", "w") as f:
        json.dump(jobs, f, indent=2)

    rank_jobs()

if __name__ == "__main__":
    agent_cycle()