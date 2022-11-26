from config import config
from chatbot import chat_init


if __name__ == "__main__":

    config["TAB_WIDTH"] = " " * (len(config["BOT_NAME"]) + 2)
    chat_init()

