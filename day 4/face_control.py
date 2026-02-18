age = float(input("Enter your age: "))
if age < 18:
    print("You are not allowed to enter the club.")
else:
    ticket = input("Do you have ticket? (yes/no): ").lower()
    if ticket == "yes":
        print("Welcome to the club!")
    elif ticket == "no":
       buy = input("Do you want to buy it? It just 5$ (yes/no)").lower()
       if buy == "yes":
           print("Have a nice party!")
       elif buy == "no":
            print("Than why you go here? Go away!")
       else:
            print("just answer: yes or no.")
    else:
       print("just answer: yes or no.")