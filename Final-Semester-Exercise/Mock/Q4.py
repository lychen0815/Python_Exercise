"""
Q4 : This question is about File I/0.
"""

def find_student_grade(inputFile1,inputFile2):
    all_student = []
    new_students = []
    with open(inputFile1) as input_file1:
        for line in input_file1:
            line = line.strip()
            student_info = line.split(" ")
            student_info.append('FIT9136')
            all_student.append(student_info)
    with open(inputFile2) as input_file2:
        for line in input_file2:
            line = line.strip()
            student_info = line.split(" ")
            student_info.append('FIT9133')
            all_student.append(student_info)

    for each_student in all_student:
        ID = each_student[0]
        mark = each_student[1]
        subject = each_student[2]
        total_mark = 0
        mark_num = 0
        total_subject = ""
        if ID not in new_students:
            new_students.append(ID)
            total_subject += subject
            new_students.append(total_subject)
            new_students.append(mark)

        else:
            total_mark += int(mark)
            mark_num += 1
            total_subject += subject
            avg_mark = total_mark // mark_num
            new_students.append(ID)
            new_students.append(total_subject)
            new_students.append(avg_mark)

    print(new_students)

    #print(all_student)

find_student_grade("FIT9136.txt","FIT9133.txt")

