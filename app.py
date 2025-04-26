import streamlit as st
import requests
from langchain_community.llms import Ollama
import base64
from io import BytesIO
from PIL import Image

# ------------- Helpers ---------------

@st.cache_data(show_spinner=False)
def get_available_models():
    """
    Fetch available models from Ollama server only once.
    """
    try:
        response = requests.get("http://localhost:11434/api/tags")
        response.raise_for_status()
        models = response.json().get("models", [])
        available_models = [model["name"] for model in models]
        return available_models
    except Exception as e:
        st.error(f"Error fetching models from Ollama server: {e}")
        st.stop()


def convert_to_base64(image_file_path):
    """
    Convert PIL images to Base64 encoded strings.
    """
    pil_image = Image.open(image_file_path)
    buffered = BytesIO()
    pil_image.save(buffered, format="png")  
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def convert_to_html(img_base64):
    """
    Display base64 encoded string as HTML image tag.
    """
    image_html = f'<img src="data:image/png;base64,{img_base64}" style="max-width: 100%;"/>'
    return image_html


@st.cache_data(show_spinner=False)
def ask_vllm(question, image_b64_list, model):
    llm = Ollama(model=model)
    llm_with_image_context = llm.bind(images=image_b64_list)
    response = llm_with_image_context.invoke(question)
    return response

# ------------- Main App ---------------

def main():
    st.set_page_config(page_title="Image Chatbot - Ollama", page_icon="🖼️", layout="wide")
    st.title("🖼️ Local Image Chatbot with Ollama")
    st.caption("Upload images and chat with AI about them!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "uploaded_images" not in st.session_state:
        st.session_state.uploaded_images = []
    if "model" not in st.session_state:
        st.session_state.model = None

    available_models = get_available_models()

    # --- Sidebar for settings ---
    with st.sidebar:
        st.header("⚙️ Settings")
        st.session_state.model = st.selectbox(
            "Choose a model",
            options=available_models,
            index=0
        )

        uploaded_files = st.file_uploader(
            "📂 Upload Images (max 7)",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True,
            key="upload"
        )

        if uploaded_files:
            if len(uploaded_files) > 7:
                st.error("You can upload at most 7 images.")
                st.stop()

            images_b64 = []
            with st.spinner("Processing images..."):
                for file in uploaded_files:
                    img_b64 = convert_to_base64(file)
                    images_b64.append(img_b64)

            st.session_state.uploaded_images = images_b64

            # Display uploaded images
            st.subheader("Uploaded Images:")
            cols = st.columns(len(images_b64))
            for idx, col in enumerate(cols):
                col.markdown(f"**Image {idx+1}**")
                col.markdown(convert_to_html(images_b64[idx]), unsafe_allow_html=True)

    st.divider()

    # --- Chat interface ---
    if st.session_state.uploaded_images:

        user_input = st.chat_input("Type your question about the image(s)")

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if user_input:
            # Show user message
            st.chat_message("user").markdown(user_input)

            # Add to history
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            # Model thinking...
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = ask_vllm(
                        user_input,
                        st.session_state.uploaded_images,
                        st.session_state.model
                    )
                    st.markdown(response)

            # Save assistant response
            st.session_state.chat_history.append({"role": "assistant", "content": response})

    else:
        st.info("👈 Please upload images first from the sidebar to start chatting!")


if __name__ == "__main__":
    main()
