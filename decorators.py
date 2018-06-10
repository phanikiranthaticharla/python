def myDecorator(f):
    def wrapper(a, b):
        print "Enterering decorator"
        f(a, b)
        print "Leaving decorator"
    return wrapper


# Using the @ keyword
@myDecorator
def mult(a, b):
    print "mult function called"
    print a*b


mult(4, 5)
