'''
Created on Jun 6, 2017

@author: cstone
'''
import os;
import time;

#Ping function, pass host and number of pings
def ping(host,numberOfPings):
    
    response = os.system("ping -c " + str(numberOfPings) +" " + host);
    if response == 0:
        return True;
    else:
        return False;
#use processor to run functions
def processor():

    #create a comma delimited list in Python
    hosts = ["www.google.com","www.msn.com","www.github.com"];
    counter = 0;
    
    while counter < 7:
        for host in hosts:
            try:
                pingIt = ping(host,1);
                if pingIt == True:
                    print(host +" is up!");
                else:
                    print(host +" is down!");
            except:
                print("ping function failed");
        time.sleep(300);
        counter +=1 #loop 7 times at 300 seconds, gives us 5 minutes

processor();
