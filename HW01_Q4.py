def hailstone(n):
    count = 0 #! The value to return
    print(n)
    while (n != 1):
        #print (n)
        if (n % 2 == 0):
            n = round(n / 2)
            print (n)
            count += 1
        elif (n % 2 != 0):
            n = n*3 + 1
            print(n)
            count += 1
    else:
        return count + 1
    return count+1

a = hailstone(1)
print('The total steps are ', a)