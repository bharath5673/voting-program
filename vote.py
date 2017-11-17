def vote():
    state=input("please enter your state")
    if state == "karnataka":
        print("okay...")
        age = int(input("now enter your age"))
        if age >= 18:
                gender = input("enter your gender")
                if (gender == "male" or gender == "female"):
                    print("okay..")
                    city = input("now enter your city")
                    if (city == "bangalore" or city == "mandya"  or city == "mysore"):
                        print("you can vote")
                    else:
                        print("sorry.. you do not belong to the domain")
                else:

                    print("please enter your correct gender")

        else:
            print("sorry...u r below 18'you can't vote")
    else:
        print("sorry.. you do not belong the state ")

vote();