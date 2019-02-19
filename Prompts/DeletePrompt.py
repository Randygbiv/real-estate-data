#this will be where we kill data based on specific things

class DeletePrompt:
    greeting = "Welcome to the delete prompt"
    warning = "There is nothing to show here yet"

    def greetUser(self):
        print(self.greeting)
        print(self.warning)
        return False