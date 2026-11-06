import json
from collections import defaultdict
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import pandas as pd
import streamlit as st
from thermiq_footer import render_footer

st.set_page_config(
    page_title="ThermIQ | Building survey",
    page_icon="🌡️",
    layout="wide",
)


@st.cache_data(ttl=86400, show_spinner=False)
def load_local_climate_context(location_name):
    """Return a 1991–2020 monthly temperature summary for a place name."""
    geocode_params = urlencode(
        {"name": location_name, "count": 1, "language": "en", "format": "json"}
    )
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?{geocode_params}"

    try:
        request = Request(geocode_url, headers={"User-Agent": "ThermIQ school project"})
        with urlopen(request, timeout=15) as response:
            matches = json.loads(response.read().decode("utf-8")).get("results", [])

        if not matches:
            return {"status": "not_found"}

        place = matches[0]
        climate_params = urlencode(
            {
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "start_date": "1991-01-01",
                "end_date": "2020-12-31",
                "daily": "temperature_2m_max",
                "timezone": "auto",
                "models": "era5_land",
            }
        )
        climate_url = f"https://archive-api.open-meteo.com/v1/archive?{climate_params}"
        request = Request(climate_url, headers={"User-Agent": "ThermIQ school project"})
        with urlopen(request, timeout=25) as response:
            daily_data = json.loads(response.read().decode("utf-8")).get("daily", {})

        monthly_totals = defaultdict(list)
        dates = daily_data.get("time", [])
        temperatures = daily_data.get("temperature_2m_max", [])
        for date, temperature in zip(dates, temperatures):
            if temperature is not None:
                monthly_totals[int(date[5:7])].append(float(temperature))

        if not monthly_totals:
            return {"status": "no_data"}

        label_parts = [place.get("name"), place.get("admin1"), place.get("country")]
        place_label = ", ".join(
            dict.fromkeys(part for part in label_parts if part)
        )
        monthly_averages = {
            month: sum(values) / len(values)
            for month, values in monthly_totals.items()
        }
        return {
            "status": "ok",
            "place": place_label,
            "monthly_averages": monthly_averages,
        }
    except (URLError, TimeoutError, KeyError, ValueError, json.JSONDecodeError):
        return {"status": "unavailable"}

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
        font-family: "Source Sans 3", sans-serif;
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

    .st-key-assessment_panel {
        box-sizing: border-box;
        width: 100%;
        background: #FFFFFF !important;
        border: 1px solid #C8DED4;
        border-radius: 26px;
        padding: 2rem 2.2rem;
        margin-top: 1.1rem;
        box-shadow: 0 16px 42px rgba(32, 52, 49, 0.10);
    }

    h1 {
        color: #203431;
        letter-spacing: -0.035em;
        margin-bottom: 0.35rem;
    }

    [data-testid="stCaptionContainer"] {
        color: #54766B;
    }

    [data-testid="stMarkdownContainer"] p {
        color: #526760;
        line-height: 1.6;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 12px;
        background: #386F65;
        color: #FFFFFF;
        border: 0 !important;
        box-shadow: none !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #DDEBE6 !important;
        opacity: 1;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        border-radius: 12px;
        background: #FBFDFC;
    }

    [data-testid="stMultiSelect"] [data-baseweb="select"] > div {
        border-radius: 12px;
        background: #FBFDFC;
    }

    [data-testid="stTextInput"] input:focus,
    [data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within {
        border-color: #6EAA98;
        box-shadow: 0 0 0 1px #6EAA98;
    }

    [data-testid="stForm"] {
        border: 0;
    }

    [data-testid="stButton"] {
        display: flex;
        justify-content: center;
    }

    [data-testid="stButton"] button[kind="primary"] {
        min-height: 3.2rem;
        padding: 0.2rem 1.5rem;
        border: 0 !important;
        border-radius: 999px !important;
        background: #386F65 !important;
        color: #FFFFFF !important;
        font-weight: 700;
        box-shadow: 0 7px 18px rgba(32, 52, 49, 0.13);
    }

    [data-testid="stFormSubmitButton"] button,
    [data-testid="stFormSubmitButton"] button * {
        color: #FFFFFF !important;
    }

    [data-testid="stDownloadButton"] button,
    [data-testid="stDownloadButton"] button * {
        color: #FFFFFF !important;
    }

    .st-key-thermiq_result_note [data-testid="stAlert"],
    .st-key-thermiq_climate_note [data-testid="stAlert"] {
        background: #386F65 !important;
        border: 1px solid #386F65 !important;
        border-radius: 14px;
    }

    .st-key-thermiq_result_note [data-testid="stAlert"] *,
    .st-key-thermiq_climate_note [data-testid="stAlert"] * {
        color: #FFFFFF !important;
    }

    [data-testid="stButton"] button[kind="primary"]:hover {
        background: #2F5E56 !important;
        transform: translateY(-1px);
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1rem 0.75rem 3rem;
        }

        .st-key-assessment_panel {
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
        st.page_link("pages/2_Cooling_Ideas.py", label="Cooling ideas")

outer_left, survey_column, outer_right = st.columns([1, 5, 1])

with survey_column:
    with st.container(key="assessment_panel"):
        st.caption("🌿  THERMIQ  ·  BUILDING ASSESSMENT")
        st.title("A quick building snapshot")
        st.write(
            "A few details can help us understand your school building. "
            "Answer what you can; “Not sure” is always okay."
        )

        st.markdown("---")

        with st.form("thermiq_building_survey"):
            st.markdown("#### 📍  School & location")
            school_left, school_right = st.columns(2)

            with school_left:
                building_name = st.text_input(
                    "School or building label (optional)",
                    placeholder="e.g. Main campus",
                )

            with school_right:
                location = st.text_input(
                    "City or area",
                    placeholder="Used for future climate context",
                )

            room_left, room_right = st.columns(2)
            with room_left:
                room_label = st.text_input(
                    "Classroom or area being assessed (optional)",
                    placeholder="e.g. Room 12 or upper-floor classroom",
                )
            with room_right:
                warmest_time = st.selectbox(
                    "When does this area usually feel warmest?",
                    [
                        "Not sure",
                        "Morning",
                        "Midday",
                        "Afternoon",
                        "Varies across rooms",
                    ],
                    help="This is based on experience, not a measured temperature.",
                )

            st.caption(
                "When you submit, only the city or area is sent to Open-Meteo to find regional climate data. "
                "The school or building label is not sent."
            )

            st.markdown("#### 🏫  Building conditions")
            roof_col, sun_col = st.columns(2)

            with roof_col:
                roof = st.selectbox(
                    "Roof material",
                    [
                        "Not sure",
                        "Concrete or slab",
                        "Metal sheet",
                        "Tile",
                        "Other",
                    ],
                )

            with sun_col:
                window_sun = st.selectbox(
                    "Direct sun at classroom windows",
                    [
                        "Not sure",
                        "Mostly morning",
                        "Mostly afternoon",
                        "Both morning and afternoon",
                        "Little or no direct sun",
                    ],
                )

            shade_col, ventilation_col = st.columns(2)

            with shade_col:
                window_shade = st.selectbox(
                    "Shade on classroom windows",
                    [
                        "Not sure",
                        "No shade",
                        "Some windows shaded",
                        "Most windows shaded",
                    ],
                )

            with ventilation_col:
                ventilation = st.selectbox(
                    "Ventilation",
                    [
                        "Not sure",
                        "Openable windows",
                        "Fans",
                        "Mechanical ventilation or exhaust",
                        "Limited or no ventilation",
                    ],
                )

            outdoor_shade = st.selectbox(
                "Shade in outdoor areas near classrooms",
                [
                    "Not sure",
                    "Little or no shade",
                    "Some shaded areas",
                    "Most areas shaded",
                ],
            )

            cooling = st.selectbox(
                "Existing cooling system",
                [
                    "Not sure",
                    "None",
                    "Fans",
                    "Air conditioning",
                    "Evaporative cooling",
                    "Combination of systems",
                ],
            )

            constraints = st.multiselect(
                "School considerations to check (optional)",
                [
                    "Budget constraints",
                    "Approval or permissions",
                    "Maintenance capacity",
                    "Limited outdoor space",
                    "Work timing or disruption",
                    "Not sure",
                ],
                placeholder="Choose any that may apply",
                help="These answers help guide discussion; they do not determine feasibility.",
            )

            submitted = st.form_submit_button(
                "Review my building details",
                type="primary",
                use_container_width=True,
            )

        st.caption(
            "Your answers create an exploratory summary in this session. "
            "This prototype does not calculate a validated risk score or predict temperatures."
        )

        if submitted:
            st.divider()
            st.markdown("### Your building snapshot")
            result_left, result_right = st.columns(2)

            with result_left:
                st.markdown(f"**School / building:** {building_name or 'Not provided'}")
                st.markdown(f"**Room / area:** {room_label or 'Not provided'}")
                st.markdown(f"**City / area:** {location or 'Not provided'}")
                st.markdown(f"**Roof:** {roof}")
                st.markdown(f"**Window sun:** {window_sun}")

            with result_right:
                st.markdown(f"**Window shade:** {window_shade}")
                st.markdown(f"**Ventilation:** {ventilation}")
                st.markdown(f"**Outdoor shade:** {outdoor_shade}")
                st.markdown(f"**Existing cooling:** {cooling}")
                st.markdown(f"**Warmest time reported:** {warmest_time}")

            if constraints:
                st.markdown(
                    "**Possible school considerations:** " + ", ".join(constraints)
                )

            observations = []
            option_cards = []

            if window_sun in ("Mostly morning", "Mostly afternoon", "Both morning and afternoon"):
                observations.append(
                    "You reported direct sun at the classroom windows. It may help to note which rooms get sun and at what time."
                )
            if warmest_time in ("Morning", "Midday", "Afternoon"):
                observations.append(
                    f"You reported that this area usually feels warmest in the {warmest_time.lower()}. This is an experience-based note, not a temperature measurement."
                )
            elif warmest_time == "Varies across rooms":
                observations.append(
                    "You reported that the warmest time varies across rooms. Compare areas separately when gathering follow-up observations."
                )
            if window_shade in ("No shade", "Some windows shaded"):
                observations.append(
                    "You reported that some or all classroom windows have little shade. Check which windows are exposed and what shading is already possible."
                )
                option_cards.append(
                    (
                        "🪟 Window shading",
                        "DOE describes exterior shading as an option for managing sun through windows; shade can also affect daylight.",
                        "Check room orientation, daylight needs, window use, and installation constraints.",
                        "U.S. Department of Energy: windows and shading",
                        "https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-windows-doors-and-skylights",
                    )
                )
            elif window_sun in ("Mostly morning", "Mostly afternoon", "Both morning and afternoon"):
                option_cards.append(
                    (
                        "🪟 Window shading",
                        "DOE describes exterior shading as an option for managing sun through windows; shade can also affect daylight.",
                        "Check room orientation, daylight needs, window use, and installation constraints.",
                        "U.S. Department of Energy: windows and shading",
                        "https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-windows-doors-and-skylights",
                    )
                )
            if roof != "Not sure":
                observations.append(
                    f"You reported a {roof.lower()} roof. Material alone is not enough to estimate indoor heat; roof color, insulation, and condition would also need review."
                )
                option_cards.append(
                    (
                        "☀️ Roof options",
                        "DOE’s cool-roof guide describes reflective roof surfaces as one option; fit depends on the existing roof and climate.",
                        "Confirm roof color, insulation, condition, access, and any school or building requirements.",
                        "U.S. Department of Energy: cool roofs",
                        "https://www.energy.gov/sites/prod/files/guide_to_cool_roofs.pdf",
                    )
                )
            if ventilation == "Limited or no ventilation":
                observations.append(
                    "You reported limited or no ventilation. Check how air moves through the rooms and what changes are safe and practical for the school."
                )
                option_cards.append(
                    (
                        "🌬️ Air movement",
                        "CDC school guidance covers safe window use, fans, and ventilation systems; it does not forecast classroom cooling.",
                        "Review possible changes with school facilities staff and check safety, room airflow, and maintenance.",
                        "CDC: ventilation in schools",
                        "https://www.cdc.gov/niosh/ventilation/guidelines/",
                    )
                )
            elif ventilation in ("Openable windows", "Fans", "Mechanical ventilation or exhaust"):
                observations.append(
                    f"You reported {ventilation.lower()} for ventilation. A follow-up could check when it is used and whether it reaches the classrooms being considered."
                )
                option_cards.append(
                    (
                        "🌬️ Air movement",
                        "CDC school guidance covers safe window use, fans, and ventilation systems; it does not forecast classroom cooling.",
                        "Check current system use, room airflow, maintenance, and school constraints.",
                        "CDC: ventilation in schools",
                        "https://www.cdc.gov/niosh/ventilation/guidelines/",
                    )
                )

            if outdoor_shade in ("Little or no shade", "Some shaded areas"):
                observations.append(
                    f"You reported {outdoor_shade.lower()} in outdoor areas near classrooms. Check which areas are used and what space or site limits apply."
                )
                option_cards.append(
                    (
                        "🌳 Outdoor shade & planting",
                        "EPA describes trees and vegetation as ways to shade surfaces and affect local heat; effects depend on the site.",
                        "Check available space, water, maintenance, utilities, and school approval before exploring options.",
                        "U.S. EPA: trees and vegetation",
                        "https://www.epa.gov/heatislands/benefits-trees-and-vegetation",
                    )
                )

            if cooling == "None":
                observations.append(
                    "You reported no existing cooling system. Document the rooms and times of concern before comparing possible options."
                )

            st.markdown("#### What may be useful to check")
            if observations:
                for observation in observations:
                    st.markdown(f"- {observation}")
            else:
                st.write(
                    "There isn’t enough detail yet to highlight a specific follow-up. "
                    "You can update any “Not sure” answers after checking with school staff."
                )

            st.markdown("#### Cooling ideas to investigate")
            if option_cards:
                idea_columns = st.columns(2)
                for index, (title, evidence, checks, source_label, source_url) in enumerate(option_cards):
                    with idea_columns[index % 2]:
                        st.markdown(
                            f"""
                            <div style="
                                min-height: 205px;
                                margin-bottom: 0.8rem;
                                padding: 1rem 1.1rem;
                                background: #F1F7F4;
                                border: 1px solid #DCEBE1;
                                border-radius: 16px;
                            ">
                                <div style="font-weight:700;color:#203431;margin-bottom:.45rem;">{title}</div>
                                <div style="font-size:.9rem;color:#526760;line-height:1.5;">{evidence}</div>
                                <div style="font-size:.84rem;color:#526760;line-height:1.5;margin-top:.5rem;"><strong>Check:</strong> {checks}</div>
                                <div style="font-size:.76rem;color:#54766B;margin-top:.7rem;">Cost &amp; suitability: not assessed yet</div>
                                <a href="{source_url}" target="_blank" rel="noopener noreferrer" style="display:inline-block;margin-top:.55rem;color:#386F65;font-size:.78rem;font-weight:700;text-decoration:none;">Source: {source_label} ↗</a>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
            else:
                st.write(
                    "No specific option is suggested from these answers alone. "
                    "A fuller building review would help identify what is practical."
                )

            with st.container(key="thermiq_result_note"):
                st.info(
                    "These are exploratory follow-up topics, not a heat-risk rating or "
                    "a prediction of cooling outcomes. Costs, feasibility, and benefits "
                    "have not been estimated."
                )

            st.markdown("#### Regional climate context")
            climate_context = None
            if location.strip():
                with st.spinner("Looking up regional historical temperatures…"):
                    climate_context = load_local_climate_context(location.strip())

                if climate_context["status"] == "ok":
                    month_labels = [
                        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
                    ]
                    monthly_averages = climate_context["monthly_averages"]
                    chart_data = pd.DataFrame(
                        {
                            "Average daily high (°C)": [
                                round(monthly_averages[month], 1)
                                if month in monthly_averages
                                else None
                                for month in range(1, 13)
                            ]
                        },
                        index=month_labels,
                    )
                    st.write(f"**Matched location:** {climate_context['place']}")
                    st.bar_chart(chart_data)
                    st.caption(
                        "Average of daily outdoor maximum temperatures for 1991–2020. "
                        "This regional grid estimate is not a school measurement or an indoor temperature. "
                        "Source: [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), ERA5-Land."
                    )
                    st.caption(
                        "If the matched location is not right, add its region or country to the city/area field and submit again."
                    )
                elif climate_context["status"] == "not_found":
                    st.info(
                        "I couldn’t match that city or area. Add a region or country to the field and submit again."
                    )
                else:
                    with st.container(key="thermiq_climate_note"):
                        st.info(
                            "Regional climate context is unavailable right now. Your building summary is still ready."
                        )
            else:
                st.caption("Add a city or area to include regional climate context.")

            report_lines = [
                "ThermIQ — Exploratory Building Snapshot",
                "",
                f"School / building: {building_name or 'Not provided'}",
                f"Room / area: {room_label or 'Not provided'}",
                f"City / area: {location or 'Not provided'}",
                f"Roof: {roof}",
                f"Direct sun at windows: {window_sun}",
                f"Window shade: {window_shade}",
                f"Ventilation: {ventilation}",
                f"Outdoor shade: {outdoor_shade}",
                f"Existing cooling: {cooling}",
                f"Warmest time reported: {warmest_time}",
                "Possible school considerations: " + (", ".join(constraints) or "Not provided"),
                "",
                "Follow-up observations:",
            ]
            report_lines.extend(f"- {item}" for item in observations)
            report_lines.extend(["", "Cooling ideas to investigate:"])
            if option_cards:
                for title, evidence, checks, source_label, source_url in option_cards:
                    report_lines.extend(
                        [
                            f"- {title}: {evidence}",
                            f"  Check: {checks}",
                            f"  Source: {source_label} — {source_url}",
                        ]
                    )
            else:
                report_lines.append("- No specific option was suggested from these answers alone.")

            if climate_context and climate_context["status"] == "ok":
                report_lines.extend(
                    [
                        "",
                        f"Regional climate context for {climate_context['place']}:",
                        "Average daily outdoor maximum temperatures by month, 1991–2020 (°C):",
                    ]
                )
                report_lines.extend(
                    f"- {month}: {climate_context['monthly_averages'][month]:.1f}"
                    for month in range(1, 13)
                    if month in climate_context["monthly_averages"]
                )
                report_lines.append(
                    "Source: Open-Meteo Historical Weather API, ERA5-Land; regional grid estimate, not an indoor temperature."
                )

            report_lines.extend(
                [
                    "",
                    "This is an exploratory summary, not a validated heat-risk rating or temperature prediction.",
                    "Costs, feasibility, and benefits have not been estimated.",
                ]
            )
            report_text = "\n".join(report_lines)

            st.markdown("#### Save this snapshot")
            download_left, download_column, download_right = st.columns([1, 2, 1])
            with download_column:
                st.download_button(
                    "⬇️  Download assessment summary",
                    data=report_text,
                    file_name="thermiq_building_snapshot.txt",
                    mime="text/plain",
                    type="primary",
                    use_container_width=True,
                    on_click="ignore",
                )

render_footer()
