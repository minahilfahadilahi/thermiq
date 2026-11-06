import streamlit as st

home = st.Page("app.py", title="Home", icon="🌿")
assessment = st.Page(
    "pages/1_Heat_Assessment.py",
    title="Heat Assessment",
    icon="🌡️",
)
cooling_ideas = st.Page(
    "pages/2_Cooling_Ideas.py",
    title="Cooling Ideas",
    icon="🌿",
)
research = st.Page(
    "pages/3_Research_Approach.py",
    title="Research & Approach",
    icon="📚",
)

page = st.navigation([home, assessment, cooling_ideas, research], position="hidden")
page.run()
