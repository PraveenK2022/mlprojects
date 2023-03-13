class Car:
    def __init__(self,window,name):
        self.windows=window
        self.name=name
    
    def w_num(self):
        print("this call has {0} windows".format(self.windows))


try:
    a=b
except:
    CustomException()