#!/bin/python3
#native Libs
import os,sys, datetime
from pathlib import Path


#custom Libs
import popularNamesParser as babyNames

#imported Libs

root = Path(os.path.dirname( __file__ ))


progPaths = [
    root,
    babyNames.dataSources,
    babyNames.babyNames_1880_to_2022,
]

consoleBanner="#"*16
consoleTitleHeader="-"*16
'''
#import another module from anywhere
modPath = root/"module"
sys.path.append(modPath)
'''

class Person:
    '''A class to generate generic information and be stored/returned as JSON data'''
    def __init__(self, firstName="", lastName="", yearBorn=datetime.datetime.now().year-16, sex="boy" or "girl") -> None:
        self.yearBorn = yearBorn
        self.sex = sex
        
        if firstName == "":
            self.firstName = babyNames.getRandomNameByYear(self.yearBorn,self.sex)
        else:
            self.firstName = firstName
        
        if lastName == "":
            self.lastName = babyNames.getRandomNameByYear(self.yearBorn,self.sex)
        else:
            self.lastName = lastName 
        #self.lastName = babyNames.getRandomNameByYear(self.yearBorn,self.sex)
        
        pass
    def age(self,):
        return datetime.datetime.now().year-self.yearBorn
    def toJson(self,):
        objKeys = list(self.__dict__.keys())
        template ={}
        for k in objKeys:
            template.setdefault(k, self.__dict__[k])
        return template
def determineSex(isBoy = babyNames.random.randint(0,1)):
    '''Helper function to determine sex of people for name selection'''
    sex = "boy"
    if not isBoy:
        sex = "girl"
    return sex
def genName(birthYear = babyNames.random.randint(1880,2022),isBoy = babyNames.random.randint(0,1)):
    '''Returns a name based off a selected year range and bool value of boy or not'''
    return babyNames.getRandomNameByYear(birthYear, determineSex(isBoy))
def generatePerson(birthYear = babyNames.random.randint(1880,2022),isBoy = babyNames.random.randint(0,1)):
    '''Returns a single person class object'''
    firstName = genName(birthYear, isBoy)
    lastName = genName(birthYear, isBoy)


    return Person(firstName=firstName,lastName=lastName, yearBorn=birthYear,sex=determineSex(isBoy))
def generatePeople(birthRange=(1880,2022),numberOfPeople = 16):
    '''Returns a list of person class objects'''
    people = [Person]
    for x in range(numberOfPeople):
        randBirthYear = babyNames.random.randint(birthRange[0],birthRange[1])
        people.append(generatePerson(randBirthYear))
    return people[1:numberOfPeople]
    pass
def menuSelection(consoleCommand=False):
    '''Function to work on,\n
    handles a console numerical input to automate a function selection,\n
    or presents a list of options and waits for console input'''
    #available options for the program as numerical selection
    options = [
        'generate single name',
        'generate a person',
        'generate multiple people',
        'quit'
    ]
    #test the argument if it's not False
    if(consoleCommand):
        #do program selection.
        if(int(consoleCommand) <= len(options) and int(consoleCommand) >= 1 ):
        
            print(f"Menu selction: {consoleCommand}")
        #something is wrong with our argument
        else:
            print(f"Menu selction: {consoleCommand} Does not exist")
        #exit
        pass
    #if we do not have a console command to do
    else:
        for x in range(len(options)):
            print(f"{x+1}. {options[x]}")
        selction = input(f"which opperation would you like to do? (1-{len(options)})")
        while int(selction) > len(options) or int(selction) < 1 :
            print("!!!--> Error option out of range <--!!!")
            for x in range(len(options)):
                print(f"{x+1}. {options[x]}")
            selction = input(f"which opperation would you like to do? (1-{len(options)})")
        pass
if __name__ == "__main__":
    # Preties and shows program information
    print(consoleBanner)
    print("Progaram Paths")
    print(consoleTitleHeader)
    for p in progPaths:    
        print(p)
    print(consoleBanner)
    print("PROGRAM BEGINS")
    print(consoleBanner)
    #saves program arg list
    args = sys.argv


    #print(len(args))
    #if we were passed no arguments
    if len(args) == 1:
        menuSelection()
    #pass along the argument, assume only the fist arg is valid
    else:
        menuSelection(args[1])
    

    '''
    people = generatePeople(numberOfPeople=16)
    for p in people:
        print(p.toJson())
    '''
  
    
    #print(babyNames.getRandomNameByYear(2023,"girl"))

    #print(sys.argv)
    #print(sys.path)
    
    pass
