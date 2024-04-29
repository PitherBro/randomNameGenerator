#collection of variables to launch/set program configuration
workingDir=$(pwd)
pythonVENV=$workingDir/venv
venvScript=$pythonVENV/bin/activate
venvRequirements=$workingDir/requirements.txt


#12 #'s in a row
seperator="############"

genHeader(){
    #a predefined way of creating a header text in console
    echo "###### $1 ######"
}
seperator-12(){
echo $seperator
}
seperator-36(){
echo $seperator$seperator$seperator
}
