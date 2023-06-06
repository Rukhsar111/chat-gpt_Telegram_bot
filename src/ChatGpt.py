import os
from dotenv import load_dotenv
from aiogram import bot, dispatcher, executor, types


class Reference:
    """
    A class to strore the previous response from the chatGPT API
    """

    raise NotImplementedError
    
# Load environment variables
load_dotenv()

# Set up OpenAI API Key


#Create a reference object to store the previous response


# Bot taken cab be obtained via 
Token=os.getenv("Token") 

# Model uset in chatGPT 

# initialize bot and dispatcher
bot=Bot(token=Token)
dispatcher=Dispatcher(bot)

def clear_past():
    """
    A function to clear the previous conversations and context.
    """

    raise NotImplementedError


@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    A function to welcome the User and clear the previous conversations and context
    """


    raise NotImplementedError


@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message)
    """
    A function to clear the previous conversations and context
    """

    raise NotImplementedError


@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message)
    """
    A  handler to display the help menu.
    """

    raise NotImplementedError





@dispatcher.message_handler()
async def chatgpt(message: types.Message)
    """
    A handler tp process the users'input and generate a response using the ChatGPT API.
    """

    raise NotImplementedError



if __name__== '__main__':
    executor.start_polling(dispatcher, skip_updates=True)







