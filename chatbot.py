import os
import sys
import re
import keyboard
from config import config
from preprocessing import query_preprocessor
from utils import bot_print, bot_print_with_name
from utils import bot_input_with_name, user_input_with_name
from utils import get_keyword_classes_from_query, get_keyword_dictionary_from_query
from utils import get_best_match_rule, invalid_query_prompt, get_response_formatter
from utils import get_rule_with_max_token_score
from utils import get_query_token_set, get_max_length_from_response

# from rule_handlers import *

def show_greeting():

    # bot_print_with_name(f"Hello! I am {config["BOT_NAME"].title()}. You can ask me your UG admissions related queries.")    
    bot_print_with_name(" Hi! What are you looking for?")
    bot_print("Let me know your queries.")
    # bot_print(" What are you looking for?")
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

    query = get_user_query(user_name)

    while continue_chat_flag == True :
        
        # keyword_classes = get_keyword_classes_from_query(query)
        # print(keyword_classes)
        preprocessed_query = query_preprocessor(query)
        
        if "quit" in preprocessed_query:
            sys.exit(0)

        keyword_classes_dictionary = get_keyword_dictionary_from_query(preprocessed_query)
        # print(keyword_classes_dictionary)
        # call_rulehandler(keyword_dictionary)

        
        query_token_set = get_query_token_set(keyword_classes_dictionary)
        print(keyword_classes_dictionary)
        print(query_token_set)

        max_length_score = get_max_length_from_response(keyword_classes_dictionary)
        # print(max_length_score)
        
        best_match_rule = get_best_match_rule(query_token_set)

        #this will return rule_handler function
        # print(get_rule_with_max_token_score(query_token_set), "get_rule_with_max_token_score")
        #check token scores 

        if best_match_rule == str(-1): 
            invalid_query_prompt() 
        else:
            response_dict = best_match_rule(keyword_classes_dictionary)
            best_match_response_formatter = get_response_formatter(query_token_set)
            response = best_match_response_formatter (response_dict)
            bot_input_with_name(response) 

        query = get_user_query(user_name)    
    return 0



# if __name__ == "__main__":

#     config["TAB_WIDTH"] = " " * (len(config["BOT_NAME"]) + 2)
#     chat_init()
