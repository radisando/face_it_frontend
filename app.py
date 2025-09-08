import os
import streamlit as st
import io
import requests
from PIL import Image
from theme import apply_theme


apply_theme()

# Define the base URI of the API
#   - Potential sources are in `.streamlit/secrets.toml` or in the Secrets section
#     on Streamlit Cloud
#   - The source selected is based on the shell variable passend when launching streamlit
#     (shortcuts are included in Makefile). By default it takes the cloud API url
if 'API_URI' in os.environ:
    BASE_URI = st.secrets[os.environ.get('API_URI')]
else:
    BASE_URI = st.secrets['cloud_api_uri']
# Add a '/' at the end if it's not there
BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
# Define the url to be used by requests.get to get a prediction (adapt if needed)
url = BASE_URI + 'predict'


import streamlit as st

# Page setup
st.set_page_config(
    page_title="Face It",
    page_icon="🤖",
    layout="wide"
)


st.title("Face It: We've Got Feelings")
#st.write("A general look at where artificial intelligence is heading.")
#st.button("Click Me")


# Just displaying the source for the API. Remove this in your final version.
#st.markdown(f"Working with {url}")

#st.markdown("Face it team. Now, the rest is up to you and the team. Start creating your page.")


# TODO: Add some titles, introduction, ...


# TODO: Request user input


# Configure where to send predictions (FastAPI) — set this in .streamlit/secrets.toml or env
API_URI = st.secrets.get("API_URI", "http://localhost:8000")  # e.g., "https://faceit-api-xxxxx-ew.a.run.app"
PRED_ENDPOINT = f"{API_URI.rstrip('/')}/predict"

# ---------- Uploader ----------
st.title("Upload an Image")
st.write("Choose a face image and let one of our models identify the emotion.")

# API endpoint (replace with your deployed FastAPI later)
url = st.secrets.get("API_URI", "http://localhost:8000/predict")

uploaded = st.file_uploader("Upload a face image", type=["jpg", "jpeg", "png"])

if uploaded:
    st.image(uploaded, caption="Preview", use_container_width=False)

    if st.button("🔍 Identify Emotion"):
        # TODO: Call the API using the user's input
        try:
            # 1️⃣ Prepare params or files based on how your API is designed
            # If API expects query params (GET request style):
            # params = {"filename": uploaded.name}

            # If API expects a file upload (multipart form, common in FastAPI):
            files = {"file": uploaded.getvalue()}  # raw bytes

            # 2️⃣ Make the request
            response = requests.post(url, files=files, timeout=30)
            response.raise_for_status()

            # 3️⃣ Parse JSON response
            data = response.json()
            # e.g. {"emotion": "happy", "scores": {"happy": 0.9, "sad": 0.1}}
            st.success(f"Predicted emotion: **{data.get('emotion', 'unknown')}**")
            st.json(data)

        except requests.exceptions.RequestException as e:
            st.error(f"API call failed: {e}")
st.markdown("Tip: please upload a clear picture of a front-facing face.")



# TODO: Call the API using the user's input
#   - url is already defined above
#   - create a params dict based on the user's input
#   - finally call your API using the requests package


# TODO: retrieve the results
#   - add a little check if you got an ok response (status code 200) or something else
#   - retrieve the prediction from the JSON

st.title("Your results....")


# TODO: display the prediction in some fancy way to the user


# TODO: [OPTIONAL] maybe you can add some other pages?
#   - some statistical data you collected in graphs
#   - description of your product
#   - a 'Who are we?'-page
