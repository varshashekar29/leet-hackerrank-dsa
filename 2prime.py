n=int(input())
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n," is not a prime number")
            break
    else:
        print(n, " is prime number")
else:
    print(n, " is not a prime number")


    #The above code works really well for 2 because
    #range(start,stop) ---> here the stop is always excluded in python hence range(2,2) there are no numbers to iterate.So it does not goes inside the loop, it moves to else part. Therefore 2 is prime number
