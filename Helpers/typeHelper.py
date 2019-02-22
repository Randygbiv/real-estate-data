#this file will be used to help check types

class typesHelper:

    def checkIfString(self, value):
        if type(value) != str:
            return False
        else:
            return True
    
    def checkIfNumber(self, value):
        if type(value) != int:
            return False
        else:
            return True

    def tryParseInt(self, value):
        try:
            return int(value)
        except ValueError:
            return False