#Polymorphism
#Duck typing
#IDE is Integrated Development Environment
class Pycharm:
	def execute(self):
		print("Compiling")
		print("Running")
		
class MyEditor:
	def execute(self):
		print("Scripting")
		print("Writing")
		print("Editing")
		print("Compiling")
		
class Laptop:
	def code(self,ide):
		ide.execute()

ide = Pycharm()
lap1 = Laptop()
lap1.code(ide)		
print("This is Duck typing an example of Polymorphism")
iide = MyEditor()
lap2 = Laptop()
lap2.code(iide)