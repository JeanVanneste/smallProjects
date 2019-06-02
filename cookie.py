#!/usr/bin/python3

def prettyDisplay(total):
    tot3 = total // 1000000
    tot2 = (total%1000000) // 1000
    tot1 = total % 1000

    return (str(int(tot3)) + "'" + str(int(tot2)) + "'" + str(int(tot1)))

print("Cookies/sec ?")
revenue = float(input())

gain = 30*60*2.5*revenue
print("Gain = "+prettyDisplay(gain))

total = 20.*(gain/3.0)
print("Minimum reserve : " + prettyDisplay(total))
