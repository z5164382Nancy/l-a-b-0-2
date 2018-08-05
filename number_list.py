def find_reverse(numbers):
    return list(reversed(numbers))
    pass

def find_max(numbers):
    return sorted(numbers)[-1]
    pass

def find_min(numbers):
    return sorted(numbers)[0]
    pass

def find_sum(numbers):
    return sum(numbers)
    pass

def find_average(numbers):
    return sum(numbers)/len(numbers)
    pass

def find_descending(numbers):
    return sorted(numbers, reverse = True)
    pass

def second_smallest(numbers):
    return sorted(set(numbers))[1]
    pass


'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    return sorted(set(numbers))[k-1]
    pass
