import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Firmbase Platform", layout="wide")

st.title("Firmbase Autonomous Strategy Platform")

# -------------------------
# NAVIGATION
# -------------------------
st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Select Module",
    [
        "Master Dashboard",
        "Financial Engine",
        "Risk Engine",
        "Opportunity Engine",
        "Capital Allocation",
        "Market Expansion",
        "Governance",
        "System Check"
    ]
)

# -------------------------
# ROUTING
# -------------------------
if page == "Master Dashboard":
    from pages.dashboard import show
    show()

elif page == "Financial Engine":
    from pages.financial import show
    show()

elif page == "Risk Engine":
    from pages.risk import show
    show()

elif page == "Opportunity Engine":
    from pages.opportunity import show
    show()

elif page == "Capital Allocation":
    from pages.capital import show
    show()

elif page == "Market Expansion":
    from pages.market import show
    show()

elif page == "Governance":
    from pages.governance import show
    show()

elif page == "System Check":
    from pages.system_check import show
    show()
