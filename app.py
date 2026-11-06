import streamlit as st
from thermiq_footer import render_footer

st.set_page_config(
    page_title="ThermIQ",
    page_icon="🌿",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background: #F7F8F4;
        color: #203431;
    }

    header[data-testid="stHeader"] {
        background: #DDF1EC;
    }

    header[data-testid="stHeader"] button,
    header[data-testid="stHeader"] [data-testid="stToolbar"] button,
    header[data-testid="stHeader"] [data-testid="stToolbar"] svg {
        color: #203431 !important;
        fill: #203431 !important;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 2rem;
        padding-bottom: 4rem;
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

    .hero {
        background: linear-gradient(135deg, #E4F1EA, #F1F5E9);
        border: 1px solid #D6E5DA;
        border-radius: 24px;
        padding: 3rem;
        margin-top: 1rem;
    }

    .eyebrow {
        color: #4C7967;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .hero h1 {
        color: #203431;
        font-size: 3.2rem;
        margin: 0.5rem 0;
    }

    .hero p {
        color: #526760;
        font-size: 1.15rem;
        max-width: 650px;
        line-height: 1.7;
    }

    .tag {
        display: inline-block;
        background: #DCEBE1;
        color: #386654;
        border-radius: 999px;
        padding: 0.45rem 0.85rem;
        font-size: 0.9rem;
        margin-top: 1rem;
    }

    [data-testid="stButton"] {
        display: flex;
        justify-content: center;
    }

    [data-testid="stButton"] button[kind="primary"] {
        width: 260px;
        min-height: 3.2rem;
        background: #386F65 !important;
        color: white !important;
        border: 0 !important;
        border-radius: 999px !important;
        font-weight: 700;
        box-shadow: 0 8px 20px rgba(32, 52, 49, 0.16);
        transition: 0.2s ease;
    }

    [data-testid="stButton"] button[kind="primary"]:hover {
        background: #2F5E56 !important;
        color: white !important;
        transform: translateY(-2px);
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
        st.markdown('<a href="#from-school-details-to-practical-options">How it works</a>', unsafe_allow_html=True)
    with nav_research:
        st.page_link("pages/3_Research_Approach.py", label="Research")
    with nav_assessment:
        st.page_link("pages/1_Heat_Assessment.py", label="Heat assessment")
    with nav_ideas:
        st.page_link("pages/2_Cooling_Ideas.py", label="Cooling ideas")

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">School heat, understood</div>
        <h1>ThermIQ</h1>
        <p>
            A thoughtful starting point for schools exploring classroom heat
            and practical ways to create more comfortable learning spaces.
        </p>
        <span class="tag">Early-stage decision-support project</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
left, middle, right = st.columns([1, 2, 1])
with middle:
    if st.button(
        "🌡️  Start a heat assessment",
        type="primary",
        use_container_width=True,
    ):
        st.switch_page("pages/1_Heat_Assessment.py")

st.write("")
st.markdown(
    """
    <style>
    @keyframes thermiq-scroll {
        from { transform: translateX(0); }
        to { transform: translateX(-50%); }
    }

    .thermiq-strip {
        overflow: hidden;
        background: #DDF1EC;
        border-radius: 14px;
        margin: 0.5rem 0 1.5rem;
        padding: 0.75rem 0;
    }

    .thermiq-strip-track {
        display: flex;
        width: max-content;
        animation: thermiq-scroll 28s linear infinite;
    }

    .thermiq-strip-text {
        color: #315F58;
        font-size: 0.82rem;
        font-weight: 650;
        letter-spacing: 0.08em;
        white-space: nowrap;
        padding-right: 2rem;
    }

    @media (prefers-reduced-motion: reduce) {
        .thermiq-strip-track { animation: none; }
    }
    </style>

    <div class="thermiq-strip">
        <div class="thermiq-strip-track">
            <span class="thermiq-strip-text">
                SCHOOL HEAT, UNDERSTOOD&nbsp; · &nbsp;
                BUILDING-SPECIFIC INSIGHTS&nbsp; · &nbsp;
                PRACTICAL COOLING OPTIONS&nbsp; · &nbsp;
            </span>
            <span class="thermiq-strip-text" aria-hidden="true">
                SCHOOL HEAT, UNDERSTOOD&nbsp; · &nbsp;
                BUILDING-SPECIFIC INSIGHTS&nbsp; · &nbsp;
                PRACTICAL COOLING OPTIONS&nbsp; · &nbsp;
            </span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.components.v1.html(
    """
    <style>
    .thermiq-gallery {
        display: flex;
        gap: 1rem;
        overflow-x: auto;
        padding: 0.4rem 0 1rem;
        scroll-snap-type: x mandatory;
    }

    .thermiq-photo {
        flex: 0 0 100%;
        overflow: hidden;
        background: white;
        border: 1px solid #DCE7DF;
        border-radius: 18px;
        scroll-snap-align: start;
    }

    .thermiq-photo img {
        transition: transform 0.4s ease;
        display: block;
        width: 100%;
        height: 300px;
        object-fit: cover;
    }

    .thermiq-photo:hover img {
        transform: scale(1.04);
    }

    .thermiq-photo p {
        margin: 0;
        padding: 0.85rem 1rem 1rem;
        color: #315F58;
        font-size: 0.8rem;
        font-weight: 600;
    }

    .thermiq-gallery::-webkit-scrollbar {
        height: 8px;
    }

    .thermiq-gallery::-webkit-scrollbar-thumb {
        background: #A9CEC3;
        border-radius: 10px;
    }
    </style>

    <div class="thermiq-gallery">
        <div class="thermiq-photo">
            <img
                src="https://images.unsplash.com/photo-1685159375749-04060db8cefb?auto=format&fit=crop&w=800&q=80"
                alt="Sunlight falling across an empty classroom"
            >
            <p>Classrooms &amp; daylight</p>
        </div>

        <div class="thermiq-photo">
            <img
                src="https://images.unsplash.com/photo-1668172242181-6916ecc4db27?auto=format&fit=crop&w=800&q=80"
                alt="A school courtyard with trees"
            >
            <p>Shade &amp; outdoor spaces</p>
        </div>

        <div class="thermiq-photo">
            <img
                src="https://images.unsplash.com/photo-1760259904989-3c9b99ad49d8?auto=format&fit=crop&w=800&q=80"
                alt="School buildings and grounds"
            >
            <p>School environments</p>
        </div>
    </div>
    """,
    height=370,
    scrolling=False,
)

st.subheader("A cooler classroom starts with the right questions.")
st.write(
    "ThermIQ is being developed to help schools understand building-specific "
    "heat factors and explore possible cooling options."
)

st.write("")
st.markdown("### From school details to practical options")

col1, col2, col3 = st.columns(3)
cards = [
    (
        col1,
        "🏫",
        "01 · DESCRIBE",
        "Tell us about the building",
        "Roof, windows, shade, ventilation, and existing cooling.",
    ),
    (
        col2,
        "🌡️",
        "02 · EXPLORE",
        "See possible heat factors",
        "Bring building details together with local climate information.",
    ),
    (
        col3,
        "🌿",
        "03 · COMPARE",
        "Consider cooling options",
        "Explore ideas by suitability, estimated cost, and feasibility.",
    ),
]

for column, icon, label, title, description in cards:
    with column:
        st.markdown(
            f"""
            <div style="
                background: white;
                border: 1px solid #DCE7DF;
                border-radius: 18px;
                padding: 1.4rem;
                min-height: 210px;
                box-shadow: 0 8px 24px rgba(32, 52, 49, 0.05);
            ">
                <div style="font-size: 1.8rem;">{icon}</div>
                <div style="
                    color: #4C7967;
                    font-size: 0.72rem;
                    font-weight: 700;
                    letter-spacing: 0.1em;
                    margin: 0.8rem 0 0.4rem;
                ">{label}</div>
                <div style="
                    color: #203431;
                    font-size: 1.1rem;
                    font-weight: 700;
                    margin-bottom: 0.5rem;
                ">{title}</div>
                <div style="
                    color: #60716B;
                    font-size: 0.92rem;
                    line-height: 1.5;
                ">{description}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")
st.markdown("## Designed around real school experiences")
st.write(
    "ThermIQ’s early research includes a survey of 120 students about classroom "
    "temperatures and access to cooling, along with interviews with school "
    "administrators about school conditions."
)

left, right = st.columns(2)

with left:
    st.markdown("### 🎒 Student perspectives")
    st.write(
        "Students experience classroom conditions firsthand. Their responses "
        "help keep the project focused on the people heat affects during the school day."
    )

with right:
    st.markdown("### 🏫 School realities")
    st.write(
        "Administrator interviews help the project consider building conditions "
        "and practical constraints schools may face."
    )

st.caption(
    "ThermIQ is an early-stage decision-support project. Its recommendations "
    "will need further research and review."
)

st.markdown("---")
st.markdown("## Cooling ideas")

ideas = [
    ("☀️", "Cool roofs", "#EAF4F0"),
    ("🪟", "Window shade", "#EEF0FA"),
    ("🌬️", "Airflow", "#F7F0E5"),
    ("🌳", "Green shade", "#E8F3E6"),
]

columns = st.columns(4)

for column, (icon, label, color) in zip(columns, ideas):
    with column:
        st.markdown(
            f"""
            <div style="
                background: {color};
                min-height: 145px;
                border-radius: 20px;
                padding: 1.2rem;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            ">
                <div style="font-size: 2.2rem;">{icon}</div>
                <div style="
                    color: #203431;
                    font-weight: 700;
                    font-size: 1rem;
                ">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

render_footer()
