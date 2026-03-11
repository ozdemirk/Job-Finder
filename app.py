import streamlit as st, json
from src.agent_loop import agent_cycle

st.title("🤖 AI Job Finder")
st.write("Automatically matched jobs based on your skills.")

st.title("AI Job Finder")

st.sidebar.header("Your Profile")

skills = st.sidebar.text_area(
    "Skills (comma separated)",
    "Product Management, AI, Strategy"
)

experience = st.sidebar.selectbox(
    "Experience Level",
    ["Junior", "Mid", "Senior", "Lead"]
)

preferred_locations = st.sidebar.text_input(
    "Preferred Locations",
    "Turkey, UAE, Remote"
)

job_types = st.sidebar.multiselect(
    "Job Type",
    ["Remote", "Hybrid", "On-site"]
)

search_button = st.sidebar.button("Search Jobs")

if search_button:
    profile = {
        "skills": [s.strip() for s in skills.split(",")],
        "experience": experience,
        "locations": preferred_locations,
        "job_types": job_types
    }
    
    agent_cycle(profile)
    
    with open("data/jobs_filtered.json") as f:
        jobs = json.load(f)
    
    for j in jobs:
        st.subheader(j["title"])
        st.write(f"**Company:** {j['company']}")
        st.write(j["reason"])
    
        st.markdown(f"[View Job Posting]({j['url']})")





