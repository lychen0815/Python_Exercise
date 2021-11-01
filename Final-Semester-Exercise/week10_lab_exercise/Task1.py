def linear_search_tuples(a_list,query):
    for index, element in a_list:
        if element == query:
            return True
    return False

print(linear_search_tuples([(1,'a'),(2,'c'),('abc','ee')],'c'))
print(linear_search_tuples([(1,'a'),(2,'c'),('abc','ee')],'abc'))

