def file_process(infile, outfile):
    input_str = ''
    with open(infile) as input_file:
        for line in input_file:
            line = line.strip()
            new_line = line.split(" ")
            for i in new_line:
                input_str += i.title() + "\n"
    with open(outfile,'w') as output_file:
        output_file.write(input_str)
file_process('input.txt','output.txt')