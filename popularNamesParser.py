#!/bin/python3
import os,sys,json, random
from pathlib import Path

root = Path(os.path.dirname( __file__ ))
dataSources = root/"dataSources"

#sourceFile
#https://github.com/aruljohn/popular-baby-names.git
#local Dir when installed
babyNames_1880_to_2022 = Path(dataSources/"popular-baby-names-master")

'''
#import another module from anywhere
modPath = root/"module"
sys.path.append(modPath)
'''

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


if  __name__ == "__main__":
    '''if this module is main, lets check the file integrity'''
    #print(__name__)
    if(os.path.exists(babyNames_1880_to_2022)):
        print("Good to Go")
    else:
        print("names do not exist, begining download")