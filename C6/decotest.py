import time

class costTime:
    def __init__(self,func):
        st=time.time()
        self.func=func
        et=time.time()
        print("用时：%f"%(et-st))
    def __call__(self, *args):
        st = time.time()
        self.func(*args)
        et = time.time()
        print("用时：%f"%(et-st))
        