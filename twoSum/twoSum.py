arr1 = [2, 7, 11, 15]
target1 = 9

arr2 = [1, 2, 3, 4]
target2 = 17

#define a function that will go over these two target
def two_sum(arr, target):

    # store values in a dictionary
    values = dict()

    # elem looks for the item in the start of the list and returns its index
    for i, elem in enumerate(arr):
        # complement is the target minus the element in the array
        comp = target - elem
        #if the complement is in the values dictionary
        if comp in values:
            #return the values in the dictionary complement and the index
            return [values[comp], i]

        values[elem] = i

    return []

list1 = two_sum(arr2, target2)
print(list1)
# outuput [0, 1]
# select two values from the array that will add up to the target value and list the indices 