import os
import streamlit as st
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
st.write("A general look at where artificial intelligence is heading.")
st.button("Click Me")


# Just displaying the source for the API. Remove this in your final version.
st.markdown(f"Working with {url}")

st.markdown("Face it team. Now, the rest is up to you and the team. Start creating your page.")


# TODO: Add some titles, introduction, ...


# TODO: Request user input


# TODO: Call the API using the user's input
#   - url is already defined above
#   - create a params dict based on the user's input
#   - finally call your API using the requests package


# TODO: retrieve the results
#   - add a little check if you got an ok response (status code 200) or something else
#   - retrieve the prediction from the JSON


# TODO: display the prediction in some fancy way to the user


# TODO: [OPTIONAL] maybe you can add some other pages?
#   - some statistical data you collected in graphs
#   - description of your product
#   - a 'Who are we?'-page
