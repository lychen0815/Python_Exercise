#Lab Activity A
#1.Flight Info System


# Destination
destinations = [
    'Melbourne',
    'Sydney',
    'Brisbane',
    'Adelaide',
    'Perth',
    'Darwin',
    'Canberra',
    'Hobart',
    'Cairns',
    'Townsville',
    'Auckland',
    'Wellington',
    'Christchurch',
    'Queenstown',
    'London Heathrow',
    'New York JFK',
    'Tokyo Narita'
]

# Carrier discription
carrier_dic = {
    'QF': 'Qantas',
    'VA': 'Virgin Australia',
    'CX': 'Cathay Pacific',
    'JL': 'Japan Airlines',
    'BA': 'British Airways'
}


while True:
    # let user input flight code
    flight_code = input("Please enter flight code:")

    # Eliminates spaces in the head and tail when entered by the user
    flight_code = flight_code.strip()

    # Check the length of the string and whether there is a space in string or not
    if ' ' in flight_code and 6 <= len(flight_code) <= 7:
        # Eliminates space inside the string
        # And check to see if the string is made up of numbers and letters
        if flight_code.replace(' ','').isalnum():
            break
        else:
            pass
    else:
        print("You need enter a space after carrier code(like after'VA')!!!")
        pass

#get the carrier and destination
carrier = flight_code.split()[0]
flight_number = flight_code.split()[1]

#flight number need to divided by 17 and get destination code
destination_code = int(flight_number) % 17

# check the carrier is valid or not
if carrier in carrier_dic.keys():
    carrier_name = carrier_dic[carrier]
    print("Flight " + str(flight_code) + " is operated by " + str(carrier_name) + " flying to " + destinations[destination_code] + ".")
else:
    print("Invalid flight code.")
