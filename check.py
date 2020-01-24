def prime(x):
    for i in (2,x):
        if(x%i==0):
            return "Not a prime no."
        else:
            return "Prime no."

