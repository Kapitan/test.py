def fn1(fn2):
    def inner(*args, **kwargs):
        print("ya vnetri fn1", *args, **kwargs)
        fn2()
    return inner
@fn1
def testfn():
    print("ya v testfv")

testfn("asf")
