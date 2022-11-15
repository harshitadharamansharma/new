import os
import sys
import re
from config import config
from preprocessing import query_preprocessor
from utils import bot_print, bot_print_with_name
from utils import bot_input_with_name, user_input_with_name
from utils import get_keyword_classes_from_query, get_keyword_dictionary_from_query
# from rule_handlers import *

def show_greeting():

    bot_print_with_name(" Hi! What are you looking for?")
    bot_print("You can ask queries like the following -")
    bot_print("1. Get me the list of colleges that have B.Sc. Honours Mathematics")
    bot_print("2. Show me the number of seats of SC category for BA Programme in Aryabhatta College")
    bot_print("3. List the colleges offering B.Ed.")
    bot_print("For more information on what you can ask the chatbot, visit x.y.com")
    bot_print("At any point, if you wish to abort the chat, type QUIT")


def get_user_name():

    user_name_prompt = "Please enter your name \n"
    user_name = bot_input_with_name(user_name_prompt)
    user_name = query_preprocessor(user_name)

    if user_name == 'quit':
        sys.exit(0)

    return user_name


def get_user_query(username):

    query = user_input_with_name(username)
    query = query_preprocessor(query)

    return query


def chat():

    user_name = get_user_name()
    show_greeting()

    continue_chat_flag = True

    while continue_chat_flag == True:

        query = get_user_query(user_name)
        # keyword_classes = get_keyword_classes_from_query(query)
        # print(keyword_classes)

        keyword_dictionary = get_keyword_dictionary_from_query(query)
        print(keyword_dictionary)
        # call_rulehandler(keyword_dictionary)

        # next_rule(keyword_dictionary)
        

    return 0


if __name__ == "__main__":

    config["TAB_WIDTH"] = " " * (len(config["BOT_NAME"]) + 2)
    # karan()
    chat()
