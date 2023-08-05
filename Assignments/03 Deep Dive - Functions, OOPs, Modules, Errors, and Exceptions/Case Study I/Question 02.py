"""
Data of XYZ company is stored in the sorted list. Write a program for searching 
specific data from that list.
"""

"""
Note:
As question is too vague and no type of data is specified in the question and,
mentioned that the list is sorted, taking following assumptions:
    sorted list => int list
    type of data to search => int
    algorithm => Binary Search
"""

def search_data(lst, search_item):
    """Searches for the data in the given list

    Args:
        lst (iterable): Sorted data collection
        search_item (int): Item to search

    Returns:
        int: Index if exists else -1
    """    

    low, high, mid = 0, (len(lst) - 1), 0
    
    while low <= high:
        mid = (low + high) // 2
        if search_item > lst[mid]:
            low = mid + 1
        elif search_item < lst[mid]:
            high = mid - 1
        else:
            return mid
        
    return -1


if __name__ == '__main__':
    index = search_data([1,2,3,4,5], 5)
    if index >= 0:
        print("Data present at index:", index)
    else:
        print("Data does not exists.")