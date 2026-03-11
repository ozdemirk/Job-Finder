import feedparser
from src.match_jobs import job_matches

def fetch_rss_jobs():

    rss_urls = [
            "https://rss.indeed.com/rss?q=product+manager&l=Turkey",
            "https://rss.indeed.com/rss?q=project+manager&l=Istanbul"
    ]

    jobs = []

    for url in rss_urls:

        feed = feedparser.parse(url)

        for entry in feed.entries:

            job = {
                "title": entry.title,
                "company": "unknown",
                "desc": entry.summary,
                "url": entry.link,
                "location": "Remote",
                "source": "rss"
            }
            if job_matches(job):
                print(f"append {job["title"]}")
                jobs.append(job)
    print(f"Indeed: {len(jobs)} jobs")        
    return jobs