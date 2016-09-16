from datetime import date
from datetime import datetime
import time,sys,os
from apscheduler.schedulers.blocking import BlockingScheduler

def event_repeatedtask():
    #task to be done repeatedly 
    def job_function():
        print("\nRepeated task occurence at time: ");
        print(time.asctime(time.localtime(time.time())));
        print("\nEXIT!>>");
        return main();

    def res():
        print("\n Want to secify the task for weekdays PRESS Y/N ?");
        response = input()
        print("\nWaiting for occurence....");
        if response == 'y':
            sched.add_job(job_function, 'cron',day_of_week='mon-fri', hour=hr , minute=mn , start_date=(sd), end_date=(ed)); #specfic to weekdays
            sched.start()
        elif response == 'n':
            sched.add_job(job_function, 'cron', hour=hr , minute=mn , start_date=(sd), end_date=(ed));
            sched.start();
        else:
            res();

    sched = BlockingScheduler()
  
    #input set for repeating task:
    print("\nSpecify the start and end date for repeated tasks : ");
    print("\n NOTE: Do NOT append 0 for MM/DD, ex.02/03");
    sd = datetime.strptime(input('\nEnter START date in the format yyyy/mm/dd '), '%Y/%m/%d');
    ed = datetime.strptime(input('\nEnter End date in the format yyyy/mm/dd '), '%Y/%m/%d');
    hr = int(input("\nEnter the hour(24 hour - format) at which task should be repeated:"));
    mn = int(input("\nEnter the minute at which task should be repeated:"));
     
    res(); #to select only weekdays or not
    

def event_specific_date():

    def my_job():
        print("\n TASK scheduled for specific time:");   #task/function scheduled at a particular date and time.
        print(time.asctime(time.localtime(time.time())));#prints current time.
        print("\nEXIT!>>");
        scheduler.shutdown();
        main();
        
    sched = BlockingScheduler()    
        
    #user input section for specific date:
    yr = int(input("\nEnter the YEAR:YYYY at which task should be repeated:"));
    m = int(input("\nEnter the MONTH:MM at which task should be repeated:"));
    d = int(input("\nEnter the DATE:DD at which task should be repeated:"));
    
    hr = int(input("\nEnter the hour(24 hour - format) at which task should be repeated:"));
    mn = int(input("\nEnter the minute at which task should be repeated:"));
    s  = int(input("\nEnter the interval in seconds!")); 
    
    sched.add_job(my_job, 'cron',year=(yr), month=(m), day=(d) , hour=hr, minute=mn, second=s);
    sched.start()
    
def event_interval():

    def to_do():                                          #action/task to be sheduled
        print(time.asctime(time.localtime(time.time()))); #prints current time
         #max_instance is 1,couldnt not add exit loop. i had ealier tried sys.exit on response but it limits to one function in interval. 

    sched = BlockingScheduler()
    # Schedule to_do to be called upon user input.
    s = int(input("\nEnter the interval in seconds!")); #user input seconds
    h = int(input("\nEnter the interval in hours!"));   #user input hours
    print("Set according to current system time:");
    print(time.asctime(time.localtime(time.time())));
    #convert string from user to datetime object.
    print("\n NOTE: Do NOT append 0 for MM/DD, ex.M/D = 2/3");#format specifier 
    var = datetime.strptime(input('Enter End date in the format Year/Month/Date/Hour/Minute/Seconds '), '%Y/%m/%d/%H/%M/%S'); #end date and time for task according to foramt
    print("Current end-date_time:");print(var); #to check input for end date
    sched.add_job(to_do, 'interval', hours=h, seconds=s , end_date=(var));
    print("\nProcess started,current time: ");
    
    sched.start()
    
    print(" \n the end");
    main();
    
def exit():
    print("\nEXIT!>>");
    sys.exit();
	
def main():
    
    #menu based program   
    while True:
        print("\n WELCOME! Select events based on type of shedule,\n press the numberic value to select");	
        print("\n 1:event_repeatedtask\n 2:event_specific_date\n 3:event_interval\n 4:exit");
        print("\n NOTE: Do NOT append 0 for MM/DD, ex.M/D = 2/3");#format specifier 
        #dict specifying the event handlers:
        action = { 1:event_repeatedtask,
                   2:event_specific_date,
                   3:event_interval,
                   4:exit }
        sel = int(input(''));           
        action[sel]();
main();
