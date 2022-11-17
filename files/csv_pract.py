import csv
    
with open('abc.csv', 'r') as csv_college_course_category_fee:
    csv_college_course_category_fee = csv.reader(csv_college_course_category_fee)

    for line in csv_college_course_category_fee:
        print(line)
