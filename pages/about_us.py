import streamlit as st
from theme import apply_theme
import base64

# Apply your custom theme
apply_theme()

# Page config
st.set_page_config(page_title="About Us", page_icon="👭🏻", layout="wide")

st.title("🌈 Meet the Team")
st.write("We’re a small group of builders exploring what’s next in AI.")

# --- Team Data ---
TEAM = [
    {
        "name": "Hannah Kiesow-Berger",
        "role": "Team Leader",
        "bio": "Hi, I'm Hannah! My background is in neuroscience and psychology, and I love using AI and analytics to make sense of complex data and turn it into something useful. I’m especially excited about projects that combine tech with a human touch, and I’m always up for learning and collaborating with others.",
        "photo": "media/TeamPics/hannah.png",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/hannahkiesow/",
            "GitHub": "https://github.com/hannahkiesow"
        }
    },
    {
        "name": "Simon Tilman Finzel",
        "role": "Team Member",
        "bio": "I began my career with an apprenticeship as an electrician and later earned a Master’s degree in Architecture. Most recently, I worked as a Data Operations Specialist, where I developed a strong interest in data-driven solutions. I’m now focused on deepening my skills in Data Science and Machine Learning to bridge my technical background with analytical and AI-powered approaches to problem-solving.",
        "photo": "media/TeamPics/simon.png",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/simon-finzel/",
            "GitHub": "https://github.com/4t4r4xi448"
        }
    },
    {
    "name": "Anna Sporre",
    "role": "Team Member",
    "bio": "I've been living in France for over 5 years, currently working as a senior insight analyst. I have 8+ years experience in consumer insights and now want to develop my skills in data science for more technical roles.",
    "photo": "media/TeamPics/anna.png",
    "links": {
        "LinkedIn": "https://www.linkedin.com/in/annasporre/",
        "GitHub": "https://github.com/anniquitita"
    }
    },
    {
        "name": "Rafael Sandoval",
        "role": "Team Member",
        "bio": "Bom dia! 👋 I’m Rafa, a visual analytics professional based in Germany. I turn complex data into useful insights with reporting, dashboards, or data-driven storytelling. Looking for a Data & AI role within Germany.",
        "photo": "media/TeamPics/rafa.png",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/rafa-sandoval/",
            "GitHub": "https://github.com/radisando"
        }
    },
    {
        "name": "Dipali Ahirrao",
        "role": "Team Member",
        "bio": "Experienced software tester transitioning into data science. Passionate about data analysis and currently upskilling to pursue a career as a data analyst or data scientist.",
        "photo": "media/TeamPics/dipali.png",
        "links": {
            "LinkedIn": "www.linkedin.com/in/dipali-jundre",
            "GitHub": "https://github.com/Deepali15091989"
        }
    },
]

# --- Global CSS styling ---
st.markdown("""
    <style>
    .team-card-container {
        display: flex;
        align-items: center;
        background-color: transparent;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .team-card-container:hover {
        transform: translateY(-5px);
        box-shadow: 4px 4px 15px rgba(0,0,0,0.2);
    }
    .team-photo {
        width: 150px;  /* Adjusted size */
        height: 150px; /* Adjusted size */
        border-radius: 20px;
        object-fit: cover;
        margin-right: 20px;
    }
    .team-content {
        flex-grow: 1;
    }
    .team-role {
        font-size: 0.9rem;
        color: white;
        margin-bottom: 10px;
        font-style: italic;
    }
    .team-name {
    color: white;
    }
    .team-links a {
        margin-right: 10px;
        text-decoration: none;
        font-weight: 500;
        color: #ADD8E6;
    }
    </style>
""", unsafe_allow_html=True)

# --- Render each member as a single HTML card ---


for member in TEAM:
    link_html = ""
    for label, url in member["links"].items():
        if not url.startswith("http"):
            url = "https://" + url

        # Use logos with white background
        if label.lower() == "linkedin":
            icon_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
        else:  # GitHub
            icon_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"

        # Add icon with link
        link_html += f'''
        <a href="{url}" target="_blank" style="margin-right:10px;">
            <img src="{icon_url}" width="20px" height="20px" style="vertical-align:middle; background:white; border-radius:3px; padding:2px;"> {label}
        </a>'''

    # Convert image to base64
    import base64
    def img_to_base64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    img_base64 = img_to_base64(member['photo'])

    card_html = f"""
    <div class="team-card-container" style="text-align:left; flex-direction: row;">
    <img src="data:image/png;base64,{img_base64}" class="team-photo">
        <div class="team-content">
            <h3 class="team-name">{member['name']}</h3>
            <div class='team-role'>{member['role']}</div>
            <p>{member['bio']}</p>
            <div class='team-links'>{link_html}</div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
