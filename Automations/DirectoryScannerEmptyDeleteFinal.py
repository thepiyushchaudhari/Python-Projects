##########################################################
#
#   Importing required libraries
#
##########################################################

import sys
import os
import time
import schedule

##########################################################
#
#   Function name :     DirectoryScanner
#   Input :             Name of Directory
#   Description :       Deletes all empty files periodically
#   Date :              19/07/2026   
#   Author :            Piyush Manohar Khairnar
#
##########################################################

def DirectoryScanner(DirectoryPath):
    Border = "-"*40

    timestamp = time.ctime()
    
    LogFileName = "Marvellous%s.log"%(timestamp)        
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = False

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : There is no such directory with name ",DirectoryPath)
        return
    
    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : It is not a directory with name ",DirectoryPath)
        return
    
    print("Log file gets created with name : ",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write(" Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")

    fobj.write(" Files from the directory are : \n\n")
    fobj.write(Border+"\n")

    TotalFiles = 0
    EmptyFile = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            TotalFiles = TotalFiles + 1

            fname = os.path.join(FolderName,fname)
            fobj.write(f"{fname} : {os.path.getsize(fname)} bytes\n")

            if(os.path.getsize(fname) == 0):
                EmptyFile = EmptyFile + 1
                os.remove(fname)

    fobj.write(Border+"\n")
    fobj.write(f"Total files scanned : {TotalFiles}\n")
    fobj.write(f"Total empty files found and deleted : {EmptyFile}\n")

    fobj.write(Border+"\n")
    fobj.write("Log file gets created at : "+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()

##########################################################
#
#   Function name :     main
#   Input :             Command line arguments
#   Description :       It controls the script
#   Date :              19/07/2026   
#   Author :            Piyush Manohar Khairnar
#
##########################################################

def main():
    Border = "-"*40
   
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)
    
    if(len(sys.argv) == 2):
        
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the scipt as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        
        else:
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            
            while True:
                schedule.run_pending()
                time.sleep(1)
                
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print(" Thank you for using Marvellous Automation Script ")
    print(Border)

##########################################################
#
#   Starter of the automation script
#
##########################################################

if __name__ == "__main__":
    main()