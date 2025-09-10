import os
import io
import requests
import streamlit as st
from PIL import Image
from theme import apply_theme
from streamlit_lottie import st_lottie

# ---------- Theme & Page ----------
apply_theme()
st.set_page_config(page_title="Face It", page_icon="🤖", layout="wide")

st.title("Face It: We've Got Feelings")
st.write("Hello and welcome!")
st.write("We trained an AI model to be able to predict the emotion from a human face. Give it a try: upload an image and let our model guess the emotion.")

# ---------- API URL setup ----------
BASE_URI = os.getenv("CLOUD_API_URI") or st.secrets.get("cloud_api_uri") or "http://localhost:8000"
if not BASE_URI.endswith("/"):
    BASE_URI += "/"
PRED_ENDPOINT = BASE_URI + "predict"


st.markdown("Tip: please upload a clear, front-facing picture of a face.")

# ---------- File uploader ----------
uploaded = st.file_uploader("Upload here!", type=["jpg", "jpeg", "png"])

if uploaded:
    st.image(uploaded, caption="Preview", use_container_width=False)

    if st.button("Identify Emotion!"):
        img_bytes = uploaded.getvalue()
        content_type = uploaded.type or "image/jpeg"

        with st.spinner("🤖 Running the AI model… please wait!"):
            try:
                # call the API
                files = {"file": (uploaded.name or "image.jpg", img_bytes, content_type)}
                r = requests.post(PRED_ENDPOINT, files=files, timeout=30)
                r.raise_for_status()

                data = r.json()

                # FastAPI returns {label, confidence, probabilities}
                label = data.get("label") or data.get("emotion", "unknown")
                conf = data.get("confidence")
                probs = data.get("probabilities") or data.get("scores") or {}

                # show result
                # --- Emotion styles: text color + translucent background (8-digit hex supports alpha) ---
                EMOTION_STYLES = {
                    "happy":    {"fg": "#111111", "bg": "#FACC1533"},  # yellow bg, dark text
                    "sad":      {"fg": "#DBEAFE", "bg": "#3B82F633"},  # blue
                    "angry":    {"fg": "#FEE2E2", "bg": "#EF444433"},  # red
                    "fear":     {"fg": "#EDE9FE", "bg": "#8B5CF633"},  # violet
                    "surprise": {"fg": "#FCE7F3", "bg": "#EC489933"},  # pink
                    "disgust":  {"fg": "#ECFDF5", "bg": "#10B98133"},  # green
                    "neutral":  {"fg": "#F3F4F6", "bg": "#9CA3AF33"},  # gray
                }

                # --- Lottie animations ---
                EMOTION_LOTTIES = {
                    "happy":    "https://assets10.lottiefiles.com/private_files/lf30_j1cnylcf.json",
                    "sad":      "https://assets10.lottiefiles.com/private_files/lf30_dg5hxlqy.json",
                    "angry":    "https://assets9.lottiefiles.com/packages/lf20_kq5rGs.json",
                    "fear":     "https://assets3.lottiefiles.com/packages/lf20_t24tpvcu.json",
                    "surprise": "https://assets5.lottiefiles.com/packages/lf20_GU9EGA.json",
                    "disgust":  "https://assets1.lottiefiles.com/packages/lf20_klvnyf8c.json",
                    "neutral":  "https://assets4.lottiefiles.com/packages/lf20_bKvfZL.json"
                }

                def load_lottie(url: str):
                    try:
                        r = requests.get(url)
                        if r.status_code == 200:
                            return r.json()
                    except Exception:
                        return None
                    return None



                conf_txt = f" ({conf:.1%})" if isinstance(conf, (int, float)) else ""
                style = EMOTION_STYLES.get(label.lower(), {"fg": "#FFFFFF", "bg": "#FFFFFF22"})
                lottie_url = EMOTION_LOTTIES.get(label.lower())

                col1, col2 = st.columns([2, 1])

                with col1:
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
                        👩Predicted Emotion: {label}{conf_txt}
                      </span>
                    </div>
                    """
                    st.markdown(badge_html, unsafe_allow_html=True)

                with col2:
                    if lottie_url:
                        lottie_json = load_lottie(lottie_url)
                        if lottie_json:
                            st_lottie(lottie_json, height=100, key=f"anim_{label}")





                #conf_txt = f" ({conf:.1%})" if isinstance(conf, (int, float)) else ""
                #st.success(f"Predicted emotion: **{label}**{conf_txt}")

                if isinstance(probs, dict) and probs:
                    import pandas as pd
                    import matplotlib.pyplot as plt
                    import seaborn as sns
                    import numpy as np
                    import streamlit as st

                    # --- Data (top 3) ---
                    series = pd.Series(probs).sort_values(ascending=False).head(3)

                    # --- Theme / palette (tweak these to your page colors) ---
                    # purple, pink, amber accents
                    BG_COLOR = "#001D7E"
                    TEXT_COLOR = "white"
                    PALETTE = ["#7C3AED", "#EC4899", "#F59E0B"]
                    sns.set_theme(style="whitegrid", font_scale=1.0)

                    col1, col2 = st.columns(2)

                    # ---------- BAR (seaborn) ----------
                    with col1:
                        fig, ax = plt.subplots(figsize=(6, 4), facecolor=BG_COLOR)
                        ax.set_facecolor(BG_COLOR)

                        sns.barplot(
                            x=series.index,
                            y=series.values,
                            palette=PALETTE[:len(series)],
                            ax=ax,
                            edgecolor="none"
                        )
                        ax.set_ylim(0, 1)  # probs 0..1
                        ax.set_xlabel("")
                        ax.set_ylabel("Probability", color=TEXT_COLOR)
                        ax.set_title("Top 3 Probabilities (Bar)", color=TEXT_COLOR, pad=12)
                        # prettify

                        ax.tick_params(colors=TEXT_COLOR)
                        for spine in ax.spines.values():
                            spine.set_visible(False)



                        ax.grid(axis="y", linestyle=":", linewidth=0.8, color='white', alpha=0.2)

                        # value labels on bars
                        for p in ax.patches:
                            ax.annotate(f"{p.get_height():.1%}",
                                        (p.get_x() + p.get_width()/2, p.get_height()),
                                        ha="center", va="bottom", xytext=(0, 6),
                                        textcoords="offset points", color=TEXT_COLOR)

                        st.pyplot(fig, clear_figure=True)

                    # ---------- DONUT PIE (matplotlib) ----------
                    with col2:
                        fig2, ax2 = plt.subplots(figsize=(6, 4), facecolor=BG_COLOR)
                        ax2.set_facecolor(BG_COLOR)

                        wedges, texts, autotexts = ax2.pie(
                            series.values,
                            labels=series.index,
                            autopct="%.1f%%",
                            startangle=90,
                            pctdistance=0.78,
                            labeldistance=1.05,
                            colors=PALETTE[:len(series)],
                            textprops={"color": TEXT_COLOR}
                        )
                        # donut hole
                        centre = plt.Circle((0, 0), 0.55, fc=BG_COLOR)
                        ax2.add_artist(centre)
                        ax2.axis("equal")
                        ax2.set_title("Top 3 Probabilities (Pie)", color=TEXT_COLOR, pad=12)

                        st.pyplot(fig2, clear_figure=True)





                # show probabilities as a bar chart if present
                #if isinstance(probs, dict) and probs:
                #    import pandas as pd
                #    import matplotlib.pyplot as plt

                #    # convert to Series and keep top 3
                #    series = pd.Series(probs).sort_values(ascending=False).head(3)

                #    # layout: bar chart left, pie chart right
                #    col1, col2 = st.columns(2)

                #    with col1:
                #        st.subheader("Top 3 Probabilities (Bar)")
                #        st.bar_chart(series)

                #    with col2:
                #        st.subheader("Top 3 Probabilities (Pie)")
                #        fig, ax = plt.subplots()
                #        ax.pie(series, labels=series.index, autopct="%.1f%%", startangle=90)
                #        ax.axis("equal")  # equal aspect ratio makes it a circle
                #        st.pyplot(fig)

                ##if isinstance(probs, dict) and probs:
                ##    import pandas as pd
                ##    df = pd.Series(probs).sort_values(ascending=False).to_frame("probability")
                ##    st.bar_chart(df)
                else:
                    st.json(data)  # fallback: show raw payload

            except requests.exceptions.RequestException as e:
                st.error(f"API call failed: {e}")







st.caption(f"🔗 Working with API at: {PRED_ENDPOINT}")  # dev only, remove in prod
