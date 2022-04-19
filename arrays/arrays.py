# Testing arrays and vectors

def array_test():
    ar = [1, 3, 5, 7, 9]

    # removes and return last object in list
    ar.pop()

    # appeneds element to end of list
    ar.append(11)

    print(ar)
    print("Index of 5:", ar.index(3)) # index place of given value

    # remove first occurence of item with given valuen
    ar.remove(5)
    print("Removed 5:", ar)

    # reverse the array
    ar.reverse()
    print("Reversed:", ar)
    # sort the array after reversal then print
    print("Sorted Return:", sorted(ar))

    ar.sort()
    print("Sorted original: ", ar)

# add functions to main
def main():
    array_test()

if __name__ == "__main__":
    main()
    print("Task Finished")