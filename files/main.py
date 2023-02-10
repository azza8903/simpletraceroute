import subprocess
import time
import json
import shutil


RESULTS_DIR = "/monroe/results/"
OUTPUTFILE = "/opt/simpletraceroute/simpletracerouteResults.txt"
TARGETINTERFACE = "op0"

try:
    with open("/monroe/config", "r") as fd:
        configurationParameters = json.load(fd)
except Exception as e:
    print("Cannot retrive /monroe/config {}".format(e))
    print("Using default parameters.......")
    configurationParameters = { 
	"targets": [
		 "google.com",
		 "YouTube.com",
		 "facebook.com",
                 "Pornhub.com",
                 "Xvideos.com",
                 "Twitter.com",
                 "Wikipedia.org",
                 "Reddit.com",
                 "Instagram.com",
                 "Xnxx.com"
        ],
        "interfaces":[
                "op0",
                "op1"
        ]
}

    usingDefaults = True

def traceRoute(interface,target):
        cmd = ["traceroute", "-i",interface, '-w', '5',target]
        out = subprocess.check_output(cmd).decode('ascii')
        return out

with open(OUTPUTFILE, 'a') as rt_tables:
        for i in range (len(configurationParameters['interfaces'])):
                print ("Using Interface: "+configurationParameters['interfaces'][i])

                for j in range (len(configurationParameters['targets'])):
                        print ("Trace routing Website: "+ 
                        configurationParameters['targets'][j])
                        
                        output=traceRoute(configurationParameters['interfaces'][i],
        configurationParameters['targets'][j])
                        
                        rt_tables.write(output)


shutil.copy2("/opt/simpletraceroute/simpletracerouteResults.txt", RESULTS_DIR + "simpletracerouteResults.txt" + ".tmp")
shutil.move(RESULTS_DIR + "simpletracerouteResults.txt" + ".tmp", RESULTS_DIR + "simpletracerouteResults.txt")

time.sleep(3600)


