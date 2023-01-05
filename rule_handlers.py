# frofaculty_department_collegem utils import invalid_query_prompt #,bot_print_with_name, bot_print
import random
import csv

# path_1 = "C:\du_chatbot_terminal\data\college_course_category_seats.csv"
path_1 = "data\college_course_category_seats.csv"
file_1 = open(path_1, newline = '')
reader1 = csv.reader(file_1)
header1 = next(reader1)

# path_2 = "C:\du_chatbot_terminal\data\\faculty_department.csv"
path_2 = "data\\faculty_department.csv"
file_2 = open(path_2, newline = '')
reader2 = csv.reader(file_2)
header2 = next(reader2)

# path_3 = "C:\du_chatbot_terminal\data\college_course.csv"
path_3 = "data\college_course.csv"
file_3 = open(path_3, newline = '')
reader3 = csv.reader(file_3)
header3 = next(reader3)

# path_4 = "C:\du_chatbot_terminal\data\college_course_category_coursefee.csv"
path_4 = "data\college_course_category_coursefee.csv"
file_4 = open(path_4, newline = '')
reader4 = csv.reader(file_4)
header4 = next(reader4)

# path_5 = "C:\du_chatbot_terminal\data\master_data.csv"
path_5 = "data\master_data.csv"
file_5 = open(path_5, newline = '')
reader5 = csv.reader(file_5)
header5 = next(reader5)

# path_6 = "C:\du_chatbot_terminal\data\degree_degreetype_link.csv"
path_6 = "data\degree_degreetype_link.csv"
file_6 = open(path_6, newline = '')
reader6 = csv.reader(file_6)
header6 = next(reader6)

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


# def check_programme_exists_at_college():
#     pass

#1
def get_number_of_colleges_in_university  (query_dict): 
    colleges_set = set()

    for row in reader5:
        colleges_set.add(row[0].strip().title())
        # print(row[0])

    response_dict = dict()
    response_dict["colleges_set"] = colleges_set
    response_dict["no_of_college"] = len(colleges_set)

    file_5.seek(0)
    next(reader5)

    return response_dict
    
#2
def get_number_of_faculties_in_university (query_dict): 
    faculties_set = set()
    for row in reader2:
        faculties_set.add(row[0].strip().title())

    response_dict = dict()
    response_dict["faculties_set"] = faculties_set
    response_dict["no_of_faculties"] = len(faculties_set)

    file_2.seek(0)
    next(reader2)

    return response_dict

#3
def get_number_of_departments_in_university(query_dict): 

    departments_set = set()
    for row in reader2:
        departments_set.add(row[1].strip().title())
    
    response_dict = dict()
    response_dict["departments_set"] = departments_set
    response_dict["no_of_departments"] = len(departments_set)
   
    file_2.seek(0)
    next(reader2)

    return response_dict

#4
def get_number_of_programmes_in_university(query_dict):

    programmes_set = set()
    for row in reader5:
        programme = row[1].strip() + " " + row[2].strip() + " " + row[3].strip() 
        programmes_set.add(programme.title())

    response_dict = dict()
    response_dict["programmes_set"] = programmes_set
    response_dict["no_of_programmes"] = len(programmes_set)
      
    file_5.seek(0)
    next(reader5)

    return response_dict

#5
def get_number_of_faculties_in_college(query_dict):
    print("get_number_of_faculties_in_college is called")
    # college = query_dict['college']
    # message_for_query_to_be_searched = "number of faculties in " + college
    # if bot_confirmation_prompt(message_for_query_to_be_searched):
    #     query_results = 5
    #     generated_response = "There are " + str(query_results) + " faulties at " + college
    #     return generated_response
    # else:
    #      return  
    # discuss the idea;; the method is in utils
    return "No faculty exists in college"

#6
def get_total_number_of_seats_for_degree_degreetype_course_at_college(query_dict):
# _programme
    college = query_dict['college'].lower()
    degree = query_dict['degree'].lower()
    degreetype = query_dict['degreetype'].lower()
    course = query_dict['course'].lower()

    response_dict = dict()
    response_dict["programme_not_available_flag"] = False
    response_dict["ba_program_flag"] = False
    response_dict["link"] = str()
    query_results = int()

    # # print("yes1")
    # if degree == "b.a." and degreetype == "program":
    #     for r in reader6:
    #         # print("yess")
    #         if r[0].strip()=="b.a." and r[1].strip() == "program":
    #             response_dict["link"] = r[2].strip()
    #     # print(response_dict["link"])
    query_results = 0

    for row in reader5:
        if row[0].strip() == college :
            if row[1].strip() == degree and row[2].strip() == degreetype and row[3].strip() == course :
                if degree == "b.a." and degreetype == "program":
                    for r in reader6:
                        if r[0].strip()=="b.a." and r[1].strip() == "program":
                            response_dict["link"] = r[2].strip()
                            # print(r[2].strip())
                            # print(response_dict["link"])
                            response_dict["ba_program_flag"] = True
                            # print("baprogram yes", response_dict["ba_program_flag"])     
                            # save_iterator_
                else:    
                    query_results = int(row[11].strip())
                    # print(query_results)
                    # print("yes")
                    
    if query_results == 0:
        response_dict["programme_not_available_flag"] = True 
        # print(response_dict["programme_not_available_flag"])

       
    response_dict["college"] = college
    response_dict["degree"] = degree
    response_dict["degreetype"] = degreetype if degreetype != "d" else ""
    response_dict["course"] = course if course != "d" else ""
    response_dict["total seats"] = str(query_results)

    # print(response_dict, "ok")

    file_5.seek(0)
    next(reader5)

    file_6.seek(0)
    next(reader6)

    return response_dict
    
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
    response_dict["ba_program_flag"] = False
    response_dict["link"] = str()
    query_results = int()
       
    query_results = 0
    
    # for i in range(11,17):
    category_index_from_csv = header5.index(category) + 8
    # print(category_index_from_csv)

    for row in reader5:
        if row[0].strip() == college :
            if row[1].strip() == degree and row[2].strip() == degreetype and row[3].strip() == course :
                if degree == "b.a." and degreetype == "program":
                    for r in reader6:
                        if r[0].strip()=="b.a." and r[1].strip() == "program":
                            response_dict["link"] = r[2].strip()
                            # print(r[2].strip())
                            # print(response_dict["link"])
                            response_dict["ba_program_flag"] = True
                            print("baprogram yes", response_dict["ba_program_flag"])
                else:
                    query_results = int(row[category_index_from_csv].strip())
                    print(query_results)

    if query_results == 0 and response_dict["ba_program_flag"] == False:
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
    
#8
def get_number_of_programmes_at_college(query_dict):
    # if query_dict['entity'] == 'course' :
    college = query_dict['college'].lower()
    programmes_at_college_set = list()

    for row in reader5:
        if row[0] == college:
            programme = "{} {} {}".format(row[1].strip(),row[2].strip(),row[3].strip()).title()
            if programme not in programmes_at_college_set:
                programmes_at_college_set.append(programme)

    query_results = len(programmes_at_college_set)

    response_dict = dict()
    response_dict["college"] = college
    response_dict["programme_set"] = programmes_at_college_set
    response_dict["no_of_programmes_at_college_set"] = query_results

    file_5.seek(0)
    next(reader5)   

    return response_dict
    # else :
    #     get_number_of_colleges_offering_course(query_dict)


#9
def get_number_of_programmes_in_faculty(query_dict):
    # faculty = query_dict['faculty']    

    # path = "D:\\new_chat\\new_n\\faculty_course.csv"
    # file = open(path, newline = '')
    # reader = csv.reader(file)
    # header = next(reader)

    # courses_at_faculty_set = set()
    # for row in reader:
    #     if row[0].lower() == faculty.lower():
    #         courses_at_faculty_set.add(row[2])

    
    # query_results = len(courses_at_faculty_set) 
    #pass facultyname #logic to count total no. course faculty; from the csv, --> available doc ?

    # possible_responses = ["There are {no_of_courses} courses at {ffaculty}", "There are {no_of_courses} courses at {ffaculty}", "{no_of_courses} courses at {ffaculty}"]
    # generated_response = (random.choice(possible_responses)).format(no_of_courses = query_results, ffaculty = faculty )  

    # return generated_response
    return "data is not available"

#10
def get_number_of_courses_in_department(query_dict):
    # department = query_dict['department']    

    # reader = csv.reader(file_) # DEPARTMENT _ COURSE
    # header = next(reader)

    # courses_in_department_set = set()
    # for row in reader:
    #     if row[1].lower() == department.lower():
    #         courses_in_department_set.add(row[2])

    # query_results = len(courses_in_department_set) #pass college name #logic to count total no. course at a college  ; from the csv, --> available doc no of courses per college with vcategoruy wise fee

    # possible_responses = ["There are {no_of_courses} courses offered by {ddepartment}", "There are {no_of_courses} courses at {ddepartment}", "{no_of_courses} courses at {ddepartment}"]
    # generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department )  

    # return generated_response
    return "data is not available"

#11
def get_number_of_programmes_in_department_at_college(query_dict):
    # college level department
    # to be discussed college level detail 
    # college = query_dict['college']
    # department = query_dict['department']    

    # query_results = 11 #pass collegename and dept name #logic to count total no. course at a college  ; from the csv, --> available doc no of courses per college with vcategoruy wise fee
   
    # possible_responses = ["There are {no_of_courses} courses offered by {ddepartment} at {ccollege}.", "There are {no_of_courses} courses at {ddepartment} at {ccollege}.", "{no_of_courses} courses at {ddepartment} at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department, ccollege = college )  

    # return generated_response
    return "college level detail ... will be updated soon"

#12
def get_number_of_department_at_college(query_dict):
    # college level department
    #college level detail
    # create college dept document;
    # college = query_dict['college']

    # query_results = 12 #pass college name #logic to count total no. departments at a college  ; from the csv, --> available doc no of courses per college with category wise fee
   
    # possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    # return generated_response
    return "college level detail ... will be updated soon"

#13
def get_number_of_department_under_faculty_at_college(query_dict):    
 #clear
    # list of department at college level needs to be categorized faculty wise
    # faculty = query_dict['faculty']
    # college = query_dict['college']

    # query_results = 13 #pass faculty, department name #logic to count total no. departments at a college  ; from the csv, --> available doc no of courses per college with category wise fee
   
    # possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    # return generated_response
    return "college level detail ... will get updated soon"

#14
def get_number_of_department_under_faculty(query_dict):
    # faculty = query_dict['faculty']

    # department_under_faculty_set = set()
    # for row in reader2:
    #     if row[0].lower() == faculty.lower():
    #         department_under_faculty_set.add(row[1].strip().title())    

    # response_dict = dict()

    # response_dict["faculty"] = faculty
    # response_dict["department_under_faculty_set"] = department_under_faculty_set

    # file_2.seek(0)
    # next(reader2)

    # return response_dict
    pass

#15
def get_number_of_colleges_offering_degree_degreetype_course(query_dict):
    # if query_dict['entity'] == 'college':
    degree = query_dict['degree'].lower()
    degreetype = query_dict['degreetype'].lower()
    course = query_dict['course'].lower()
    
    colleges_offering_programme_set = set()

    for row in reader5:
        if row[1].strip() == degree and row[2].strip() == degreetype and row[3].strip() == course :
            colleges_offering_programme_set.add(row[0])
    
    print(len(colleges_offering_programme_set))
    response_dict = dict()
    programme = "{} {} {}".format(degree.strip().title(),degreetype.strip().lower(),course.strip().title())
    response_dict["programme"] = programme
    response_dict["colleges_offering_programme_set"] = colleges_offering_programme_set

    file_5.seek(0)
    next(reader5)

    return response_dict
# else:
#     get_number_of_courses_at_college(query_dict)


#16
def get_list_of_faculties_in_college(query_dict):
    # faculties at college
    # pass
    # return generated_response
    return "There's no faculty in a college"

#17
def get_list_of_colleges_in_university(query_dict):

    colleges_set = list()
    for row in reader5:
        if row[0].strip().title() not in colleges_set:
            colleges_set.append(row[0].strip().title())
        # print(row[0])
    
    response_dict = dict()
    response_dict["college_set"] = colleges_set

    file_5.seek(0)
    next(reader5)

    return response_dict

#18
def get_list_of_faculties_in_university(query_dict):

    faculties_set = list()
    for row in reader2:
        if row[0].strip().title() not in faculties_set:
            faculties_set.append(row[0].strip().title())   

    response_dict = dict() 
    response_dict["faculties_set"] = faculties_set

    file_2.seek(0)
    next(reader2)

    return response_dict

#19
def get_list_of_departments_in_university(query_dict):

    departments_set = list()
    for row in reader2:
        if row[1].strip().title() not in departments_set and row[1].strip().title() != "No Dept":
            departments_set.append(row[1].strip().title())

    response_dict = dict() 
    response_dict["departments_set"] = departments_set

    file_2.seek(0)
    next(reader2)

    return response_dict

#20
def get_list_of_programmes_in_university(query_dict):
    programmes_set = set()
    for row in reader5:
        programme = "{} {} {}".format(row[1].strip().title(),row[2].strip().lower() if row[2].strip().lower() != "d" else "",row[3].strip().title()  if row[3].strip().title() != "D" else "")
        programmes_set.add(programme.title())
        # programme = "{} {} {}".format(degree.strip().title(),degreetype.strip().lower() if degreetype != "d" else "",course.strip().title() if course != "d" else "")

   
    response_dict = dict()
    response_dict["programmes_set"] = programmes_set
      
    file_5.seek(0)
    next(reader5)

    return response_dict    

#21
def get_list_of_programmes_at_college(query_dict):
# if query_dict['entity'] == 'course':  
    college = query_dict['college'].lower()
    programmes_at_college_set = list()

    for row in reader5:
        if row[0] == college:
            # programme = "{} {} {}".format(row[1].strip().title(),row[2].strip().lower(),row[3].strip().title())
            programme = "{} {} {}".format(row[1].strip().title(),row[2].strip().lower() if row[2].strip().lower() != "d" else "",row[3].strip().title()  if row[3].strip().title() != "D" else "")
            if programme not in programmes_at_college_set:
                programmes_at_college_set.append(programme)

    response_dict = dict()
    response_dict["college"] = college
    response_dict["programme_set"] = programmes_at_college_set

    file_5.seek(0)
    next(reader5)   

    return response_dict
#    else : 
#     get_list_of_colleges_offering_course(query_dict)


#22
def get_list_of_programmes_in_faculty(query_dict):
    # faculty = query_dict['faculty']    

    # path = "D:\\new_chat\\new_n\\faculty_course.csv"
    # file = open(path, newline = '')
    # reader = csv.reader(file)
    # header = next(reader)

    # courses_at_faculty_set = set()
    # for row in reader:
    #     if row[0].lower() == faculty.lower():
    #         courses_at_faculty_set.add(row[2])

    
    # query_results = len(courses_at_faculty_set) 
    #pass facultyname #logic to count total no. course faculty; from the csv, --> available doc ?

    # possible_responses = ["There are {no_of_courses} courses at {ffaculty}", "There are {no_of_courses} courses at {ffaculty}", "{no_of_courses} courses at {ffaculty}"]
    # generated_response = (random.choice(possible_responses)).format(no_of_courses = query_results, ffaculty = faculty )  

    # return generated_response
    return (random.choice("data is not available", "data will be availavble soon ..."))

#23
def get_list_of_programmes_in_department(query_dict):
    # department = query_dict['department']    


    # reader = csv.reader(file_2)  DEPARTMETN - COURSE
    # header = next(reader)

    # courses_in_department_set = set()
    # for row in reader:
    #     if row[1].lower() == department.lower():
    #         courses_in_department_set.add(row[2])

    # query_results = len(courses_in_department_set) #pass college name #logic to count total no. course at a college  ; from the csv, --> available doc no of courses per college with vcategoruy wise fee

    # possible_responses = ["There are {no_of_courses} courses offered by {ddepartment}", "There are {no_of_courses} courses at {ddepartment}", "{no_of_courses} courses at {ddepartment}"]
    # generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department )  

    # return generated_response
    return "data is not available"

#24
def get_list_of_programmes_in_department_at_college(query_dict):
    # college level department
    # to be discussed college level detail 
    # college = query_dict['college']
    # department = query_dict['department']    

    # query_results = 11 #pass collegename and dept name #logic to count total no. course at a college  ; from the csv, --> available doc no of courses per college with vcategoruy wise fee
   
    # possible_responses = ["There are {no_of_courses} courses offered by {ddepartment} at {ccollege}.", "There are {no_of_courses} courses at {ddepartment} at {ccollege}.", "{no_of_courses} courses at {ddepartment} at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department, ccollege = college )  

    # return generated_response
    return "college level detail ... will be updated soon"

#25
def get_list_of_department_at_college(query_dict):
    # college level department
    #college level detail
    # create college dept document;
    # college = query_dict['college']

    # query_results = 12 #pass college name #logic to count total no. departments at a college  ; from the csv, --> available doc no of courses per college with category wise fee
   
    # possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    # return generated_response
    return "college level detail ... will be updated soon"

#26
def get_list_of_department_under_faculty_at_college(query_dict):
    #clear
    # list of department at college level needs to be categorized faculty wise
    # faculty = query_dict['faculty']
    # college = query_dict['college']

    # query_results = 13 #pass faculty, department name #logic to count total no. departments at a college  ; from the csv, --> available doc no of courses per college with category wise fee
   
    # possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    # return generated_response
    return "college level detail ... will be updated soon"

#27
def get_list_of_department_under_faculty(query_dict):
    
#     faculty = query_dict['faculty']

#     department_under_faculty_set = set()
#     for row in reader2:
#         if row[0].lower() == faculty.lower():
#             department_under_faculty_set.add(row[1].strip().title())    

#     response_dict = dict()
#     response_dict["faculty"] = faculty
#     response_dict["department_under_faculty_set"] = department_under_faculty_set   

#     file_2.seek(0)
#     next(reader2)

#     return response_dict
    pass

#28
def get_list_of_colleges_offering_degree_degreetype_course(query_dict):
    degree = query_dict['degree'].lower()
    degreetype = query_dict['degreetype'].lower()
    course = query_dict['course'].lower()
    
    colleges_offering_programme_set = set()

    for row in reader5:
        if row[1].strip() == degree and row[2].strip() == degreetype and row[3].strip() ==  course :
            colleges_offering_programme_set.add(row[0])
    
    response_dict = dict()
    programme = "{} {} {}".format(degree.strip().title(), degreetype.strip().lower() if degreetype != "d" else "",course.strip().title() if course != "d" else "")
    response_dict["programme"] = programme
    response_dict["colleges_offering_programme_set"] = colleges_offering_programme_set

    file_5.seek(0)
    next(reader5)
    # if query_dict['entity'] == 'college':
    # else:
    #     get_list_of_courses_at_college(query_dict)
    return response_dict


#29
def get_cutoff_for_category_for_degree_degreetype_course_college(category, course, college):
    pass 


#30
def get_cutoff_for_degree_degreetype_course_for_college( course, college):
    pass

#31
def get_coursefee_for_category_for_degree_degreetype_course_college(query_dict):
    college = query_dict['college'].lower()
    degree = query_dict['degree'].lower()
    degreetype = query_dict['degreetype'].lower()
    course = query_dict['course'].lower()
    category = query_dict['category'].lower()
    response_dict = dict()
    query_results = int()
    category_index_from_csv = header5.index(category)

    # if 
    for row in reader5:
        if row[0].strip() == college and row[1].strip() == degree and row[2].strip() == degreetype and row[3].strip() == course :
            query_results = int(row[category_index_from_csv])

    response_dict["coursefee"] = query_results

    # programme = "{} {} {}".format(degree.strip().title(), degreetype.strip().lower(), course.strip().title())
    programme = "{} {} {}".format(degree.strip().title(), degreetype.strip().lower() if degreetype != "d" else "", course.strip().title() if course != "d" else "")

    response_dict["college"] = college.title()
    response_dict["programme"] = programme.strip()
    response_dict["category"] = category.upper() if category.upper() != "UR" else "Unreserved"
    file_5.seek(0)
    next(reader5)

    return response_dict
    
#32
# def get_details_for_eligibility_of_degree_degreetype_course(query_dict):
#     degree = query_dict['degree'].lower()
#     degreetype = query_dict['degreetype'].lower()
#     course = query_dict['course'].lower()
    
#     response_dict = dict()

#     for row in reader6:
#         if row[0].strip() == degree and row[1].strip() == degreetype:
#             response_dict["link"] = row[2].strip()
    
#     programme = "{} {} {}".format(degree.strip().title(), degreetype.strip().lower(), course.strip().title())

#     response_dict["programme"] = programme             
#     return response_dict 

# #33
# def get_details_for_duration_of_degree_degreetype_course(query_dict):
#     degree = query_dict['degree'].lower()
#     degreetype = query_dict['degreetype'].lower()
#     course = query_dict['course'].lower()
    
#     response_dict = dict()

#     for row in reader6:
#         if row[0].strip() == degree and row[1].strip() == degreetype:
#             response_dict["link"] = row[2].strip()
    
#     # programme = "{} {} {}".format(degree.strip().title(), degreetype.strip().lower(), course.strip().title())
#     programme = "{} {} {}".format(degree.strip().title(),degreetype.strip().lower() if degreetype != "d" else "",course.strip().title() if course != "d" else "")
    
#     response_dict["programme"] = programme             
#     return response_dict 
     

# def get_details_for_syllabus_of_degree_degreetype_course(query_dict):
#     degree = query_dict['degree'].lower()
#     degreetype = query_dict['degreetype'].lower()
#     course = query_dict['course'].lower()
    
#     response_dict = dict()

#     for row in reader6:
#         if row[0] == degree and row[1] == degreetype:
#             print("yes")
#             response_dict["link"] = row[2].strip()
    
#     programme = "{} {} {}".format(degree.strip().title(), degreetype.strip().lower(), course.strip().title())
    
#     response_dict["programme"] = programme             
#     return response_dict 

#32
def get_details_for_degree_degreetype_course(query_dict):
    degree = query_dict['degree'].lower()
    degreetype = query_dict['degreetype'].lower()
    course = query_dict['course'].lower()
    
    response_dict = dict()

    for row in reader6:
        if row[0].strip() == degree and row[1].strip() == degreetype:
            response_dict["link"] = row[2].strip()
    
    # programme = "{} {} {}".format(degree.strip().title(), degreetype.strip().lower(), course.strip().title())
    programme = "{} {} {}".format(degree.strip().title(),degreetype.strip().lower() if degreetype != "d" else "",course.strip().title() if course != "d" else "")

    # print(response_dict["link"])  
    response_dict["programme"] = programme 
    response_dict["details"] = query_dict["details"]           
    
    file_6.seek(0)
    next(reader6)
    
    return response_dict 


#33
def get_number_of_programme_under_degree(query_dict):
    degree = query_dict['degree'].lower() 

    response_dict = dict()
    programme_under_degree_set = set()

    for row in reader5:
        if row[1].lower().strip() == degree:
            print(row[1])
            programme = "{} {} {}".format(row[1].strip().title(), row[2].strip().lower() if row[2].lower().strip() != "d" else "",row[3].strip().title() if row[3].strip().lower() != "d" else "")
            programme_under_degree_set.add(programme)

    response_dict["programme_set"] = programme_under_degree_set 
    response_dict["degree"] = degree
    # print(response_dict["programme_set"])

    file_5.seek(0)
    next(reader5)
    
    return response_dict  

#34
def get_list_of_programme_under_degree(query_dict):
    degree = query_dict['degree'].lower() 

    response_dict = dict()
    programme_under_degree_set = set()

    for row in reader5:
        if row[1].lower().strip() == degree:
            programme = "{} {} {}".format(row[1].strip().title(), row[2].strip().lower() if row[2].lower().strip() != "d" else "",row[3].strip().title() if row[3].strip().lower() != "d" else "")
            programme_under_degree_set.add(programme)

    response_dict["programme_set"] = programme_under_degree_set 
    response_dict["degree"] = degree
    # print(response_dict["programme_set"])

    file_5.seek(0)
    next(reader5)
    
    return response_dict  




#35
def get_number_of_programme_under_degreetype(query_dict):
    degreetype = query_dict['degreetype'].lower() if query_dict['degreetype'].lower() != "d" else ""

    response_dict = dict()
    programme_under_degree_set = set()

    for row in reader5:
        if row[2].lower().strip() == degreetype:
            programme = "{} {} {}".format(row[1].strip().title(), row[2].strip().lower() if row[2].lower().strip() != "d" else "",row[3].strip().title() if row[3].strip().lower() != "d" else "")
            programme_under_degree_set.add(programme)

    response_dict["programme_set"] = programme_under_degree_set
    response_dict["degreetype"] = degreetype
    # print(response_dict["programme_set"])

    file_5.seek(0)
    next(reader5)
    
    return response_dict  


#36
def get_list_of_programme_under_degreetype(query_dict):
    degreetype = query_dict['degreetype'].lower() if query_dict['degreetype'].lower() != "d" else ""
    response_dict = dict()
    programme_under_degree_set = set()

    for row in reader5:
        if row[2].lower().strip() == degreetype:
            programme = "{} {} {}".format(row[1].strip().title(), row[2].strip().lower() if row[2].lower().strip() != "d" else "",row[3].strip().title() if row[3].strip().lower() != "d" else "")
            programme_under_degree_set.add(programme)

    response_dict["programme_set"] = programme_under_degree_set 
    response_dict["degreetype"] = degreetype

    file_5.seek(0)
    next(reader5)
    
    return response_dict  

    

#37
def get_number_of_programme_under_degree_degreetype(query_dict):
    degreetype = query_dict['degreetype'].lower() if query_dict['degreetype'].lower() != "d" else ""
    degree = query_dict['degree'].lower() 

    response_dict = dict()
    programme_under_degree_set = set()

    for row in reader5:
        if row[1].lower().strip() == degree and row[2].lower().strip() == degreetype:
            programme = "{} {} {}".format(row[1].strip().title(), row[2].strip().lower() if row[2].lower().strip() != "d" else "",row[3].strip().title() if row[3].strip().lower() != "d" else "")
            programme_under_degree_set.add(programme)

    response_dict["programme_set"] = programme_under_degree_set 
    response_dict["degreetype"] = degreetype
    response_dict["degree"] = degree

    file_5.seek(0)
    next(reader5)
    
    return response_dict  


#38
def get_list_of_programme_under_degree_degreetype(query_dict):
    degreetype = query_dict['degreetype'].lower() if query_dict['degreetype'].lower() != "d" else ""
    degree = query_dict['degree'].lower()

    response_dict = dict()
    programme_under_degree_set = set()

    for row in reader5:
        if row[1].lower().strip() == degree and row[2].lower().strip() == degreetype:
            programme = "{} {} {}".format(row[1].strip().title(), row[2].strip().lower() if row[2].lower().strip() != "d" else "",row[3].strip().title() if row[3].strip().lower() != "d" else "")
            programme_under_degree_set.add(programme)

    response_dict["programme_set"] = programme_under_degree_set 
    response_dict["degreetype"] = degreetype
    response_dict["degree"] = degree

    file_5.seek(0)
    next(reader5)
    
    return response_dict  

#39
def get_availability_of_programme_in_college(query_dict):
    pass
    
#40
def get_availability_of_degree_in_college(query_dict):
    pass

#41
def get_availability_of_degree_degreetype_in_college(query_dict):
    pass