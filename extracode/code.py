from rulebase import rulebase

# path_1 = "C:\du_chatbot_terminal\data\college_course_category_seats.csv"
# file_1 = open(path_1, newline = '')
# reader1 = csv.reader(file_1)
# header1 = next(reader1)


# path_2 = "C:\du_chatbot_terminal\data\\faculty_department.csv"
# file_2 = open(path_2, newline = '')
# reader2 = csv.reader(file_2)
# header2 = next(reader2)


# path_3 = "C:\du_chatbot_terminal\data\college_course.csv"
# file_3 = open(path_3, newline = '')
# reader3 = csv.reader(file_3)
# header3 = next(reader3)

# path_4 = "C:\du_chatbot_terminal\data\college_course_category_coursefee.csv"
# file_4 = open(path_4, newline = '')
# reader4 = csv.reader(file_4)
# header4 = next(reader4)


# def get_csv_iterator(path):
#     file = open(path, newline = "")

# path_1 = "D:\\new_chat\\new_bot\data\college_course_category_seats.csv"
# file_1 = open(path_1, newline = '')
# reader1 = csv.reader(file_1)
# header1 = next(reader1)


# path_2 = "D:\\new_chat\\new_bot\data\\faculty_department.csv"
# file_2 = open(path_2, newline = '')
# reader2 = csv.reader(file_2)
# header2 = next(reader2)

# path_3 = "D:\\new_chat\\new_bot\data\college_course.csv"
# file_3 = open(path_3, newline = '')
# reader3 = csv.reader(file_3)
# header3 = next(reader3)

# path_4 = "D:\new_chat\new_bot\data\college_course_category_coursefee.csv"
# file_4 = open(path_4, newline = '')



# def bot_confirmation_prompt(query_to_be_searched):
#     print("Are you asking for"+ query_to_be_searched +"?")
#     print("1.Yes! this what I was looking for.")
#     print("2.No! I asked something else.")
 
#     confirmation = input("Enter the you choice 1 OR 2")
#     if confirmation == "1":
#         return True
#     elif confirmation ==  "2":
#         print("OK, can you please repeat your query?")
#         # invalid_query_prompt()
#         return False
#     else :
#         #call next rule from the handler
#         print("Wrong input!!")
#         return False


# NOTE::- for BA program we will add a note, that (we are going to process the application)every college has a separate combination of subjects for BA program go to this link for more information (if degree == B.A. and degreetype == program)

def get_rule_with_max_token_score(query_set):
    
    # rule_token_score = 0
    # max_token_score = 0
    rule_with_max_score 
    final_rule_token_score_dict = dict()
    for rule in rulebase:
        rule_token_score = 0
        max_token_score = 0
        for token in query_set:
            if token in set(str(rulebase[rule]["rule_format"].split("_"))):
                rule_token_score += 1
                rule_for_rulescore = rulebase[rule]["rule_handler"]
        # max_token_score = max(max_token_score, rule_token_score)
        if max_token_score < rule_token_score:
            max_token_score = rule_token_score
            rule_with_max_score = rule_for_rulescore
    if max_token_score == 0:
        return str(-1)
    final_rule_token_score_dict["rule"] = rule_with_max_score 
    final_rule_token_score_dict["score"] = max_token_score

    return final_rule_token_score_dict
    
def get_rule_with_max_token_score(query_set):
    # rule_token_score = 0
    # max_token_score = 0
    # rule_with_max_score 
    final_rule_token_score_dict = dict()
    # a=0
    
    for rule in rulebase:
        rule_format_set = set(str(rulebase[rule]["rule_format"]).split("_"))
        rule_token_score = 0
        max_token_score = 0
        # a =0
        # print(rule_format_set)
        # print(rulebase[rule]["rule_format"])
        # a+=1
        for token in query_set:
            # print(a, token)
            # a+=1
            if token in rule_format_set :
                # print("hh", rule_format_set)
                rule_token_score += 1
                rule_for_rulescore = rulebase[rule]["rule_handler"]
                # print(rule_token_score)
        # max_token_score = max(max_token_score, rule_token_score)
            if max_token_score < rule_token_score:
                max_token_score = rule_token_score
                rule_with_max_score = rule_for_rulescore
        print(max_token_score)
    if max_token_score == 0:
        return str(-1)
    final_rule_token_score_dict["rule"] = rule_with_max_score 
    final_rule_token_score_dict["score"] = max_token_score

    return final_rule_token_score_dict
    
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
    print(max_token_score, "ok")

    if max_token_score == 0:
        return str(-1)
    final_rule_token_score_dict["rule"] = rule_with_max_score 
    final_rule_token_score_dict["score"] = max_token_score

    return final_rule_token_score_dict
    


#7
def get_number_of_seats_for_category_for_degree_degreetype_course_at_college(query_dict):
# _programme
    college = query_dict['college'].lower()
    degree = query_dict['degree'].lower()
    degreetype = query_dict['degreetype'].lower()
    course = query_dict['course'].lower()
    category = query_dict['category'].lower()

    response_dict = dict()
    # response_dict["seats"] = 0
    response_dict["programme_not_available_flag"] = False
    ba_program_flag = False
    response_dict["link"] = str()
    query_results = int()

    # if degree == "b.a." and degreetype == "program":
    #     for r in reader6:
    #         if r[0].strip()=="b.a." and r[1].strip() == "program":
    #             response_dict["link"] == r[2].strip()
                # print("hh")
    
    # else:
       
    query_results = 0
    
    # for i in range(11,17):
    category_index_from_csv = header5.index(category) + 8
    # print(category_index_from_csv)

    for row in reader5:
        if row[0].strip() == college :

            # if degree == "b.a." and degreetype == "program":
            #     for r in reader6:
            #         if r[0].strip()=="b.a." and r[1].strip() == "program":
            #             response_dict["link"] == r[2].strip()
            #             ba_program_flag = True

            if row[1].strip() == degree and row[2].strip() == degreetype and row[3].strip() == course :
                if degree == "b.a." and degreetype == "program":
                    for r in reader6:
                        if r[0].strip()=="b.a." and r[1].strip() == "program":
                            response_dict["link"] == r[2].strip()
                            ba_program_flag = True
                else:
                    query_results = int(row[category_index_from_csv].strip())
                    print(query_results)

    if query_results == 0 and ba_program_flag == False:
        response_dict["programme_not_available_flag"] = True
        print(response_dict["programme_not_available_flag"])

    response_dict["college"] = college 
    response_dict["degree"] = degree
    response_dict["degreetype"] = degreetype if degreetype != "d" else ""
    response_dict["course"] = course if course != "d" else ""
    response_dict["category"] = category.upper() if category.upper() != "UR" else "Unreserved"
    response_dict["seats"] =str(query_results)

    file_5.seek(0)
    next(reader5)

    file_6.seek(0)
    next(reader6)
    
    return response_dict
