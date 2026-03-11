import streamlit as st, json

st.title("🤖 AI Job Finder")
st.write("Automatically matched jobs based on your skills.")

with open("data/jobs_filtered.json") as f:
    jobs = json.load(f)

for j in jobs:
    st.subheader(j["title"])
    st.write(f"**Company:** {j['company']}")
    st.write(j["reason"])
    st.markdown(f"[View Job Posting]({j['url']})")