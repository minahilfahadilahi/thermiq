import streamlit as st
from thermiq_footer import render_footer

st.set_page_config(
    page_title="ThermIQ | Cooling ideas",
    page_icon="🌿",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp,
    [data-testid="stAppViewContainer"] {
        background: #DCEDE7 !important;
        color: #203431;
    }

    header[data-testid="stHeader"] {
        background: #DCEDE7;
    }

    .block-container {
        max-width: 1050px;
        padding: 2.2rem 1.3rem 4rem;
    }

    .st-key-thermiq_nav {
        background: #FFFFFF;
        border-radius: 18px;
        padding: 0.75rem 1.15rem;
        margin-top: 1.25rem;
        box-shadow: 0 6px 18px rgba(32, 52, 49, 0.06);
    }

    .st-key-thermiq_nav [data-testid="stPageLink"] a,
    .st-key-thermiq_nav a {
        color: #203431 !important;
        text-decoration: none !important;
        font-family: "Source Sans 3", sans-serif !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        line-height: 1.25 !important;
        border-radius: 999px;
        padding: 0.35rem 0.55rem;
        transition: background-color 0.18s ease, color 0.18s ease;
    }

    .st-key-thermiq_nav a *,
    .st-key-thermiq_nav [data-testid="stMarkdownContainer"] p {
        font-family: "Source Sans 3", sans-serif !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        line-height: 1.25 !important;
        margin: 0 !important;
    }

    .st-key-thermiq_nav [data-testid="stPageLink"] a,
    .st-key-thermiq_nav [data-testid="stPageLink"] a * {
        color: #000000 !important;
    }

    .st-key-thermiq_nav [data-testid="stPageLink"] a:hover,
    .st-key-thermiq_nav a:hover {
        color: #386F65 !important;
        background: #DDF1EC;
    }

    .st-key-cooling_panel {
        background: #FFFFFF !important;
        border: 1px solid #C8DED4;
        border-radius: 26px;
        padding: 2rem 2.2rem;
        margin-top: 1.1rem;
        box-shadow: 0 16px 42px rgba(32, 52, 49, 0.10);
    }

    .st-key-cooling_note [data-testid="stAlert"] {
        background: #386F65 !important;
        border: 1px solid #386F65 !important;
        border-radius: 14px;
    }

    .st-key-cooling_note [data-testid="stAlert"] * {
        color: #FFFFFF !important;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1rem 0.75rem 3rem;
        }

        .st-key-cooling_panel {
            padding: 1.25rem 1rem;
            border-radius: 20px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container(key="thermiq_nav"):
    nav_brand, nav_how, nav_research, nav_assessment, nav_ideas = st.columns(
        [1.8, 1.2, 0.85, 1.25, 1.2]
    )
    with nav_brand:
        st.page_link("app.py", label="🌿  ThermIQ")
    with nav_how:
        st.markdown('<a href="/#from-school-details-to-practical-options">How it works</a>', unsafe_allow_html=True)
    with nav_research:
        st.page_link("pages/3_Research_Approach.py", label="Research")
    with nav_assessment:
        st.page_link("pages/1_Heat_Assessment.py", label="Heat assessment")
    with nav_ideas:
        st.markdown("**Cooling ideas**")

with st.container(key="cooling_panel"):
    st.caption("THERMIQ  ·  OPTIONS TO EXPLORE")
    st.title("Cooling ideas for schools")
    st.write(
        "These are starting points for discussion. The right fit depends on the "
        "building, school priorities, and local conditions."
    )

    options = [
        (
            "☀️",
            "Reflective roof surfaces",
            "The U.S. Department of Energy describes reflective roof surfaces as one way to reflect more sunlight. Pakistan’s NEECA building code also covers cool roofs and notes that assessment depends on location and building design.",
            "Check roof material, color, insulation, condition, access, glare, and seasonal needs.",
            "U.S. Department of Energy: cool roofs",
            "https://www.energy.gov/sites/prod/files/guide_to_cool_roofs.pdf",
        ),
        (
            "🪟",
            "Window shading",
            "Exterior overhangs and sunscreens are options for managing sun through windows; shading also needs to preserve useful daylight.",
            "Check window direction, time of sun, daylight needs, ventilation, and installation constraints.",
            "U.S. Department of Energy: windows and shading",
            "https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-windows-doors-and-skylights",
        ),
        (
            "🌬️",
            "Ventilation and air movement",
            "CDC school guidance covers safe window use, fans, and ventilation systems. It addresses ventilation and air quality, not classroom cooling outcomes.",
            "Check outdoor conditions, safe window operation, room airflow, system maintenance, and school requirements.",
            "CDC: ventilation in schools",
            "https://www.cdc.gov/niosh/ventilation/guidelines/",
        ),
        (
            "🌳",
            "Outdoor shade and vegetation",
            "The U.S. EPA describes trees and vegetation as ways to shade surfaces and affect local heat. Results depend on site conditions.",
            "Check available space, water, utilities, maintenance, access, and school approval.",
            "U.S. EPA: trees and vegetation",
            "https://www.epa.gov/heatislands/benefits-trees-and-vegetation",
        ),
    ]

    card_columns = st.columns(2)
    for index, (icon, title, evidence, checks, source_label, source_url) in enumerate(options):
        with card_columns[index % 2]:
            extra_source = ""
            if title == "Reflective roof surfaces":
                extra_source = (
                    '<br><a href="https://neeca.gov.pk/SiteImage/Downloads/ecbc23.pdf" '
                    'target="_blank" rel="noopener noreferrer" '
                    'style="display:inline-block;margin-top:.45rem;color:#386F65;font-size:.78rem;font-weight:700;text-decoration:none;">'
                    "NEECA Pakistan: Energy Conservation Building Code 2023 ↗</a>"
                )
            st.markdown(
                f"""
                <div style="
                    min-height: 275px;
                    margin-bottom: 1rem;
                    padding: 1.25rem;
                    background: #F1F7F4;
                    border: 1px solid #DCEBE1;
                    border-radius: 18px;
                ">
                    <div style="font-size:1.7rem;margin-bottom:.45rem;">{icon}</div>
                    <div style="font-size:1.05rem;font-weight:700;color:#203431;margin-bottom:.5rem;">{title}</div>
                    <div style="font-size:.9rem;color:#526760;line-height:1.5;">{evidence}</div>
                    <div style="font-size:.85rem;color:#526760;line-height:1.5;margin-top:.7rem;"><strong>What to check:</strong> {checks}</div>
                    <div style="font-size:.78rem;color:#54766B;margin-top:.7rem;">Cost, feasibility, and benefits: not estimated for this school</div>
                    <a href="{source_url}" target="_blank" rel="noopener noreferrer" style="display:inline-block;margin-top:.6rem;color:#386F65;font-size:.78rem;font-weight:700;text-decoration:none;">Source: {source_label} ↗</a>
                    {extra_source}
                </div>
                """,
                unsafe_allow_html=True,
            )

    with st.container(key="cooling_note"):
        st.info(
            "These options are not ranked recommendations. Compare them with school "
            "facilities staff and local evidence; ThermIQ has not estimated costs, "
            "feasibility, or cooling outcomes."
        )

render_footer()
