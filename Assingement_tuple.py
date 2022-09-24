#     Write a Python program to get a list, sorted in 
# increasing order by the last element in each tuple from a given 
# list of non-empty tuples


# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 


def return_last_element(tuple_item):
    return tuple_item[-1]

Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Sample_List_sec = sorted(Sample_List,key=return_last_element)
print("Expected Result :-",Sample_List_sec )


# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]