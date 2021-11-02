def find_student_grade(inputFile1,inputFile2,outputFile):
    student_info = {}

    with open(inputFile1) as file1:
        for line in file1.readlines():
            line = line.strip()
            new_line = line.split(' ')
            student_info[new_line[0]] = new_line[1]
        list1 = [[x,y] for x,y in student_info.items()]
        for i in range(len(list1)):
            list1[i].insert(1,inputFile1)

        with open(inputFile2) as file2:
            for line in file2.readlines():
                line = line.strip()
                new_line = line.split(" ")
                if new_line[0] in student_info.keys():
                    for student in list1:
                        if new_line[0] == student[0]:
                            student[2] = (int(student[2]) + int(new_line[1]))//2
                            student.insert(2,inputFile2)
        out_info = ""
        for element in list1:
            for idx in range(len(element)):
                if idx == len(element)-1:
                    out_info += str(element[idx])
                else:
                    out_info += str(element[idx]) + ","

            out_info += "\n"
        with open(outputFile,'w') as file3:
            file3.write(out_info)



find_student_grade("FIT9136.txt","FIT9133.txt","output.txt")