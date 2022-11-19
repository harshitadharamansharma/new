import os
import sys
import re
from config import config
from preprocessing import query_preprocessor
from utils import bot_print, bot_print_with_name
from utils import bot_input_with_name, user_input_with_name
from utils import get_keyword_classes_from_query, get_keyword_dictionary_from_query
from utils import get_best_match_rule, invalid_query_prompt
# from rule_handlers import *

def show_greeting():

    # bot_print_with_name(f"Hello! I am {config["BOT_NAME"].title()}. You can ask me your UG admissions related queries.")    
    bot_print_with_name(" Hi! What are you looking for?")
    bot_print("Let me know how can I help you.")
    bot_print(" What are you looking for?")
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

    return query


def chat_init():

    user_name = get_user_name()
    show_greeting()

    continue_chat_flag = True

    while continue_chat_flag == True :
        
        query = get_user_query(user_name)
        # keyword_classes = get_keyword_classes_from_query(query)
        # print(keyword_classes)
        preprocessed_query = query_preprocessor(query)
        
        if "quit" in preprocessed_query:
            sys.exit(0)

        keyword_classes_dictionary = get_keyword_dictionary_from_query(preprocessed_query)
        print(keyword_classes_dictionary)
        # call_rulehandler(keyword_dictionary)

        query_token_set = set(keyword_classes_dictionary.keys())

        if 'entity' in keyword_classes_dictionary.keys():    
            query_token_set.add(keyword_classes_dictionary['entity'])
            query_token_set.remove('entity')
        # print(query_token_set)

        best_match_rule = get_best_match_rule(query_token_set)
        #this will return rule_handler function

        if best_match_rule == str(-1): 
            invalid_query_prompt() 
        else:
            response = best_match_rule(keyword_classes_dictionary)
            bot_print_with_name(response)

    return 0



if __name__ == "__main__":

    config["TAB_WIDTH"] = " " * (len(config["BOT_NAME"]) + 2)
    chat_init()

    
    

    
    
