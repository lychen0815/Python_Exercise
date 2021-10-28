"""
You are given a file 'input.txt' in the following format:

This is a sentence.
This is another sentence.
Please write a function def file_process(infile, outfile): that reads the input file with the argument infile as the input filename and create a new file with the filename provided by the argument outfile that stores every word(capitalized) from the input file in separate lines, following the format below:

This
Is
A
Sentence.
This
Is
Another
Sentence.
You may assume every word is split by white space character only.
"""
output_list = []
def file_process(infile, outfile):
    with open(infile) as file:
        for line in file.readlines():
            line = line.strip()
            new_list = line.split(" ")
            for i in new_list:
                output_list.append(i.capitalize())
    output_new_list = "\n".join(output_list)
    with open(outfile,'w') as f:
        f.write(str(output_new_list))
file_process("input.txt","output.txt")