for i in range (1,101):
    if (i % 3 == 0 and i % 5 == 0):
        print("fizz buzz")
    else :
        if (i % 5 == 0):
            print("buzz")
        else:
            if (i % 3 == 0):
                print("fizz")
            else :
                print(i)
