
def adds_to_ten(given_list):
    number_dict = {}
    for number in given_list:
        if (10 - number) in number_dict:
            print(str(number) + "," + str(10 - number))
            return
        else:
            number_dict[number] = 1
    print("There is no pair of ten in this list.")


given_list = [1, 3, 9, 5, 2]
print(adds_to_ten(given_list))
