#this will be where we display the data with a class

class DisplayData:
    greeting = "This is where we display the data in various ways, not all of it though"
    warning = "There is nothing else to show here"

    def greetUser(self):
        print(self.greeting)
        print(self.warning)
        return False