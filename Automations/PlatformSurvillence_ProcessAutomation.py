import psutil, sys, os, time, schedule

def ProcessScan():
    listprocess = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid", "name", "username", "status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        listprocess.append(info)

    return listprocess

def PlatformSurvillance(FolderName):
    Border = "--"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to proceed as directory name is existing but it is not a directory")
            return

    else:
        os.mkdir(FolderName)  
        print("Directory for the log file created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj= open(FileName,"w")

    print(f"Log file created successfully with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Survillence System-----\n")
    fobj.write("Log file created at : "+ timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-------------------- System Report --------------------\n")

    # CPU Information
    fobj.write("Number of active CPU Cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n"%psutil.cpu_percent())
    fobj.write(Border+"\n")

    #RAM Information
    memory = psutil.virtual_memory()

    fobj.write("RAM Usage : %s %%\n"%memory.percent)
    fobj.write("Total RAM Available : %s\n"%memory.total)

    fobj.write(Border+"\n")

    # Network Usage
    netobj = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj. write("Sent : %.2f MB \n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj. write("Recieved : %.2f MB \n" %(netobj.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # Process Log
    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n"%info.get("pid"))
        fobj.write("NAME : %s\n"%info.get("name"))
        fobj.write("USERNAME : %s\n"%info.get("username"))
        fobj.write("CPU USAGE : %.4f\n"%info.get("cpu_percent"))
        fobj.write("RAM USAGE : %.2f\n"%info.get("memory_percent"))

        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("-------------------- End of Log File --------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    Border = "--"*50

    print(Border)
    print("----- Marvellous Platform Survillence System -----")
    print(Border)

    # -- h and --u handeling
    if(len(sys.argv) == 2):
        if((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
            print("This automation script is used to perform ")
            print("1: It fetches the information of running process")
            print("2: It fetches the information about the primary storage as RAM")
            print("3: It fetches the information about the secondary stoarge as HDD")
            print("4: It fetches the information about the microprocessor")
            print("5: It gets auto scheduled periodically")
            print("6: It maintains all records into a log file")
            print("7: It sends the log files through mail periodically")

        elif((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Filder_Name : To store the log files that will be created")
            

        else:
            print("Invalid Number of Arguments")


    #Actual project code
    elif(len(sys.argv) == 3):

        #print("CPU Usage : ",psutil.cpu_percent())
        print("Scheduler Started Successfully")
        print("Press ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance, sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)
            

    else:
        print("Unable to proceed as Arguments are not matching")
        print("Please use --h or --u flags to get more details")


    print(Border)
    print("-----Thank You for using our Automation System-----")
    print(Border)

if __name__ == "__main__":
    main()