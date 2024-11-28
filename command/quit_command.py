from command.command import Command

class QuitCommand(Command):

	def execute(self):
		print("deconnection...")
		exit()