# 🧠 Mental Health Support Bot

[![Rasa](https://img.shields.io/badge/Rasa-v3.x-blue.svg)](https://rasa.com/)
[![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](LICENSE)

A compassionate AI-powered chatbot designed to provide mental health support, resources, and a safe space for users to express their feelings. Built with the **Rasa Framework**, this bot utilizes Natural Language Understanding (NLU) to engage in meaningful conversations and offer guidance.

## 🚀 Key Features

- **Empathetic Conversations**: Engaging dialogue focused on mental well-being.
- **Resource Guidance**: Provides links and information for professional help.
- **Sentiment Analysis**: Understands the user's emotional state to respond appropriately.
- **Custom Actions**: Dynamic responses based on user interactions.
- **Multi-channel Support**: Can be integrated with web widgets, Socket.io, and more.

## 🛠️ Tech Stack

- **Framework**: [Rasa Open Source](https://rasa.com/)
- **Language**: Python
- **Natural Language Understanding**: Rasa NLU
- **Dialogue Management**: Rasa Core

## 📥 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/bahasuru-naya/Mental-health-bot.git
cd Mental-health-bot
```

### 2. Set up a Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install rasa
```

## 🎮 How to Run

### Option 1: Terminal Mode (CLI)
Open two terminal windows/tabs:

**Terminal 1 (Action Server):**
```bash
rasa run actions
```

**Terminal 2 (Chat Interface):**
```bash
rasa shell
```

### Option 2: GUI / Web Integration (Socket.io)
If you are using a web frontend:

**Terminal 1 (Action Server):**
```bash
rasa run actions
```

**Terminal 2 (API Server):**
```bash
rasa run -m models --enable-api --cors "*"
```

## 📂 Project Structure

- `data/`: Contains NLU training data, stories, and rules.
- `actions/`: Custom Python actions for complex logic.
- `config.yml`: Configuration for NLU and Core policies.
- `domain.yml`: Defines the bot's universe (intents, entities, slots, responses).
- `endpoints.yml`: Configuration for action server and other endpoints.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---
*Disclaimer: This chatbot is intended for supportive conversation and is not a substitute for professional medical advice, diagnosis, or treatment.*
