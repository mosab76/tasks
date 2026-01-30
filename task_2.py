while 1 :
    temp = int(input("Please enter current temperature in Celsius: "))
    if temp >= 30 :
        print("It's a hot day. Stay hydrated!")
    elif temp >= 20 and temp <= 29 :
        print("It's a warm day. Enjoy the weather!")
    elif temp >= 10 and temp <= 19 :
        print("It's a cool day. Wear a jacket!")
    else :
        print("It's a cold day. Stay warm!")
        
# i used while loop to make you test the code without needing to refresh
    