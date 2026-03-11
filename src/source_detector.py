from urllib.parse import urlparse

def detect_source(url):
    if not url:
        return "unknown"

    domain = urlparse(url).netloc.lower()

    if "linkedin.com" in domain:
        return "linkedin"

    if "indeed.com" in domain:
        return "indeed"

    if "glassdoor.com" in domain:
        return "glassdoor"

    if "monster.com" in domain:
        return "monster"

    if "ziprecruiter.com" in domain:
        return "ziprecruiter"

    # If not known job board → assume company site
    if domain:
        return "company_site"

    return "unknown"