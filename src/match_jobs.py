import json
from sentence_transformers import SentenceTransformer, util
from src.query_builder import build_queries

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_data():
    with open("data/my_profile.json") as f:
        profile = json.load(f)
    with open("data/jobs_raw.json") as f:
        jobs = json.load(f)
    return profile, jobs

def score_job(job, profile):
    text = (job["title"] + " " + job["desc"]).lower()
    score = 0
    for skill in profile["skills"]:
        if skill.lower() in text:
            score += 1
    return score

def semantic_match(job, profile, profile_text):
    job_text = job["title"] + " " + job["desc"]
    job_vec = model.encode(job_text)
    profile_vec = model.encode(profile_text)
    return float(util.cos_sim(job_vec, profile_vec))

def rank_jobs():
    profile, jobs = load_data()
    profile_text = " ".join(profile["skills"]) + " " + " ".join(profile["desired_roles"])
    ranked = []
    for job in jobs:
        rule_score = score_job(job, profile)
        sim_score = semantic_match(job, profile, profile_text)
        total = rule_score + sim_score * 10
        ranked.append((total, job))
    ranked = sorted(ranked, key=lambda x: x[0], reverse=True)
    top_jobs = [j for _, j in ranked[:20]]
    with open("data/jobs_filtered.json", "w") as f:
        json.dump(top_jobs, f, indent=2)
    print("Top 20 jobs saved.")
    return top_jobs

def job_matches(job):
    
    with open("data/my_profile.json") as f:
        profile = json.load(f)
    queries = build_queries(profile)

    text = (job["title"] + " " + job["desc"]).lower()

    for qr in queries:
        if qr in text:
            # print(f"TRUE qr and text: {qr}, {job["title"]}")
            return True
    # print(f"FALSE qr and text: {qr}, {job["title"]}")
    return False

if __name__ == "__main__":
    rank_jobs()