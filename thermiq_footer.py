import streamlit as st


def render_footer():
    st.markdown(
        """
        <style>
        .st-key-thermiq_footer {
            box-sizing: border-box;
            background: #DDF1EC;
            border: 1px solid #C8DED4;
            border-radius: 18px;
            margin-top: 2.8rem;
            padding: 1.2rem 1.4rem;
        }

        .st-key-thermiq_footer [data-testid="stPageLink"] a,
        .st-key-thermiq_footer [data-testid="stPageLink"] a * {
            color: #386F65 !important;
            font-size: 0.9rem !important;
            font-weight: 700 !important;
            text-decoration: none !important;
        }

        .st-key-thermiq_footer [data-testid="stPageLink"] a:hover {
            color: #203431 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container(key="thermiq_footer"):
        brand_column, links_column = st.columns([1.2, 3.8])
        with brand_column:
            st.markdown("**🌿 ThermIQ**")
            st.caption("Created by Minahil Fahad Ilahi")

        with links_column:
            home, assessment, cooling, research = st.columns(4)
            with home:
                st.page_link("app.py", label="Home")
            with assessment:
                st.page_link("pages/1_Heat_Assessment.py", label="Heat assessment")
            with cooling:
                st.page_link("pages/2_Cooling_Ideas.py", label="Cooling ideas")
            with research:
                st.page_link("pages/3_Research_Approach.py", label="Research")

        st.caption(
            "Exploratory prototype · Not a validated heat-risk score or a school-specific cost estimate."
        )
