
tests = ['126','371','118']
with open("test.txt",'w') as f:
    f.write('\n'.join(tests))


def checkArmstrong(filename):

    with open(filename) as file:

        for line in file.readlines():
            line = line.strip()
            digits_total = 0
            the_number = int(line)

            for digit in line:
                digits_total += int(digit) ** 3

            if digits_total == the_number:
                print(True)
            else:
                print(False)


checkArmstrong("test.txt")