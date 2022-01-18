# Find-the-age-of-the-biggest-candidate-and-the-second-biggest-candidate
Find the age of the biggest candidate and the second biggest candidate

import os
os.system('cls')
list123 = []
input_user = 0
while input_user != -1:
    input_user = int(input(''))
    if input_user >= 10 and input_user <= 90:
        list123.append(input_user)
list123.sort()
much_bigger = list123[-1]
bigger = list123[-2]
print(much_bigger , bigger)
