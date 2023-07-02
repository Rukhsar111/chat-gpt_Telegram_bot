# chat-gpt_Telegram_bot
chat-gpt_Telegram_bot

# chatGPT-Telegram-bot: How to build powerful chatbots with ChatGPT API, Python, and Telegram

## Prerequisites
- Python 3.7 or higher
- A Telegram account
- An OpenAI account and an API key

  ## How to run the code

1. Clone this repository or download the zip file
2. Create a virtual environment and activate it
3. Install the dependencies using `pip install -r requirements.txt`
    > Or alternatively to the above two steps you can run `init_setup.sh` by running the following command in your terminal-
    ```bash
    bash init_setup.sh
    ```
4. Create a `.env` file in the root directory and add your OpenAI API key and Telegram BOT TOKEN [refered as TOKEN here] as follows:

```ini
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TOKEN=xxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

5. Run `python src/chatgpt.py` to start the bot
6. Open Telegram and search for your bot username
7. 7. Start a conversation with your bot and enjoy!
