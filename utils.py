from config import config
from nltk.stem import WordNetLemmatizer
from synonyms import synonyms
from keyword_classes import keyword_classes

from rulebase import rulebase
import re
import random
import keyboard


def bot_print(message):
    print(config["TAB_WIDTH"] + message + "\n")


def bot_print_with_name(message):
    print(config["BOT_NAME"].title() +  ": " +  message + "\n")
    # keyboard.press('enter')


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
    query2_dict = dict()
 
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
                query2_dict[key]=sh_kw
 
    # query_dict = {}
    # for key in shortlisted_keyword_classes:
    #     for value in shortlisted_keywords:
    #         query_dict[key] = value
    #         break
 
    # query_dict = dict(zip(shortlisted_keyword_classes,shortlisted_keywords))
    # print(query_dict)
    # print("quey2_dict is = " + str(query2_dict))
    return query2_dict


def get_query_token_set(keyword_classes_dictionary):
    
    query_token_set = set(keyword_classes_dictionary.keys())

    if  'quantifier' in keyword_classes_dictionary.keys() or 'show' in keyword_classes_dictionary.keys() : 
        
        if 'entity' in keyword_classes_dictionary.keys():    
            query_token_set.add(keyword_classes_dictionary['entity'])
            query_token_set.remove('entity')
               
            # if ('degree' in keyword_classes_dictionary.keys()) and ('programme' not in keyword_classes_dictionary.values()):
            if 'degree' in query_token_set and 'programme' not in query_token_set:
                
                if 'degreetype' in keyword_classes_dictionary.keys() and 'course' not in keyword_classes_dictionary.keys():
                    keyword_classes_dictionary['course'] = "d"
                    query_token_set.add('course')

                elif 'degreetype' not in keyword_classes_dictionary.keys() and 'course' not in keyword_classes_dictionary.keys():
                    keyword_classes_dictionary['course'] = "d"
                    query_token_set.add('course')  
                    keyword_classes_dictionary['degreetype'] = "d"
                    query_token_set.add('degreetype')

                elif 'degreetype' not in keyword_classes_dictionary.keys() and 'course' in keyword_classes_dictionary.keys():
                    keyword_classes_dictionary['degreetype'] = "d"
                    query_token_set.add('degreetype')
            
    return query_token_set    



def get_best_match_rule(query_set):
    ''' parameter :-  set of keywords present in the query
        return:- rule_handler function from rulebase'''
    for rule in rulebase:
        rule_format_set = set(str(rulebase[rule]["rule_format"]).split("_"))   # :b d:
        if rule_format_set == query_set :
            # print("yes")
            return rulebase[rule]["rule_handler"]        
    return str(-1)  # if no match found 
        
def get_response_formatter(query_set):
    ''' parameter :-  set of keywords present in the query
        return:- response_formatter function from rulebase'''
    for rule in rulebase:
        rule_format_set = set(str(rulebase[rule]["rule_format"]).split("_"))   # :b d:
        if rule_format_set == query_set :
            # print("yes")
            return rulebase[rule]["response_formatter"]        
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


# def check_programme_exists():
#    pass


def get_rule_with_max_token_score(query_set):

        final_rule_token_score_dict = dict()
        max_token_score = 0

        for rule in rulebase:
            rule_format_set = set(str(rulebase[rule]["rule_format"]).split("_"))
            rule_token_score = 0

            for token in query_set:
                if token in rule_format_set :
                    rule_token_score += 1
                # print(rule_token_score)
            # max_token_score = max(max_token_score, rule_token_score)
            
            if max_token_score < rule_token_score:
                max_token_score = rule_token_score
                rule_with_max_score = rulebase[rule]["rule_handler"]
        # print(max_token_score, "ok")

        if max_token_score == 0:
            return str(-1)
            return str('No rule matched')

        final_rule_token_score_dict["rule"] = rule_with_max_score 
        final_rule_token_score_dict["score"] = max_token_score

        return final_rule_token_score_dict

'''def get_rule_with_max_token_score(query_set):

    rule_token_score_dict = dict()
    rule_lenght_score_dict = dict()
    has_required_tokens = True
    rule_with_max_token_score = dict()
    
    for rule in rulebase:
        rule_format_set = set(str(rulebase[rule]["rule_format"]).split("_"))
        rule_token_score = 0
        lenght_of_query_in_rule = 0

        for token in query_set:
            if token in rule_format_set :
                rule_token_score += 1
                lenght_of_query_in_rule += len(token)
                
        if rule_token_score == 0:
                has_required_tokens = False

        rule_token_score_percentage = 100*(float(rule_token_score) / float(len(rule_format_set)))

        # for token in query_set:
        #     if token not in rule_format_set:
        #         has_required_tokens = False
        #         break

        if has_required_tokens == True:
            rule_token_score_dict[rule] = rule_token_score_percentage
            rule_lenght_score_dict[rule] = lenght_of_query_in_rule
        else:
            rule_token_score_dict[rule] = 0
            rule_lenght_score_dict[rule] = 0

    for rule, score in rule_token_score_dict.items():        
        print(rule,":",score)

    number_of_rules_with_same_max_score = 0

    for rule, score in rule_token_score_dict.items():
        max_score_found = max(rule_token_score_dict.values())
        if score is max_score_found and max_score_found != 0:
            print("Rule number with max score is : \"", str(rule), "\" with score: ", score)
            number_of_rules_with_same_max_score += 1 
            rule_with_max_token_score[number_of_rules_with_same_max_score]["rule_number"] = rule
            rule_with_max_token_score[number_of_rules_with_same_max_score]["score"] = score
            rule_with_max_token_score[number_of_rules_with_same_max_score]["rule"] = rulebase[rule]["rule_handler"]
            rule_with_max_token_score[number_of_rules_with_same_max_score]["rule_format_set"] = set(str(rulebase[rule]["rule_format"]).split("_"))
            rule_with_max_token_score[number_of_rules_with_same_max_score]["response_formatter"] = rulebase[rule]["response_formatter"]
            print(str(rule_with_max_token_score["rule"]))
        else:
            rule_with_max_token_score["rule"]

    print("there is/are ", str(number_of_rules_with_same_max_score), "with max score")

    # if number_of_rules_with_same_max_score > 1:
    #     max_lenght = 0
    #     # max_token_lenght = max(len(rule_with_max_token_score[]["rule_format_set"]))
    #     for r in rule_with_max_token_score:
    #         if max_lenght >= r[number_of_rules_with_same_max_score]["rule_format_set"]:
    #             max_lenght = rule_token_score_dict
    #             rule_with_max_lenght = rule_formet_set
    #         else:
    #         # max_lenght = max(max_lenght, rule_lenght_score_dict[r])
    #             rule_with_max_lenght = 

    return rule_with_max_token_score'''


'''This was to count the length of the appended list of the elemnts present in the query_token_set or query_set'''
# def get_rule_with_max_length_score(query_set):

#     final_rule_length_score_dict = dict()
#     max_token_score = 0

#     for rule in rulebase:
#         rule_format_set = set(str(rulebase[rule]["rule_format"]).split("_"))
#         rule_token_score = 0


#         for token in query_set:
#             if token in rule_format_set :
#                 rule_token_score += 1
#             # print(rule_token_score)
#         # max_token_score = max(max_token_score, rule_token_score)
#         if max_token_score < rule_token_score:
#             max_token_score = rule_token_score
#             rule_with_max_score = rulebase[rule]["rule_handler"]
#     # print(max_token_score, "ok")

#     if max_token_score == 0:
#         return str(-1)
#     final_rule_length_score_dict["rule"] = rule_with_max_score 
#     final_rule_length_score_dict["score"] = max_token_score

#     return final_rule_length_score_dict 
    
def get_max_length_from_response(keyword_classes_dictionary):

    string_query_token = str()
    for a in keyword_classes_dictionary.values():
        # print(a)
        string_query_token = string_query_token.join(a.strip())
        # print(a)
    max_token_score = len(string_query_token)
    # print(max_token_score )

    return max_token_score

# def 
     
     

# Checkpoints :- define checkpoint rules
# rule score then ask for slot filling
