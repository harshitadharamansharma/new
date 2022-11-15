from config import config
from nltk.stem import WordNetLemmatizer
from synonyms import synonyms
from keyword_classes import keyword_classes
import re


def bot_print(message):
    print(config["TAB_WIDTH"] + message)


def bot_print_with_name(message):
    print(config["BOT_NAME"].title() +  ": " +  message)


def bot_input_with_name(prompt):
    bot_input = input(config["BOT_NAME"].title() + ": " + prompt)
    return bot_input


def user_input_with_name(username, prompt=None):

    if prompt == None:
        prompt = ""

    user_input = input(username.title() + ": " + prompt)
    return user_input


def get_lemmatized_query(query):
    
    lemmatizer = WordNetLemmatizer()

    original_keywords = query.split(" ")
    lemmatized_keywords = []

    for kw in original_keywords:
        # lemmatized_keywords.append(" " + lemmatizer.lemmatize(kw) + " ")
        lemmatized_keywords.append(lemmatizer.lemmatize(kw))

    lemmatized_query = " ".join(lemmatized_keywords)

    return lemmatized_query


def get_keyword_classes_from_query(query):

    # Spaces added at both ends of query so that the keywords at the edges are similarly treated as the keywords at the non-edge locations
    lemmatized_query = " " + get_lemmatized_query(query) + " "

    shortlisted_keywords = []
    shortlisted_keyword_classes = []

    for key in list(synonyms.keys()):
        for kw in synonyms[key]:
            match_found = re.search(r'( ' + kw + ' )', lemmatized_query)
            # Find (" " + kw + " ") in lemmatized_query:
            if match_found != None:
                shortlisted_keywords.append(key)
    
    for sh_kw in shortlisted_keywords:
        for key in list(keyword_classes.keys()):
            if sh_kw in keyword_classes[key]:
                shortlisted_keyword_classes.append(key) 

    return shortlisted_keyword_classes





def get_keyword_dictionary_from_query(query):
 
    # Spaces added at both ends of query so that the keywords at the edges are similarly treated as the keywords at the non-edge locations
    lemmatized_query = " " + get_lemmatized_query(query) + " "
 
    shortlisted_keywords = []
    shortlisted_keyword_classes = []
 
    for key in list(synonyms.keys()):
        for kw in synonyms[key]:
            match_found = re.search(r'( ' + kw + ' )', lemmatized_query)
            # Find (" " + kw + " ") in lemmatized_query:
            if match_found != None:
                shortlisted_keywords.append(key)
   
    for sh_kw in shortlisted_keywords:
        for key in list(keyword_classes.keys()):
            if sh_kw in keyword_classes[key]:
                shortlisted_keyword_classes.append(key)
 
    # query_dict = {}
    # for key in shortlisted_keyword_classes:
    #     for value in shortlisted_keywords:
    #         query_dict[key] = value
    #         break
 
    query_dict = dict(zip(shortlisted_keyword_classes,shortlisted_keywords))
    print(query_dict)
    return query_dict



def bot_confirmation_prompt(query_to_be_searched):
    bot_print_with_name("Are you asking for "+ query_to_be_searched +"?")
    bot_print("1.Yes! this what I was looking for.")
    bot_print("2.No! I asked something else.")
 
    confirmation = input("Enter the you choice 1 OR 2")
    if confirmation == 1:
        return True
    else :
        #call next rule from the handler
        pass
