temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")



score = int(input("What is your test score, dummy?"))
if score >= 90:
    print("Your grade is an A")
else:
    if score >= 80:
        print('Your grade is a B')
    else:
        if score >= 70:
            print("Your grade is a C, you may never find happiness")
        else:
            if score >= 60:
                print('Your grade is a d')
            else:
                print('You failed')