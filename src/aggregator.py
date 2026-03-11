def collect_jobs():

    from src.google_jobs_tool import fetch_google_jobs
    from src.remotive import fetch_remotive_jobs
    # from src.greenhouse import fetch_greenhouse_jobs
    from src.rss import fetch_rss_jobs
    from src.adzuna import fetch_adzuna_jobs

    jobs = []

    jobs += fetch_google_jobs()
    jobs += fetch_remotive_jobs()
    # jobs += fetch_greenhouse_jobs()
    jobs += fetch_rss_jobs()
    jobs += fetch_adzuna_jobs()

    return jobs