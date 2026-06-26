#!/bin/python3
# native Libs
from common import *


# custom Libs
import popularNamesParser as babyNames

# imported Libs

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
    def toJson(self,indent=2) -> str:
        objKeys = list(self.__dict__.keys())
        template ={}
        for k in objKeys:
            template.setdefault(k, self.__dict__[k])
        return template


def progDebugInfo():
    # Preties and shows program information
    print(consoleBanner)
    print("Progaram Paths")
    print(consoleTitleHeader)
    for p in progPaths:    
        print(p)
    print(consoleBanner)
    print("PROGRAM BEGINS")
    print(consoleBanner)
def determineSex(isBoy = babyNames.random.randint(0,1)):
    '''Helper function to determine sex of people for name selection'''
    if not isBoy:
        sex = "girl"
    else:
        sex = "boy"
    return sex
def genName(birthYear = babyNames.random.randint(1880,2022),isBoy = babyNames.random.randint(0,1)):
    '''Returns a name based off a selected year range and bool value of boy or not'''
    return babyNames.accessMasterFile(birthYear, determineSex(isBoy))
def generatePerson(birthYear = babyNames.random.randint(1880,2022),isBoy = babyNames.random.randint(0,1)):
    '''Returns a single person class object'''
    firstName = genName(birthYear, isBoy)
    lastName = genName(birthYear, isBoy)


    return Person(firstName=firstName,lastName=lastName, yearBorn=birthYear,sex=determineSex(isBoy))
def generatePeople(isboy :int = None,\
                   birthRange: Tuple[int, int]=(1880,2022),
                   numberOfPeople : int = 16):
    '''Returns a list of person class objects'''
    people : List[Person] = []
    random_sex = False
    if isboy == None:
        random_sex = True
    for x in range(numberOfPeople):
        if random_sex:
            isboy = babyNames.random.randint(0,1)

        randBirthYear = babyNames.random.randint(birthRange[0],birthRange[1])
        people.append(generatePerson(randBirthYear, isboy))
    return people[0:numberOfPeople]

def parseSelectedOption(selection, userInputData=()):
    match(selection):
        case 1:
            #we passed console data
            if(userInputData):
                    
                pass
            #get user input
            else:
                year = input("What year would you like to select names from?(1880-2022)") or babyNames.random.randint(1880,2022)

                sexSelection = input("what sex is the name based from?(boy or girl)") or babyNames.random.randint(0,1)
                
                print(f"{year}:{type(year)}\n{sexSelection}:{type(selection)}")
                print(genName(int(year), sexSelection))

                pass
        case 2:
            generatePerson()
        case 3:
            generatePeople()
            pass
        case _:
            print("idk what you did but i don't like it")
            pass
    pass

#consoleCommand will be a tuple, with 1 arg being selection, followed by year, then sex selection
def menuSelection():
    '''
    Function to work on,\n
    handles a console numerical input to automate a function selection,\n
    or presents a list of options and waits for console input
    '''
    #available options for the program as numerical selection
    options = [
        'generate single name',
        'generate a person',
        'generate multiple people',
        'quit'
    ]
    #show the list of availble options
    for x in range(len(options)):
        print(f"{x+1}. {options[x]}")
    #get user input
    selction = input(f"which opperation would you like to do? (1-{len(options)})")

    #validate user input
    while int(selction) > len(options) or int(selction) < 1 :
        #alert to error
        print("!!!--> Error option out of range <--!!!")
        #reshow menu options
        for x in range(len(options)):
            print(f"{x+1}. {options[x]}")
        #ask for input again, assume proper numerical value
        selction = int(input(f"which opperation would you like to do? (1-{len(options)})"))
        
        
    parseSelectedOption(selection=int(selction))

def consoleParser(consoleCommand):
    if(consoleCommand):
        #do program selection.
        if(int(consoleCommand) <= len(options) and int(consoleCommand) >= 1 ):  
            print(f"Menu selction: {consoleCommand}")
        #something is wrong with our argument
        else:
            print(f"Menu selction: {consoleCommand} Does not exist")
        parseSelectedOption(consoleCommand)
        #exit
        pass



    with open(htmlFilePath, 'w') as f:
        f.write(doc.render())
if __name__ == "__main__":
    #saves program arg list
    args = sys.argv
    progDebugInfo()

    #if we were passed no arguments
    if len(args) == 1:
        menuSelection()
    #pass along the argument, assume only the fist arg is valid
    else:
        #check legnth of the argument(1-3)
        #test what each value is and if they are appropriate
        possibleArgs = args[1:5]
        actualSize : int = len(possibleArgs)
        print(f"# args: {actualSize}")
        match(actualSize):
            #must only be the menu selction option
            case 1:
                #print("must only be the menu selction option")
                consoleParser((possibleArgs[0]))
                pass
            #should be a year, but might a selction of sex
            case 2:
                print("should be a year, but might a selction of sex")
                pass
            #should be both, but in what order?
            case 3:
                # menu option, year, number of people
                selection = possibleArgs[0]
                year = possibleArgs[1]
                sexSelection = possibleArgs[2]

                if selection == "1":
                    
                    name = genName(int(year), sexSelection)
                    print(f"name: {name}")
                elif selection == "2":
                    person = generatePerson(int(year), sexSelection)
                    print(f"person: {person.toJson()}")
                elif selection == "3":

                    selection : str = possibleArgs[0]
                    year : int = possibleArgs[1]
                    numberOfPeople : int = int(possibleArgs[2])

                    peoples = generatePeople(None, birthRange=(int(year), int(year)), numberOfPeople=numberOfPeople)
                    peoples_json = json.dumps([p.toJson() for p in peoples], indent=2)

                    print(f"{peoples_json}",file=open(jsonDataPath/"people.json","w"))
                    
                    json_to_html(peoples, jsonDataPath/"people.json", htmlDataPath/"people.html")
                    print(f"JSON file saved to: {jsonDataPath/'people.json'}")
                    print(f"HTML file saved to: {htmlDataPath/'people.html'}")
                print(f"Menu selction: {selection}\nYear: {year}\nSex Selection: {'RANDOM'}")
                pass
            case 4:
                # menu option, year, sex, number of people
                selection : str = possibleArgs[0]
                year : int = possibleArgs[1]
                sexSelection : int = int(possibleArgs[2])
                numberOfPeople : int = int(possibleArgs[3])
                peoples = generatePeople(sexSelection, (int(year),int(year)),numberOfPeople=numberOfPeople)
                peoples_json = json.dumps([p.toJson() for p in peoples], indent=2)

                print(f"{peoples_json}",file=open(jsonDataPath/"people.json","w"))
                
                json_to_html(peoples, jsonDataPath/"people.json", htmlDataPath/"people.html")
                print(f"JSON file saved to: {jsonDataPath/'people.json'}")
                print(f"HTML file saved to: {htmlDataPath/'people.html'}")
                print(f"Menu selction: {selection}\nYear: {year}\nSex Selection: {determineSex(sexSelection)}\nNumber of People: {numberOfPeople}")

            case _ :
                print("your args too big for your head")
        

        #menuSelection((args[1],args[2],args[3]))
    
    #print(babyNames.accessMasterFile(1880, "the ultimate gender bender of all time"))

    #babyNames.accessMasterFile(1880)





    """    people = generatePeople((1880,1920),numberOfPeople=1000)
    for p in people:
        print(p.toJson())
    """    
  
    
    #print(babyNames.getRandomNameByYear(2023,"girl"))

    #print(sys.argv)
    #print(sys.path)
    
    pass
