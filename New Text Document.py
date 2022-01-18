import os
os.system('cls')
input_age = 0
the_smallest_age = 9
the_greatest_age = 90
list_in_10_to_90 = []
while input_age != -1:
    input_age = int(input(""))
    if input_age == -1:
        break
    elif input_age <= the_smallest_age:
        continue
    elif input_age > the_smallest_age and input_age <= the_greatest_age:
        list_in_10_to_90.append(input_age)
    elif input_age > the_greatest_age:
        continue
if list_in_10_to_90 == []:
        print('is empty')
else:
    print(max(list_in_10_to_90))







# if the_smallest_age <= the_greatest_age:
#     if list_in_10_to_90 == (range(the_smallest_age,the_greatest_age)):

    # elif the_greatest_age > 90:
    #     print(the_greatest_age)
    # elif list_in_10_to_90 == []:
    #     print('is empty')
