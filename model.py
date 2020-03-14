import pickle

"""
    Main backend file
"""

#MONTHS = ["", ]


class Month:
    def __init__(self, name):
        self.name = name
        self.incomes = {}
        self.expenses = {}

    def addIncome(self, name, value):
        if name not in self.incomes:
            self.incomes[name] = value

    def addExpense(self, name, value):
        if name not in self.expenses:
            self.expenses[name] = value

    def displayData(self):
        print(self.name)
        print("incomes")
        for name in self.incomes:
            print(self.incomes[name])
        print()
        print("expenses")
        for name in self.expenses:
            print(self.expenses[name])


class Company:
    def __init__(self, args):
        self.months = {}
        # list of pereodic expenses which automatically applies every month
        # It's needed to complete month's reports
        # maybe better as dictionary
        self.pereodicIncomes = {}
        self.pereodicExpenses = {}
        #

    def addPereodicIncome(self, name, value):
        income = PereodicIncome(name, value)
        if name not in self.pereodicIncomes:
            self.pereodicIncomes[name] = income
            return "ok"
        else:
            return "incomeAlreadyInList"

    def addPereodicExpense(self, name, value):
        expense = PereodicExpense(name, value)
        if name not in self.pereodicExpenses:
            self.pereodicExpenses[name] = expense
            return "ok"
        else:
            return "expenseAlreadyInList"

    def removePereodicIncome(self, name):
        if name in self.pereodicIncomes:
            del self.pereodicIncomes[name]
            return "ok"
        else:
            return "noSuchIncome"

    def removePereodicExpense(self, name):
        if name in self.pereodicExpenses:
            del self.pereodicExpenses[name]
            return "ok"
        else:
            return "noSuchExpense"

    def __addPereodicDataToMonth__(self, month):
        for incomeName in self.pereodicIncomes:
            month.addIncome(incomeName, self.pereodicIncomes[incomeName])

        for expenseName in self.pereodicExpenses:
            month.addExpense(expenseName, self.pereodicExpenses[expenseName])
            
    
    def createNewMonth(self, monthID):
        if monthID not in self.months:
            self.months[monthID] = Month(monthID)
            self.__addPereodicDataToMonth__(self.months[monthID])
        else:
            return "monthAlreadyExist"


    def addIncomeToMonth(self, monthID, name, value):
        if monthID in self.months:
            income = InstantIncome(name, value)
            self.months[monthID].addIncome(name, income)
            return "ok"
        else:
            return "noSuchMonth"

    def addExpenseToMonth(self, monthID, name, value):
        if monthID in self.months:
            expense = InstantExpense(name, value)
            self.months[monthID].addExpense(name, expense)
            return "ok"
        else:
            return "noSuchMonth"

    def getMonthData(self, monthID):
        if monthID in self.months:
            self.months[monthID].displayData()
        else:
            return "noSuchMonth"



class PereodicIncome:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name + " - " + str(self.value)

class InstantIncome:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        return self.name + " - " + str(self.value)


class PereodicExpense:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        return self.name + " - " + str(self.value)

class InstantExpense:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        return self.name + " - " + str(self.value)




