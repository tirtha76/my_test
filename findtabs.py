# program for getting openingtab&closingtab of application

import psutil
import datetime

proc_list = []
def opentab():
    while True:
        for proc in psutil.process_iter():
            try:
                if 'idle' in proc.name():
                    processName = proc.name()
                    processID = proc.pid
                    if processID not in proc_list:
                        print('alert: someone trying to enter your application...........')
                        opening_t=datetime.datetime.today()# to get time of openingtab
                        tm = "Started at {}".format(opening_t)

                        print(processName ,tm, ' with procees id: ', processID )
                        proc_list.append(processID)
                                
                             
                else:
                    continue
            except Exception as E:#(psutil.NoSuchProcess, psutil.AccessDenied,):
               print(E)
    
        
    

            
def closedtab():
    
    rproc_list=[]
    
    while True:
        for procid in proc_list:
            if psutil.pid_exists(procid) != True and procid not in rproc_list:
                print('process idle with id {} has closed '.format(procid))
                rproc_list.append(procid)
            else:
                pass


                
                
                
            
if __name__ == '__main__':
    opentab()
    closedtab()
