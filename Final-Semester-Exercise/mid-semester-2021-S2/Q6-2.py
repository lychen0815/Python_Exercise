secret_codes = [
('A',	'AB'),
('B',	'2A'),
('C',	'B21'),
('D',	'BAB'),
('E',	'BA1'),
('F',	'AA'),
('G',	'11'),
('H',	'21'),
('I',	'B12'),
('J',	'B2A'),
('K',	'BB1'),
('L',	'BBA'),
('M',	'1A'),
('N',	'A2'),
('O',	'B1B'),
('P',	'BAA'),
('Q',	'A1'),
('R',	'1B'),
('S',	'B1A'),
('T',	'B2B'),
('U',	'BB2'),
('V',	'BA2'),
('W',	'2B'),
('X',	'B11'),
('Y',	'B22'),
('Z',	'22'),
(' ',	'12')
]

def decode_mi6():
    user_input = input("Please enter code: ")
    if set(user_input) - set('12AB'):
        print('Invalid code')
    else:
        code_dict = {v : k for k,v in secret_codes}

        current_substr = ''
        decoded_str = ''
        for char in user_input:
            current_substr += char
            if current_substr in code_dict:
                decoded_str += code_dict[current_substr]
                current_substr = ''
        if current_substr:
            print('Invalid code!')
        else:
            print('The decoded String is: ',decoded_str)



decode_mi6()

