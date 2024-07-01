#write functions here, don't add input('') statements here!
maximum = int(input("Enter the maximum value :"))
total = 0
num = 1

while num <= maximum:
    if(num % 2 == 0):
        print("{0}".format(num))
        total = total + num
    num = num + 1

    print(" Sum Of Even Numbers from 1 to N ={0}".format(total))

    