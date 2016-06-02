__author__ = 'jlu69'

def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder

def hellocounter (name):
    count=[0]
    def counter():
        count[0]+=1
        print 'Hello,',name,',',str(count[0])+' access!'
    return counter

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"


if __name__ == "__main__":
    #sample 1
    # p = make_adder(23)
    # q = make_adder(44)
    # print p(100)
    # print q(100)

    #sample 2
    # hello = hellocounter('ma6174')
    # hello()
    # hello()
    # hello()

    print hello()
