#this is where the help prompts are

class HelpPrompt:
    
    greeting = ("This is a command line interface that will pull data from a " +
                "website for real estate. It will then place that data inside " +
                "of a database. Then the data can be accessible to the user in " +
                "various ways.")

    def greetUser(self):
        print(self.greeting)
        return False