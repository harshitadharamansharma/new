import csv

path = "C:\du_chatbot_terminal\data\college_course_category_coursefee.csv"
file = open(path, newline = "")
reader1 = csv.reader(file)
# header = next(reader1)
a = list()

for r in reader1:
    # if r[1] not in a:
    #     a.append(r[1])
    print(r[2])
    # print(', '.join(r[0]))


# print(a)
# print(len(a))

