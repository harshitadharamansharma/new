from config import config
from nltk.stem import WordNetLemmatizer
from synonyms import synonyms
from keyword_classes import keyword_classes

from rulebase import rulebase
import re
import random


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



def get_best_match_rule(query_set):
    '''this method will take keyword classes set as input and if the tokens(keywords in the set is euql to the elements in the set generated after spluting the rule_format string then the best mathed rule will be returned'''
    for rule in rulebase:
        rule_format_set = set(str(rulebase[rule]["rule_format"]).split("_"))   # :b d:
        if rule_format_set == query_set :
            return rulebase[rule]["rule_handler"]
    return str(-1)  # if no match found 
        

def invalid_query_prompt():
    invalid_query_responses = [ "I didn't get this! can you please come again?",
    "Not able to process this, could you repeat that",  "Didn't get what you want?", "Your query is either invalid or can't be processed", 
    "OK! let me process your query! Could you repeat that? ", " Wrong input!"]
    bot_print_with_name(random.choice(invalid_query_responses))



def want_to_know_more_prompt(know_more_link):
    bot_input_with_name(f"Want to know more about the website? Check out the link:- {know_more_link}")


def do_you_mean_this_prompt():
    '''This function will be called for queries such as 'no. of faculty in college' to confirm wether the user meant the same as it was matched by the best_rule_match() method, or something else; the query is valid but no such entry is there in the university as no such heirachy exist. So rule with similar rokens will be asked otherwise, and will be confirmed via confirmation prompt..... (this can be coonsidered as second best match ,  (string vector position:- this is generally used for synonyms, but can also be experimented here )) ...'''
    pass



