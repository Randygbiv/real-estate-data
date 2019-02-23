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

    #Mutates the type of element so that it can be parsed correctly.
    def mutateType(self, elm, typeOfData):
        if elm == "None":
            return elm
        else:
            if typeOfData == 'int':
                return int(elm)
            else:
                return str(elm)
    
    #this makes sure that an element isn't none
    def checkNone(self, elm, typeOfTag):
        if elm == None:
            return 'None'
        else:
            if typeOfTag == "none":
                return elm.text
            else:
                return elm[typeOfTag]