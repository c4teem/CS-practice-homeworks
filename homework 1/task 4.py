# FOUR

# H H : M M : S S
# 0 1 2 3 4 5 6 7

time = input()
counting = 0
count_variables = 0 

for i in time:

    if count_variables == 0 and (i == "0" or i == "1" or i == "2"):
        count_variables += 1
        counting += 1

    elif count_variables == 1 and (i == "0" or i == "1" or i == "2" or i == "3"):
        count_variables += 1
        counting += 1

    elif count_variables == 2 and i == ":":
        count_variables += 1
        counting += 1

    elif count_variables == 3 and (i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5"):
        count_variables += 1
        counting += 1

    elif count_variables == 4 and (i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9"):
        count_variables += 1
        counting += 1

    elif count_variables == 5 and i == ":":
        count_variables += 1
        counting += 1

    elif count_variables == 6 and (i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5"):
        count_variables += 1
        counting += 1

    elif count_variables == 7 and (i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9"):
        count_variables += 1
        counting += 1

    else:
        count_variables += 1  


if counting == 8:
    print("TRUE")
else:
    print("FALSE")
