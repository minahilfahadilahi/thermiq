import csv
from io import StringIO

import streamlit as st
from thermiq_footer import render_footer

st.set_page_config(
    page_title="ThermIQ | Research & approach",
    page_icon="📚",
    layout="wide",
)


def make_blank_csv(headers):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(headers)
    writer.writerow([""] * len(headers))
    return output.getvalue()

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

    .st-key-research_panel {
        background: #FFFFFF !important;
        border: 1px solid #C8DED4;
        border-radius: 26px;
        padding: 2rem 2.2rem;
        margin-top: 1.1rem;
        box-shadow: 0 16px 42px rgba(32, 52, 49, 0.10);
    }

    .research-card {
        min-height: 185px;
        padding: 1.2rem;
        background: #F1F7F4;
        border: 1px solid #DCEBE1;
        border-radius: 18px;
    }

    .research-label {
        color: #4C7967;
        font-size: 0.74rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    [data-testid="stDownloadButton"] button,
    [data-testid="stDownloadButton"] button * {
        background: #386F65 !important;
        color: #FFFFFF !important;
        border-color: #386F65 !important;
    }

    [data-testid="stDownloadButton"] button:hover {
        background: #2F5E56 !important;
        border-color: #2F5E56 !important;
    }

    .st-key-research_note [data-testid="stAlert"] {
        background: #386F65 !important;
        border: 1px solid #386F65 !important;
        border-radius: 14px;
    }

    .st-key-research_note [data-testid="stAlert"] * {
        color: #FFFFFF !important;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1rem 0.75rem 3rem;
        }

        .st-key-research_panel {
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
        st.markdown("**Research**")
    with nav_assessment:
        st.page_link("pages/1_Heat_Assessment.py", label="Heat assessment")
    with nav_ideas:
        st.page_link("pages/2_Cooling_Ideas.py", label="Cooling ideas")

with st.container(key="research_panel"):
    st.caption("THERMIQ  ·  RESEARCH & APPROACH")
    st.title("How ThermIQ is being developed")
    st.write(
        "ThermIQ brings school experiences, building details, and public sources "
        "together to support early exploration of classroom heat and possible responses."
    )

    st.markdown("### What informs the project")
    input_left, input_right = st.columns(2)
    with input_left:
        st.markdown(
            """
            <div class="research-card">
                <div class="research-label">School experiences</div>
                <p style="color:#203431;font-weight:700;margin:.55rem 0 .35rem;">Student and administrator input</p>
                <p style="color:#526760;line-height:1.5;margin:0;">An initial survey of 120 students explored classroom temperatures and access to cooling, alongside interviews with school administrators. The school helped facilitate student participation and administrator access; research and tool development are conducted independently.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with input_right:
        st.markdown(
            """
            <div class="research-card">
                <div class="research-label">Building details</div>
                <p style="color:#203431;font-weight:700;margin:.55rem 0 .35rem;">A room-by-room snapshot</p>
                <p style="color:#526760;line-height:1.5;margin:0;">The assessment records roof, windows, shade, ventilation, cooling, outdoor conditions, and experience-based timing to identify useful follow-up questions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### How to read the climate chart")
    st.write(
        "When a city or area is entered, ThermIQ shows average daily outdoor "
        "maximum temperatures by month for 1991–2020, using Open-Meteo’s ERA5-Land "
        "historical data. It represents a regional grid estimate, not the school site "
        "or an indoor classroom measurement."
    )

    st.markdown("### Sources and local context")
    st.markdown(
        "- **Pakistan school research:** A 2022 study in Multan examined indoor environmental quality in four public-school classrooms, combining measurements with teacher and student questionnaires. Its findings describe that study’s setting and should not be assumed to represent every school. [Read the study record](https://orbi.uliege.be/handle/2268/289779)."
    )
    st.markdown(
        "- **Pakistan building guidance:** NEECA’s Energy Conservation Building Code 2023 includes guidance on building envelopes, passive design, cool roofs, and HVAC. It is a design reference; it does not assess ThermIQ’s example school. [Read the code](https://neeca.gov.pk/SiteImage/Downloads/ecbc23.pdf)."
    )
    st.markdown(
        "- **Climate data:** Open-Meteo’s historical weather data is based on reanalysis and uses regional grid cells. [Read the API and data notes](https://open-meteo.com/en/docs/historical-weather-api)."
    )
    st.markdown(
        "- **Intervention background:** The Cooling Ideas page links to general guidance from the U.S. Department of Energy, CDC, and EPA. These sources offer background, not Pakistan-specific estimates for this school."
    )

    st.markdown("### Gather Lahore-specific evidence")
    st.write(
        "Use one row per room observation or local quote. Record when and where "
        "information came from so it can be checked later. A temperature reading "
        "is optional—include one only if you have a thermometer and can record its method."
    )
    st.caption(
        "Keep student responses anonymous. Do not enter student names or identifiable health information."
    )

    room_template = make_blank_csv(
        [
            "record_date",
            "non_identifying_site_code",
            "room_or_area_label",
            "observation_time",
            "warmest_time_reported",
            "observation_source_or_method",
            "indoor_air_temperature_c_if_measured",
            "thermometer_type_if_used",
            "direct_sun_at_windows",
            "window_shading",
            "ventilation_windows_or_fans",
            "existing_cooling",
            "outdoor_shade",
            "notes",
        ]
    )
    quote_template = make_blank_csv(
        [
            "quote_date",
            "intervention_type",
            "supplier_or_source_name",
            "source_document_or_url",
            "amount_pkr",
            "what_the_quote_includes",
            "maintenance_or_replacement_costs_if_known",
            "availability_or_lead_time_if_known",
            "school_feasibility_notes",
            "quote_valid_until_if_listed",
            "notes",
        ]
    )

    template_left, template_right = st.columns(2)
    with template_left:
        st.download_button(
            "⬇️  Room observation template",
            data=room_template,
            file_name="thermiq_lahore_room_observations.csv",
            mime="text/csv",
            use_container_width=True,
        )
    with template_right:
        st.download_button(
            "⬇️  Intervention quote template",
            data=quote_template,
            file_name="thermiq_lahore_intervention_quotes.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with st.container(key="research_note"):
        st.info(
            "ThermIQ is an exploratory prototype. It does not provide a validated "
            "heat-risk score, predict indoor temperatures, rank interventions, or "
            "estimate school-specific costs, feasibility, or benefits."
        )

render_footer()
