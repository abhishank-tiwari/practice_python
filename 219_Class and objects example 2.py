class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("CPU is ",self.cpu)
        print("Ram is ",self.ram)
        
com1 = Computer("i5","16 gb")

com1.config()