import os
import io
import requests
import streamlit as st
from PIL import Image
from theme import apply_theme

# ---------- Theme & Page ----------
apply_theme()
st.set_page_config(page_title="Face It", page_icon="🤖", layout="wide")

st.markdown(
    "<h1 style='text-align: center; font-size: 60px;'>Face It: We've Got Feelings</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align: center;'>😊😢🤢😡😨😲😐🥳😖🫣🤨</h1>",
    unsafe_allow_html=True
)

st.header("👋 Hey there!")
st.write("We trained a slightly over-confident AI that thinks it can read your emotions 😏.")
st.write(" ")

st.header("All you have to do is:")
st.write("📸 Upload a face pic (front-facing, clear photo)")
st.write("👉 Sit back and let our model take its best guess!")

# ---------- API URL setup ----------
BASE_URI = os.getenv("CLOUD_API_URI") or st.secrets.get("cloud_api_uri") or "http://localhost:8000"
if not BASE_URI.endswith("/"):
    BASE_URI += "/"
PRED_ENDPOINT = BASE_URI + "predict"

st.markdown("⚡ Tip: No sunglasses, masks, or ninja disguises 🥷 (our AI is good, but not *that* good...yet). 🤓")
st.write(" ")

# ---------- File uploader + results side by side ----------
col_left, col_right = st.columns([1, 2])  # adjust width ratio

with col_left:
    uploaded = st.file_uploader("Upload here!", type=["jpg", "jpeg", "png"])
    run_prediction = False
    if uploaded:
        st.image(uploaded, caption="Preview", use_container_width=False)
        if st.button("Identify Emotion!"):
            run_prediction = True

with col_right:
    if uploaded and run_prediction:
        # placeholder for spinner + results
        result_placeholder = st.empty()

        with result_placeholder.container():
            with st.spinner("🤖 The AI model is thinking.... please wait!"):
                try:
                    img_bytes = uploaded.getvalue()
                    content_type = uploaded.type or "image/jpeg"

                    # call the API
                    files = {"file": (uploaded.name or "image.jpg", img_bytes, content_type)}
                    r = requests.post(PRED_ENDPOINT, files=files, timeout=30)
                    r.raise_for_status()
                    data = r.json()

                    # FastAPI returns {label, confidence, probabilities}
                    label = data.get("label") or data.get("emotion", "unknown")
                    conf = data.get("confidence")
                    probs = data.get("probabilities") or data.get("scores") or {}

                except requests.exceptions.RequestException as e:
                    st.error(f"API call failed: {e}")
                    data, label, conf, probs = None, None, None, None

        # After spinner finishes → overwrite placeholder with results
        if data:
            # --- Emotion styles ---
            EMOTION_STYLES = {
                "happy":    {"fg": "#FFFFFF", "bg": "#FACC1533"},
                "sad":      {"fg": "#FFFFFF", "bg": "#3B82F633"},
                "angry":    {"fg": "#FFFFFF", "bg": "#EF444433"},
                "fear":     {"fg": "#FFFFFF", "bg": "#8B5CF633"},
                "surprise": {"fg": "#FFFFFF", "bg": "#EC489933"},
                "disgust":  {"fg": "#FFFFFF", "bg": "#10B98133"},
                "neutral":  {"fg": "#FFFFFF", "bg": "#9CA3AF33"},
            }

            conf_txt = f" ({conf:.1%})" if isinstance(conf, (int, float)) else ""
            style = EMOTION_STYLES.get(label.lower(), {"fg": "#FFFFFF", "bg": "#FFFFFF22"})

            badge_html = f"""
            <div style="
                display:flex; align-items:center; justify-content:center;
                margin: 12px 0 4px 0;
            ">
              <span style="
                  background:{style['bg']};
                  color:{style['fg']};
                  padding:12px 18px;
                  border-radius:999px;
                  font-weight:700;
                  font-size:24px;
                  letter-spacing:0.3px;
                  box-shadow: 0 4px 12px rgba(0,0,0,0.25);
                  border:1px solid rgba(255,255,255,0.15);
              ">
                👩🧠🫀 Predicted Emotion: {label}{conf_txt}
              </span>
            </div>
            """
            result_placeholder.markdown(badge_html, unsafe_allow_html=True)

            # --- Show probabilities as bar chart ---
            if isinstance(probs, dict) and probs:
                import pandas as pd
                import matplotlib.pyplot as plt
                import seaborn as sns

                series = pd.Series(probs).sort_values(ascending=False).head(3)

                BG_COLOR = "#001D7E"
                TEXT_COLOR = "white"
                PALETTE = ["#7C3AED", "#EC4899", "#F59E0B"]
                sns.set_theme(style="whitegrid", font_scale=1.0)

                fig, ax = plt.subplots(figsize=(6, 4), facecolor=BG_COLOR)
                ax.set_facecolor(BG_COLOR)

                sns.barplot(
                    x=series.index,
                    y=series.values,
                    palette=PALETTE[:len(series)],
                    ax=ax,
                    edgecolor="none"
                )
                ax.set_ylim(0, 1)
                ax.set_xlabel("")
                ax.set_ylabel("Probability", color=TEXT_COLOR)
                ax.set_title("Top 3 Predicted Emotions", color=TEXT_COLOR, pad=12)

                ax.tick_params(colors=TEXT_COLOR)
                for spine in ax.spines.values():
                    spine.set_visible(False)

                ax.grid(axis="y", linestyle=":", linewidth=0.8, color='white', alpha=0.2)

                for p in ax.patches:
                    ax.annotate(f"{p.get_height():.1%}",
                                (p.get_x() + p.get_width()/2, p.get_height()),
                                ha="center", va="bottom", xytext=(0, 6),
                                textcoords="offset points", color=TEXT_COLOR)

                st.pyplot(fig, clear_figure=True)

            else:
                st.json(data)

st.image("media/banner.png", use_container_width=True)
