#Duck typing
class Pycharm:
	def execute(self):
		print("Compiling")
		print("Running")

class MyEditor:
	def execute(self):
		print("Spell check")
		print("Convention check")
		print("Compiling")
		print("Running")

class Laptop:
	def code(self,ide):
		ide.execute()
		
ide = MyEditor()
 
lap1 = Laptop()
lap1.code(ide)
ide = Pycharm()
lap1.code(ide)