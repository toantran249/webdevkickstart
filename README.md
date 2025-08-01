# Simple ChatGPT Chatbot with Streamlit

A simple chatbot application built with Streamlit and OpenAI's ChatGPT API.

## Features

- 🤖 Interactive chat interface
- 💬 Conversation history
- 🔄 Clear conversation option
- 🎨 Clean and modern UI
- ⚙️ Easy configuration

## Setup Instructions

### 1. Install Dependencies

Choose one of the following methods:

**Using pip:**
```bash
pip install -r requirements.txt
```

**Using pipenv:**
```bash
pipenv install
pipenv shell
```

### 2. Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create an account or sign in
3. Generate a new API key

### 3. Configure Environment

1. Copy the `.env` file template
2. Replace `your_openai_api_key_here` with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

### 4. Run the Application

```bash
streamlit run chatbot.py
```

The application will open in your default web browser at `http://localhost:8501`

## Usage

1. Type your message in the chat input at the bottom
2. Press Enter or click Send
3. Wait for the AI response
4. Continue the conversation
5. Use the "Clear Conversation" button in the sidebar to start fresh

## Project Structure

```
demo-python/
├── chatbot.py          # Main chatbot application
├── .env               # Environment variables (API key)
├── requirements.txt   # Python dependencies
├── Pipfile           # Pipenv dependencies
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Important Notes

- Keep your `.env` file secure and never commit it to version control
- The `.gitignore` file is configured to exclude sensitive files
- The chatbot uses GPT-3.5-turbo model by default
- API usage will be charged according to OpenAI's pricing

## Troubleshooting

**"OpenAI API key not found" error:**
- Make sure your `.env` file exists in the project root
- Verify the API key is correctly set in the `.env` file
- Ensure there are no extra spaces or quotes around the API key

**Import errors:**
- Run `pip install -r requirements.txt` to install dependencies
- If using pipenv, run `pipenv install` and `pipenv shell`

**Streamlit not opening:**
- Check if the application is running on `http://localhost:8501`
- Try `streamlit run chatbot.py --server.port 8502` to use a different port
