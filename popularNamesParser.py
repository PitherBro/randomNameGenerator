#!/bin/python3
import os,sys,json, random
from pathlib import Path

root = Path(os.path.dirname( __file__ ))
dataSources = root/"dataSources"

#sourceFile
#https://github.com/aruljohn/popular-baby-names.git
#local Dir when installed
babyNames_1880_to_2022 = Path(dataSources/"popular-baby-names-master")
masterFilePath = dataSources/"master.json"

'''
#import another module from anywhere
modPath = root/"module"
sys.path.append(modPath)
'''


masterFile = False
'''The big file of all the names (File Object with Read Permission)'''

def getDataFiles():
    '''Download files from Github and dispense into dataSources File '''
    pass
def getRandomNameByYear(year,boyOrGirl=None):
    '''Access a data folder by year, select a random name from that list.\n
        \tyear= an integer between 1880 and 2022, cannot be blank\n
        \tboyOrGirl=None by default, but can be "boy" or "girl"\n
        if boyOrGirl is None, returns random Girl or Boy name
    '''
    #makes sure year is between 1880 and 2022, reutrns None if not true
    if( not (year >= 1880 and year <= 2022)):
        print("please only use a year between 1880 and 2022")
        return None
    #compiles selected year into the related JSON file name
    fileName = "girl_boy_names_"+ str(year) + ".json"
   
    #comiles the abosulte path to JSON file
    completeFilePath = babyNames_1880_to_2022/str(year)/fileName
    fObj =open(completeFilePath,'r')
    #returns the contents of the JSON file
    contentsRaw = dict(json.loads(fObj.read()))

    #Gets the keys of the JSON file (year, boys, girls) 
    contentKeys = list(contentsRaw.keys())

    ## Set a default value of boy or girl name
    #generates random index for selecting boy or girl list from known keys. offset by 1 because year is first
    coinFlip = random.randint(0,1) +1
    #randomly selects girl or boy list
    selection = contentKeys[coinFlip]

    #make sure boyOrGirl is None, if not, lets use user selection
    if(boyOrGirl):
        #print(boyOrGirl)
        match boyOrGirl:
            case "boy":
                selection = "boys"
            case "girl":
                selection = "girls"
    #outputs if boyOrGirl is left blank
    else:
        print("DNE")
    #print(f"{contentKeys} --> {selection}")
    namesList = contentsRaw[selection]
    namesListSize = len(namesList)-1
    #print(contentsRaw[selection],selection)
    #make 1 random selection
    randListSelection = random.randint(0,namesListSize)
    #make sure selection is not blank
    while(namesList[randListSelection] == ''):
        randListSelection = random.randint(0,namesListSize)
    
    return namesList[randListSelection]
    #print(namesList,"\n",selection)
def createMasterFileJSON():
    '''Consolidate the github repo into one JSON file to save I/O '''
    
    masterFile = {}

    for x in range(1880,2023):
        completeFilePath = babyNames_1880_to_2022/str(x)/f"girl_boy_names_{x}.json"
        curYearData = dict(json.loads(open(completeFilePath,'r').read()))
        year = curYearData.pop("year")
        masterFile.setdefault(year, curYearData)
        #print(masterFile)
        #masterFile.append(json.dumps(curYearData))
    print("-"*32)
    print(json.dumps(masterFile),file=open(masterFilePath,'w'))
def accessMasterFile(year,boyOrGirl=None):
    '''Access the master file by year, select a random name list based on Sex.\n
        \tyear= an integer between 1880 and 2022, cannot be blank\n
        \tboyOrGirl=None by default, but can be "boy" or "girl"\n
        if boyOrGirl is None, returns random Girl or Boy name
    '''
    #So python knows to look globaly not locally for masterFile
    global masterFile
    #the file is already assigned and being used, no action needed
    if(masterFile):
        #print("is here")
        pass
    #the file needs to be, and is assigned
    else:
        print("not here, not all, dont look.")
        masterFile = open(masterFilePath,"r")

    #makes sure year is between 1880 and 2022, reutrns None if not true
    if( not (year >= 1880 and year <= 2022)):
        print("please only use a year between 1880 and 2022")
        return None
    contentsRaw = dict(json.loads(masterFile.read()))

    #https://pscustomobject.github.io/python/Python-Reset-Read-Write-Position/
    masterFile.seek(0,0)
    #contentKeys = list(contentsRaw.keys())
    #print(contentsRaw[str(year)])
    coinFlip = random.randint(0,1)
    selection = "girls"
    match coinFlip:
        case 0:
            selection = "girls"
        case 1:
            selection = "boys"
        case _:
            print("The flip flipping failed i say")
    if(boyOrGirl):
        #print(boyOrGirl)
        match boyOrGirl:
            case "boy":
                selection = "boys"
            case "girl":
                selection = "girls"
            case _ :
                print("invalid option, using a random selection")

    #print(contentsRaw[str(year)][selection],"-"*16,"\n" ,selection)
    namesList = contentsRaw[str(year)][selection]
    namesListSize = len(namesList)-1

    #make 1 random selection
    randListSelection = random.randint(0,namesListSize)
    #make sure selection is not blank
    while(namesList[randListSelection] == ''):
        randListSelection = random.randint(0,namesListSize)
    #print(selection)
    return namesList[randListSelection]
    
def checkModuleIntegretiy():
    '''
    Checks that module directories and files are all there.
    '''
    return os.path.exists(babyNames_1880_to_2022) and\
         True

if  __name__ == "__main__":
    '''if this module is main, lets check the file/module integrity'''
    #print(__name__)
    if(checkModuleIntegretiy()):
        print("Good to Go")
        
    else:
        print("Names do not exist, begining download")
        print("Consolidating...")
        #createMasterFileJSON()
        print("Removing archive")
    
