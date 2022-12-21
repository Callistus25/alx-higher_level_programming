#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in my_list[:x]:
        try:
            j += 1
            print("{}".format(i), end="")
        except:
            break
    print("")
    return
