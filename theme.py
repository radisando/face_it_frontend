import streamlit as st


def apply_theme():
    """Inject custom CSS theme into the Streamlit app."""
    st.markdown("""
    <style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #001D7E 0%, #9D4EDD 50%, #FF6EC7 100%);
        color: #FFFFFF;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 29, 126, 0.9);
    }

    /* Sidebar links */
    section[data-testid="stSidebar"] a {
        color: #FFFFFF !important;        /* default white */
        text-decoration: none;
    }
    section[data-testid="stSidebar"] a:hover {
        color: #FF6EC7 !important;        /* pink on hover */
    }

    /* Buttons */
    div.stButton > button {
        background-color: #6C63FF;
        color: white;
        border-radius: 8px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #8A7CFF;
    }

    /* Team cards */
    .team-card {
        padding: 1rem;
        border-radius: 16px;
        background: rgba(255,255,255,0.08);
        text-align: center;
    }
    .team-role { opacity: 0.9; font-size: 0.95rem; }
    .team-links a { color: #FFD6FF; text-decoration: none; margin-right: 0.75rem; }
    .team-links a:hover { color: #FF6EC7; text-decoration: underline; }

    /* Circular images */
    .team-photo img {
        border-radius: 50%;
        width: 160px !important;
        height: 160px !important;
        object-fit: cover;
        margin-bottom: 0.75rem;
        border: 3px solid #FFFFFF33;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)
