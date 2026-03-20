import streamlit as st
from pages.dashboard import show


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Firmbase",
    page_icon="📊",
    layout="wide"
)


# -----------------------------
# APP ENTRY
# -----------------------------
def main():
    show()


if __name__ == "__main__":
    main()
