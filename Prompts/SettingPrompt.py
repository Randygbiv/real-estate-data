#this will be where the user manages their data and what DB they use

from Helpers import typeHelper
from Helpers import cliHelper

typeHelp = typeHelper.typesHelper()
cliHelp = cliHelper.Helper()

class SettingPrompt:
    greeting = "Welcome to settings where you'll decide where your data is stored"
    warning = "There is currently nothing to show here."

    def greetUser(self):
        print(self.greeting)
        print(self.warning)
        return False
