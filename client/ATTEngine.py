import subprocess
import urllib2
from subprocess import call
import os

class ATTSpeech:
    CLIENT_ID = "6jpqkqevk1v3ydnziwshofffrffbb5q7"
    CLIENT_SECRET = "nwzba5j61alo2jgaskkwr5xioy7vl639"
    TOKEN = "None"
    def __init__(self):
        pass

    def getToken(self):
        #Get Access Token via OAuth.
        proc = subprocess.Popen([os.environ['JASPER_HOME']+"/jasper/static/getToken.sh", self.CLIENT_ID, self.CLIENT_SECRET], stdout=subprocess.PIPE)
        tmp = proc.stdout.read()
        tmp = tmp.replace("\"","").replace("{","").replace("}","").split(":")[1]
        self.TOKEN = tmp[:32]

    def getResults(self,path):
        if not self.haveInternet():
            return ["SPECIAL CASE I COULD NOT CONNECT TO THE INTERNET",None]

        proc = subprocess.Popen(["sh", os.environ['JASPER_HOME']+"/jasper/static/getResults.sh",self.TOKEN,path], stdout=subprocess.PIPE)
        tmp = proc.stdout.read()
        for strin in tmp.upper().replace("\"","").replace("{","").replace("[","").replace(":","").replace("}","").replace("]","").split(","):
            print strin
            if "HYPOTHESIS" in strin:
                strin = strin.strip().replace("HYPOTHESIS","").strip()
                return [strin,None]
            if "IOEXCEPTION" in strin:
                return ["SPECIAL CASE SPEECH API HAD AN ERROR",None]
            if "UNAUTHORIZED" in strin:
                print "The current token is invalic, getting a new one..."
                self.getToken()
                return self.getResults(path)
        return ["",""]

    def haveInternet(self):
        try:
            response=urllib2.urlopen('http://74.125.228.100',timeout=1) #Google IP. Prevents a long DNS look up for a url. 1 second timeout. Adjust as needed
            return True
        except urllib2.URLError as err: pass
        return False
