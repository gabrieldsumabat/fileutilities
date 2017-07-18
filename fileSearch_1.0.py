### fileSearch_1.0 ###
## Made by Gabriel Sumabat

##########
##Imports#
##########
import os

###################
## MAIN FUNCTION ##
###################
version = "1.0"
## Welcoming Message
print ("Welcome to fileSearch "+version+"! \n")
##Infite loop
while 1:
        ## Find Folder
        pathValid=False
        confirmPath=False
        print("########## FOLDER/FILE SELECTION ##########\n\n")
        while confirmPath==False:
                cwDir = os.getcwd()
                print ("The current working directory is "+cwDir)
                print ("Listing files: \n")
                print (os.listdir())
                print ("\nIf this is not where the file is located please enter the full path now.")
                print ("Else enter 'c' to select this folder.")
                print ("Note: This entry is case sensitive.\n")
                pathInput=input()
                if pathInput!='c' and pathInput!='C':
                        pathValid=os.path.isdir(pathInput)
                        if pathValid==True:
                                os.chdir(pathInput)
                        else:
                                print("\n    ERROR:Path is invalid.\n")
                else:
                        print ("\nRemaining in current directory.\n")
                        pathValid=True
                        confirmPath=True
        ## Find File Name
        print ("\nPlease enter the log name.\n")
        fileValid=False
        while fileValid==False:
                fileLog=input()
                fileValid=os.path.isfile(fileLog)
                if fileValid==False:
                        print("\n    ERROR:Selected filename is invalid.\n") 
        ## Calculate Output File
        target=fileLog + "_search"
        print ("\nThe results of the search will be placed in a file called:\n"+target)
        ## Customize Search for Dates
        print("\n\n########## DATE SELECTION ##########\n\n")
        print ("Are there date(s) you are searching for? (Y/N)\n")
        dateChoice="invalid"
        dateSelected=[]
        while dateChoice=="invalid":
                userDate=input()
                if userDate=='Y' or userDate=='y':
                        dateChoice=1
                elif userDate=='N' or userDate=='n':
                        dateChoice=0
                else:
                        print("\n   ERROR:Invalid character detected.\n")
        if dateChoice==1:
                print ("\nDefault format is MM/DD/YYYY.")
                print ("Ex. 02/08/2017 for Febuary 8, 2017.")
                getDate=False
                while getDate==False:
                            print("\nPlease enter a valid date.")
                            print("Please enter 'C' to confirm you are complete.\n")
                            dateInput=input()
                            if dateInput=='c' or dateInput=='C':
                                getDate=True
                                print ("\nDate list is confirmed as: \n"+str(dateSelected)[1:-1])
                            elif dateInput=='d' or dateInput=='D':
                                print ("\nWhich string would you like to remove?\n")
                                removeDate=input()
                                if removeDate in dateSelected:
                                    dateSelected.remove(removeDate)
                                    print("Deleted "+removeDate+".")
                                else:
                                    print("\n   ERROR:Element does not exist. \n    Please enter 'D' again if you wish to attempt to delete.\n")
                                print ("\nThe current date list is:\n"+str(dateSelected)[1:-1])
                            else:
                                dateSelected.append(dateInput)
                                print ("\nThe current date list is:\n"+str(dateSelected)[1:-1])
        else:
                print ("No specified date(s) configured.\n")
        ## Configue custom string search
        print("\n\n########## STRING SELECTION ##########\n\n")
        getQuery=False
        valueQuery=[]
        while getQuery==False:
                    print("Please enter a string to search for.")
                    print("Please enter 'C' to confirm you are complete.")
                    print("Alternatively, enter 'D' to delete a string.\n")
                    queryInput=input()
                    if queryInput=='c' or queryInput=='C':
                        getQuery=True
                        print ("\nQuery list is confirmed as: \n"+str(valueQuery)[1:-1])
                    elif queryInput=='d' or queryInput=='D':
                          print ("\nWhich string would you like to remove?\n")
                          removeQuery=input()
                          if removeQuery in valueQuery:
                              valueQuery.remove(removeQuery)
                              print("Deleted "+removeQuery+".")
                          else:
                              print("Element does not exist. \n Please enter 'D' again if you wish to attempt to delete.\n")
                          print ("\nThe current query list is:\n"+str(valueQuery)[1:-1])
                    else:
                        valueQuery.append(queryInput)
                        print ("\nThe current query list is:\n"+str(valueQuery)[1:-1])
        ##Writing to the file
        print("\n\n########## SEARCH FUNCTION ##########\n\n")
        activeLog = open(fileLog, 'r')
        writtenLog = open(target, 'w+')
        i=0
        for line in activeLog:
                if any(query in line for query in valueQuery) and dateChoice==0 or any(query in line for query in valueQuery) and any(date in line for date in dateSelected):
                        writtenLog.write(line)
                        i+=1
        activeLog.close()
        writtenLog.close()
        print (str(i)+" lines written to "+target)
        print ("\nFlowchart extraction complete!")
        print ("Enter any key to continue.")
        print ("Or use 'CTRL+C' to quit.\n\n\n") 
        input()


                
##Written by Gabriel Sumabat in Python 3.6 on Feb 15, 2017 ##
## Program is compatible with most Python 3 versions.
####################Version 0.1A######################
##Last updated by Gabriel Sumabat on Feb 17th, 2017 ##
