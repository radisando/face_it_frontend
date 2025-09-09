import os
import io
import requests
import streamlit as st
from PIL import Image
from theme import apply_theme

# ---------- Theme & Page ----------
apply_theme()
st.set_page_config(page_title="Face It", page_icon="🤖", layout="wide")

st.title("Face It: We've Got Feelings")
st.write("Upload an image and let our model guess the emotion.")

# ---------- API URL setup ----------
BASE_URI = os.getenv("CLOUD_API_URI") or st.secrets.get("cloud_api_uri") or "http://localhost:8000"
if not BASE_URI.endswith("/"):
    BASE_URI += "/"
PRED_ENDPOINT = BASE_URI + "predict"

st.caption(f"🔗 Working with API at: {PRED_ENDPOINT}")  # dev only, remove in prod

# ---------- File uploader ----------
uploaded = st.file_uploader("Upload a face image", type=["jpg", "jpeg", "png"])

if uploaded:
    st.image(uploaded, caption="Preview", use_container_width=False)

    if st.button("Identify Emotion!"):
        try:
            # file bytes + content type
            img_bytes = uploaded.getvalue()
            content_type = uploaded.type or "image/jpeg"

            # call the API
            files = {"file": (uploaded.name or "image.jpg", img_bytes, content_type)}
            r = requests.post(PRED_ENDPOINT, files=files, timeout=30)
            r.raise_for_status()

            data = r.json()

            # Your FastAPI returns {label, confidence, probabilities}
            label = data.get("label") or data.get("emotion", "unknown")
            conf = data.get("confidence")
            probs = data.get("probabilities") or data.get("scores") or {}

            # show result
            conf_txt = f" ({conf:.1%})" if isinstance(conf, (int, float)) else ""
            st.success(f"Predicted emotion: **{label}**{conf_txt}")

            # show probabilities as a bar chart if present
            if isinstance(probs, dict) and probs:
                import pandas as pd
                df = pd.Series(probs).sort_values(ascending=False).to_frame("probability")
                st.bar_chart(df)
            else:
                st.json(data)  # fallback: show raw payload

        except requests.exceptions.RequestException as e:
            st.error(f"API call failed: {e}")

st.markdown("Tip: please upload a clear, front-facing picture of a face.")
