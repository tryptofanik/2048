class Field:

    value = None


    def __init__(self,value):
        self.value = value

    def getValue(self):
        if self.value == None:
            return "."
        return self.value

    def __str__(self):
        if self.value is None:
            return str(0)
        return str(self.value)

    def isOccupied(self):
        return self.value != None

    def setValue(self, newvalue):
        self.value = newvalue
