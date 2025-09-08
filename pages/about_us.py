import streamlit as st
from theme import apply_theme


apply_theme()


st.set_page_config(page_title="About Us", page_icon="👥", layout="wide")


st.title("👥 Meet the Team")
st.write("We’re a small group of builders exploring what’s next in AI.")

# --- Example team data (edit to yours) ---
TEAM = [
    {
        "name": "Hannah Kiesow-Berger",
        "role": "Computational Neuroscientist",
        "bio": "Bridging psychology and machine learning to build useful, human-centered AI products.",
        "photo": "https://picsum.photos/seed/hannah/300/300",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/hannahkiesow/",
            "Email": "mailto:hannahkiesow@gmail.com"
        }
    },
    {
        "name": "Dipali",
        "role": "ML Engineer",
        "bio": "Loves MLOps, reproducible research, and squeezing latency from models.",
        "photo": "https://picsum.photos/seed/alex/300/300",
        "links": {
            "GitHub": "https://github.com/",
            "Twitter": "https://twitter.com/"
        }
    },
    {
        "name": "Rafa",
        "role": "Product Designer",
        "bio": "Designing delightful, accessible interfaces with a bias for clarity.",
        "photo": "https://picsum.photos/seed/maya/300/300",
        "links": {
            "Portfolio": "https://example.com",
            "Dribbble": "https://dribbble.com/"
        }
    },
    {
        "name": "Dipali",
        "role": "ML Engineer",
        "bio": "Loves MLOps, reproducible research, and squeezing latency from models.",
        "photo": "https://picsum.photos/seed/alex/300/300",
        "links": {
            "GitHub": "https://github.com/",
            "Twitter": "https://twitter.com/"
        }
    },
    {
        "name": "Rafa",
        "role": "Product Designer",
        "bio": "Designing delightful, accessible interfaces with a bias for clarity.",
        "photo": "https://picsum.photos/seed/maya/300/300",
        "links": {
            "Portfolio": "https://example.com",
            "Dribbble": "https://dribbble.com/"
        }
    },
]

# --- Render as responsive cards ---
cols_per_row = 3
for i in range(0, len(TEAM), cols_per_row):
    row = TEAM[i:i+cols_per_row]
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            st.markdown('<div class="team-card">', unsafe_allow_html=True)
            st.image(member["photo"], use_container_width=True)
            st.subheader(member["name"])
            st.markdown(f"<div class='team-role'>{member['role']}</div>", unsafe_allow_html=True)
            st.write(member["bio"])
            # links
            link_md = " ".join([f"[{label}]({url})" for label, url in member["links"].items()])
            st.markdown(f"<div class='team-links'>{link_md}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# Optional back link to Home
st.page_link("app.py", label="⬅️ Back to Home")
