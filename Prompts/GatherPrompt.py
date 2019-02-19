#this will be the command to make requests to BS4 and requests

class GatherPrompt:
    greeting = "This is where we'll gather data, it will take prompts"
    warning = "There is nothing to show here, move along"

    def greetUser(self):
        print(self.greeting)
        print(self.warning)
        return False