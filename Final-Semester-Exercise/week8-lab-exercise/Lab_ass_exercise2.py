'''
2. insert_dictionary
Write a function insert_dictionary(): which accepts 3 arguments:

a_dictionary: a dictionary

a_key: a string

a_value: an integer

The function adds the key-value pair({a_key: a_value}) to a_dictionary.

If the key is present in the dictionary, do not update the value. Instead print "Key present".

Furthermore, if any of the parameters are not valid, the function should raise an exception and show an appropriate message.

You may apply any kind of error handling techniques learnt so far.
'''

def insert_dictionary(a_dictionary, a_key, a_value):
    if not(type(a_dictionary) is dict):
        raise TypeError('a_dictionary is not a dictionary')
    if not(type(a_key) is str):
        raise TypeError('a_key is not a string')
    if not(type(a_value) is int):
        raise TypeError('a_value is not a integer')
    if (a_key in a_dictionary):
        print('Key present')
    else:
        a_dictionary[a_key] = a_value

print(insert_dictionary({'a':1,'b':2},'a',1))






























