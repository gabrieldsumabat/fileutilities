## Imports
import os

###################
## DEF FUNCTIONS ##
###################

def findFilename(fileType):
    ## Find Folder
    confirmPath=False
    print("\n##### "+fileType+" FILE SELECTION #####")
    while confirmPath==False:
        print("\nPlease enter the full path to the "+fileType+" file. \n Ex. C:\\Folder\\file.txt or /opt/folder/file.txt")
        pathInput=input()
        testPath=os.path.exists(pathInput)
        if testPath==False:
            print("    #ERROR: Path to file does not exist.\n")
        isFile=os.path.isfile(pathInput)
        if isFile==False:
            print("    #ERROR: Path does not point to file.\n")
        if testPath==True and isFile==True:
              print("Valid path entered.\n\nPlease verify this is the path you want by entering 'c'.")
              print("Path:"+pathInput)
              print("To return to path selection enter 'n'.")
              validInput=False
              while validInput==False:
                  userConfirm=input()
                  if userConfirm=='c' or userConfirm=='C':
                      confirmPath=True
                      validInput=True
                  elif userConfirm=='n' or userConfirm=='N':
                      validInput=True
                  else:
                      print("   #ERROR: Invalid input detected.")
    ## Find File Offset
    print("\nPlease enter the line offset value. (Integers only)")
    print("Ex. Entering 2 would exclude the first two characters from the line comparison.")
    print("Enter 0 if there is no line offset value.\nA negative offset will select characters starting from the end of the line.")
    print("Ex. Entering -2 for 'three' will print 'ee'.\n")
    validOffset=False
    while validOffset==False:
        ## ScrubInput
        validType=False
        while validType==False:
            getOffset=input()
            ## Check Input
            try:
                getOffset=int(getOffset)
                validType=True
            except:
                print("    #ERROR:Invalid type detected.")

        getOffset=int(getOffset)
        print ("Input is valid. \nPlease confirm by entering 'c' or 'C'\nThe selected offset is: "+str(getOffset))
        validInput=False
        while validInput==False:
            userConfirm=input()
            if userConfirm=='c' or userConfirm=='C':
                validOffset=True
                validInput=True
            elif userConfirm=='n' or userConfirm=='N':
                validInput=True
            else:
                print("   #ERROR: Invalid input detected.")
    return pathInput, getOffset


def setFilename(fileType):
    ## Find Folder
    confirmPath=False
    print("\n##### "+fileType+" FILE SELECTION #####")
    while confirmPath==False:
        print("\nPlease enter the full path to the "+fileType+" file. \n Ex. C:\\Folder\\file.txt or /opt/folder/file.txt")
        pathInput=input()
        testPath=os.path.exists(pathInput)
        if testPath==True:
            print("    #ERROR: Path to file already exist.\n")
        if testPath==False:
              print("Valid path entered.\n\nPlease verify this is the path you want by entering 'c'.")
              print("Path:"+pathInput)
              print("To return to path selection enter 'n'.")
              validInput=False
              while validInput==False:
                  userConfirm=input()
                  if userConfirm=='c' or userConfirm=='C':
                      confirmPath=True
                      validInput=True
                  elif userConfirm=='n' or userConfirm=='N':
                      validInput=True
                  else:
                      print("   #ERROR: Invalid input detected.")
    return pathInput


###################
## MAIN FUNCTION ##
###################
version = "1.0"
## Welcoming Message
print ("Welcome to fileCompare "+version+"! \n")
print ("This utility will compare the source file to the target file.")
print ("Any unique lines from either text file will be output into a new text file.")
## Setup File IO
confirmFiles=False
while confirmFiles==False:
    print("\n##### FINDING FILE NAMES ##### \n")
    fileType="source"
    sourceFile, sourceOffset=findFilename(fileType)
    print(sourceFile)
    fileType="target"
    ##Ensure source and target are different files
    fileSame=True
    while fileSame==True:
        targetFile, targetOffset=findFilename(fileType)
        if targetFile==sourceFile:
            print("    #ERROR: Same source and target detected. Restarting file selection for target file.")
        else:
            fileSame=False
    fileType="output"
    outputFile=setFilename(fileType)
    print ("##### CONFIRMING FILENAMES ##### \n")
    print ("\nThe selected files are: \n Source:"+sourceFile+", offset:"+str(sourceOffset)+"\n Target:"+targetFile+", offset:"+str(targetOffset)+"\n Output:"+outputFile)
    print ("Please confirm this selection be entering 'c' or 'C'.")
    userConfirm=False
    while userConfirm==False:
            userInput=input()
            if userInput=='C' or userInput=='c':
                userConfirm=True
                confirmFiles=True
            else:
                print ("    #ERROR INVALID INPUT") 
## Remove offset if configured.
with open(sourceFile) as openSource:
    sourceLines=set(openSource.read().splitlines())
with open(targetFile) as openTarget:
    targetLines=set(openTarget.read().splitlines())
sourceFiltered=[]
for sline in sourceLines:
    sourceFiltered.append(sline[sourceOffset:])
targetFiltered=[]
for tline in targetLines:
    targetFiltered.append(tline[targetOffset:])
## Compares the two lists and writes the results. 
writtenFile=open(outputFile,'w+')
writtenFile.write("#####Source File Unique lines##### \n\n")
sourceDifference=list(set(sourceFiltered)-set(targetFiltered))
for elems in sourceDifference:
    writtenFile.write(elems+"\n")
writtenFile.write("\n\n#####Target File Unique lines##### \n\n")
targetDifference=list(set(targetFiltered)-set(sourceFiltered))
for elemt in targetDifference:
    writtenFile.write(elemt+"\n")
writtenFile.close()
## Closing Messages
print("\nCompare has completed.")
print("Results are stored in "+outputFile)
print("Enter any key to close this window.")
input()
        
    
    
###Future Enhancements###
## Tab completion of file search
## cd/dir style navigation



## Coded by Gabriel Sumabat on Feb 16, 2017
## Last updated on Feb 21, 2017
