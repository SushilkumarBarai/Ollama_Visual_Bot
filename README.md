# 🖼️ Image Chatbot with Ollama

Welcome to the **Image Chatbot**, a powerful, efficient, and scalable web application built using **Streamlit** and **Ollama**.  
Upload multiple images and seamlessly interact with them by asking natural questions.  
Experience lightning-fast responses with local AI models, without relying on cloud services.  
Choose from multiple advanced models like `minicpm-v`, `llava`, and more.  
Built for performance, real-time interaction, and a smooth ChatGPT-like experience!

---

## 📌 Project Overview

This chatbot allows users to:

- Upload up to **7 images** (PNG, JPEG, JPG).
- Select an available **Ollama** model to interact with.
- **Chat** and ask questions about the uploaded images.
- View responses in a **beautiful ChatGPT-like** chat interface.
- Handle **Multiple of concurrent users** with optimized session management.

---

## 🚀 Features

- 🎨 **Multiple Image Upload:** Upload and preview up to 7 images.
- ⚡ **Real-time Chat:** Chat with images context just like a human assistant.
- 🔥 **Ollama Model Support:** Choose from locally running Ollama models.
- 🧠 **Efficient Model Handling:** Cached API calls for available models.
- 🛡️ **Scalable:** Built to handle large user traffic with session-based architecture.
- 🎯 **Beautiful UI:** Modern ChatGPT-style conversation layout.
- 📦 **Lightweight:** No heavy backend setup — just Streamlit + Ollama.

---

# Screenshot 

Here’s a screenshot of the application:

### Sample 1


![Screenshot](https://github.com/SushilkumarBarai/Ollama_Visual_Bot/blob/main/images/Screenshot.png)


### Sample 2

![Screenshot](https://github.com/SushilkumarBarai/Ollama_Visual_Bot/blob/main/images/Screenshot_2.png)


## 📚 Technology Stack

| Technology      | Purpose |
|:----------------|:--------|
| **Python**       | Core programming language |
| **Streamlit**    | Frontend & application framework |
| **Ollama**       | Local AI model serving (vision + language models) |
| **LangChain**    | Model binding & context management |
| **Pillow (PIL)** | Image processing |
| **Requests**     | HTTP API calls (to Ollama server) |


## 📖 About Ollama

**Ollama** is a platform that allows you to run advanced AI models — **locally on your own machine** — without sending any data to external servers.

It acts as a **lightweight local server** for AI models, similar to how databases run locally.  
You can pull large language models (LLMs) or multimodal models (like vision + language) directly using `ollama`.

In this project:

- Ollama serves models like **MiniCPM**, **LLaVA**, and other **vision-capable models**.
- Our chatbot **connects to Ollama's REST API** to send **images + text** and receive **AI responses**.
- **No model downloading** is needed inside the Streamlit app — just interact with your local Ollama models!

> **Example Ollama commands:**
> ```bash
> ollama pull minicpm-v
> ollama pull llava
> ollama run minicpm-v
> ```

For more details, visit: [https://ollama.com/](https://ollama.com/)


---

## 🖥️ How to Run Locally

### 1. Prerequisites

- Python 3.8+
- Ollama installed and running locally
- Basic knowledge of Streamlit

### 2. Clone the Repository

```bash
git clone https://github.com/SushilkumarBarai/Ollama_Visual_Bot.git
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Application
```
streamlit run app.py
```