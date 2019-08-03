import psutil
import datetime
import threading
import sys

proc_list = []

def opentab():
    
    while True:
            
        for proc in psutil.process_iter():
            try:
                if proc.name() == 'idle':
                        
                    processName = proc.name()
                    processID = proc.pid
                        
                    if processID not in proc_list:
                        print('alert: someone trying to enter your application...........')
                        opening_t=datetime.datetime.today()
                        tm = "Started at {}".format(opening_t)

                        print(processName ,tm, ' with procees id: ', processID )
                        proc_list.append(processID)
                            
                           
                    else:
                        continue
            except (psutil.NoSuchProcess, psutil.AccessDenied,):
               pass
        

            
def closedtab():
    
    rproc_list=[]
    
    while True:
        for procid in proc_list:
            if psutil.pid_exists(procid) != True and procid not in rproc_list:
                print('process idle with id {} has closed '.format(procid))
                rproc_list.append(procid)
            else:
                pass



    
                    
##thread_list = []

thread1=threading.Thread(target=opentab())
##thread1.append(thread_list)


thread2=threading.Thread(target=closedtab())
##thread_list.append(thread2)
thread1.start()
thread2.start()

thread1.join()


##def run_my_app():
##    for thread in thread_list:
##        thread.start()
##        print("Thread1 Started..")
##def run_my_app1():
##    for thread in thread_list:
##        thread.join()
##        print("Thread2 started..")
##def run_main():
##    run_my_app()
##    run_my_app1()
##    return "Done"
##    
##
##if __name__ == '__main__':
##    try:
##        print("Starting Monitoring...")
##        run_main()
##    except Exception as Ex:
##        print(Ex)
##        sys.exit()
##        
##    
##
##
##    





##for thread in process:
##    thread




                
                
                
            
