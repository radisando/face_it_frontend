# <b>PROJECT NAME</b>
Emotion Recognition Web App (face_it)
🔗 Live Demo

# <b>DESCRIPTION</b>
• Developed an AI-powered web application that recognizes human emotions from facial expressions in real time.
• Collaborated in a 5-person team, focusing on both model performance (deep learning, bias reduction) and scalable deployment (Streamlit frontend + FastAPI backend in Docker).
• Implemented a pipeline where user-uploaded images are preprocessed (grayscale, resize, normalize) and classified using a Convolutional Neural Network (CNN) and transfer learning with ResNet50.
• Enhanced explainability & trust with Grad-CAM visual heatmaps and SHAP feature importance to interpret model predictions.

# <b>GOAL</b>
• Design an accurate, fair, and explainable AI system, with special focus on reducing misclassifications of subtle emotions (e.g., Fear vs. Disgust). Deliver a solution that’s interpretable, production-ready, and user-friendly.

<b>DATASET</b>
• FER-2013 dataset (~40k labeled face images, PNG/JPG)
• Applied augmentation to rebalance underrepresented classes
• Seven emotion categories:
😊 Happiness | 😢 Sadness | 😱 Fear | 😡 Anger | 🤢 Disgust | 😲 Surprise | 😐 Neutral

# <b>KEY FEATURES</b>
📸 Upload face images for recognition
🧹 Automated preprocessing pipeline (grayscale, resize, normalization)
🤖 Deep learning classification into 7 emotions (CNN + ResNet50)
🪞 Explainability with Grad-CAM & SHAP
⚡ Full-stack deployment: Streamlit frontend + FastAPI backend + Docker
☁️ Cloud-ready architecture for scaling real-time applications
