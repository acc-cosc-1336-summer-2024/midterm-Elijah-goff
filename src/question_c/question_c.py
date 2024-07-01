#write functions here, don't add input('') statements here!
a = 10
def use_global():
    global a
    print("a val :" ,a)

    a = a+15 #modify
    print("a val:" ,a)

    a = a+25
    return

use_global()
print("a val:" ,a)
