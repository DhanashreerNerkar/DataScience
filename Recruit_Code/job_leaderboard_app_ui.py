import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("xgb_predicted_ranking_test.csv")

df = load_data()

# Sidebar: Job Selector
st.sidebar.title("Job Selector")
job_options = df[['Job_ID', 'Job_Title', 'Company']].drop_duplicates()
job_display = job_options.apply(lambda x: f"{x['Job_ID']} - {x['Job_Title']} @ {x['Company']}", axis=1)
selected_job = st.sidebar.selectbox("Select a Job to View Leaderboard", job_display)

# Extract job_id from selected
job_id = int(selected_job.split(" - ")[0])
job_df = df[df['Job_ID'] == job_id].sort_values(by="Predicted_Rank")

# Display header
st.title("Candidate Leaderboard")
st.subheader(f"Job: {job_df['Job_Title'].iloc[0]} @ {job_df['Company'].iloc[0]}")

# Display leaderboard
st.markdown("Top Candidates")
st.dataframe(
    job_df[[
        "Predicted_Rank", "Candidate_Name", 
        "Predicted_Score", 
        "skills_semantic_score", "experience_semantic_score", 
        "project_semantic_score", "education_semantic_score"
    ]].reset_index(drop=True),
    use_container_width=True
)

# Add a visual metric card
top_candidate = job_df.iloc[0]
st.success(f" Top Candidate: **{top_candidate['Candidate_Name']}** with score **{top_candidate['Predicted_Score']:.2f}**")
