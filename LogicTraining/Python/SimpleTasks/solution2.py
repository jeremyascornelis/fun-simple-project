#get age from the user
userName = input("Enter your name: ")
userAge = int(input("Enter your age: "))

if userAge >= 18:
    print("You are able to participate in voting")
else:
    print(f"Sorry! You can't participate in voting because your age is {userAge}, you will be able to participate after {18-userAge} year")