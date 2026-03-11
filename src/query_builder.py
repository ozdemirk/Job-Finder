def build_queries(profile):
    roles = profile["desired_roles"]
    skills = profile.get("skills", [])
    locations = profile["locations"]

    queries = []

    for role in roles:
        for loc in locations:
            queries.append(f"{role} {loc}")

        for skill in skills:
            queries.append(f"{skill} {role}")

    return list(set(queries))