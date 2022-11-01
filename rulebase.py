rulebase = {
    1: {
        "rule_format": "degree_course_college",
        "rule_handler": get_courses_for_degree_in_college
    
    },
    2: {
        "rule_format": "seatmatrix_degree_course_college",
        "rule_handler": "get_seatmatrix_for_degree_in_college",
        #DIFFERENT METHODS TO GET :- 1.TOTAL SEATS; 2.CATEGORY WISE SEATS; 3.
    }
#     3: {
#         "rule_format": "degree_course_college_",
#         "rule_handler": "get_seatmatrix_courses_for_degree_in_college",
        
#     }
#     4: {
#         "rule_format": "degree_course_college_SC",
#         "rule_handler": "get_seatmatrix_courses_for_degree_in_college",
#     }
}