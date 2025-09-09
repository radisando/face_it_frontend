import streamlit as st
from theme import apply_theme


apply_theme()


st.set_page_config(page_title="About Us", page_icon="👥", layout="wide")


st.title("👥 Meet the Team")
st.write("We’re a small group of builders exploring what’s next in AI.")

# --- Example team data (edit to yours) ---
TEAM = [
    {
        "name": "Dipali Ahirrao",
        "role": "Team",
        "bio": "Experienced software tester transitioning into data science. Passionate about data analysis and currently upskilling to pursue a career as a data analyst or data scientist.",
        "photo": "https://picsum.photos/seed/hannah/300/300",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/hannahkiesow/",
            "Email": "mailto:hannahkiesow@gmail.com"
        }
    },
    {
        "name": "Simon Tilman Finzel",
        "role": "team",
        "bio": "I began my career with an apprenticeship as an electrician and later earned a Master’s degree in Architecture. Most recently, I worked as a Data Operations Specialist, where I developed a strong interest in data-driven solutions. I’m now focused on deepening my skills in Data Science and Machine Learning to bridge my technical background with analytical and AI-powered approaches to problem-solving.",
        "photo": "https://picsum.photos/seed/alex/300/300",
        "links": {
            "GitHub": "https://github.com/",
            "Twitter": "https://twitter.com/"
        }
    },
    {
        "name": "Rafael Sandoval",
        "role": "team",
        "bio": "Bom dia! 👋 I’m Rafa, a visual analytics professional based in Germany. Overall I turn complex data - and sometimes boring - into useful insights; with reporting, dashboards, or data-driven storytelling. Looking for a Data & AI roles within Germany.",
        "photo": "https://picsum.photos/seed/maya/300/300",
        "links": {
            "Portfolio": "https://example.com",
            "Dribbble": "https://dribbble.com/"
        }
    },
    {
        "name": "Anna Sporre",
        "role": "team",
        "bio": "My name is Anna, I'm from Sweden. I've been living in France for more than 5 years, starting my life in Paris during Covid and later moved down to the southwest, been living in Biarritz for 3,5 years where I spend my free time surfing, hiking, climbing and enjoying culture and food in France or a quick trip to Spain for some tapas in San Sebastian. I'm currently working as a senior insight analyst, mostly working with social listening. I've been working in various consumer insights role for over 8 years and now I'm looking to develop my skills in data science to access more technical roles within data analytics and data science.",
        "photo": "https://picsum.photos/seed/alex/300/300",
        "links": {
            "GitHub": "https://github.com/",
            "Twitter": "https://twitter.com/"
        }
    },
    {
        "name": "Hannah Kiesow-Berger",
        "role": "team",
        "bio": "I was previously a computational neuroscientist, but I want to refresh and learn more coding. After completion of the Le Wagon bootcamp, I plan to look for a job in data science, with a focus in health and well-being. :)",
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
st.page_link("app.py", label="Back to the home page")
