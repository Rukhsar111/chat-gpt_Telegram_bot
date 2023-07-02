import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import openai


class Reference:
    """
    A class to store the previous response from the chatGPT API
    """
    def __init__(self)-> None:
        self.response=""


    
    
# Load environment variables
load_dotenv()

# Set up OpenAI API Key
openai.api_key=os.getenv("OPEN_API_KEY")

#Create a reference object to store the previous response
reference=Reference()


# Bot taken cab be obtained via 
TOKEN=os.getenv("TOKEN") 

# Model uset in chatGPT 
Model_Name="gpt-3.5-turbo"


# initialize bot and dispatcher
bot=Bot(token=TOKEN)
dispatcher=Dispatcher(bot)

def clear_past():
    """
    A function to clear the previous conversations and context.
    """

    reference.response=""


@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    A function to welcome the User and clear the previous conversations and context
    """

    clear_past()
    await message.reply(f"Hello! \nI'm  chatGPT Telegram bot created by Rukhsar! \n How may I assist yoy today?")
    


@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A function to clear the previous conversations and context
    """
    clear_past()
    await message.reply(f"I've cleared the past converstions")
    


@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A  handler to display the help menu.
    """

    help_command="""
    Hi!! I'm a bot created by Rukhsar. Please follow these commands.
    /start - to start the conversation .
    /clear - to clear the pat conversations.
    /help -  to get this help menu.
    I hope this helps.
    """

    await message.reply(help_command)

    
@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the users'input and generate a response using the ChatGPT API.
    """

    response=openai.ChatCompletion.create(
        model=Model_Name,
        messages=[
            {"role": "assistant" , "content": reference.response},
            {"role": "user","content": message.text}
        ]
    )
    reference.response=response['choices'][0]['message']['content']
    await bot.send_message(chat_id=message.chat.id, text=reference.response)




if __name__== '__main__':
    executor.start_polling(dispatcher, skip_updates=True)







