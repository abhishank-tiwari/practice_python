from abc import ABC , abstractmethod
class Computer(ABC):
	@abstractmethod
	def process(self):
		pass

	
class Laptop(Computer):
	def process(self):
		print("its running")

		
com1 = Laptop()
com1.process()
class Whiteboard:
	def write(self):
		print("Its writing")

		
class Programmer:
	def work(self,com):
		print("Solving Bugs")

		
prog1 = Programmer()
com = Laptop()
prog1.work(com)
whit1 = Whiteboard()
prog1.work(whit1)