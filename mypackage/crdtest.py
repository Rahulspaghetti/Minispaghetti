#!/usr/bin/env python
# coding: utf-8

# In[84]:


import json
import datetime
import threading
import time
import os.path
import io
import sys


from threading import *

def check(): #Values to be stored
        if os.path.exists('Datastore.json'):
            pass
        else:
            print ("Either file is missing or is not readable, creating file...")
            empty={}
            with open("Datastore.json", "w") as outfile:
                json.dump(empty, outfile)
            
def create(key,value,timeout=0.0):
    check()
    with open('Datastore.json') as createjson_file: 
        Datastore = json.load(createjson_file)
    if key in Datastore:
        print("key already exists")
    else:
        if(key.isalpha()):
            if sys.getsizeof(Datastore)<(1024*1020*1024) and sys.getsizeof(value)<=(16*1024*1024): #Non Functional requiremnt:file size less than 1GB
                #Jsonobject value less than 16KB
                if timeout==0.0:
                    data=[value,timeout]
                else:
                    threading.Thread(target=timedelete, args=(key,timeout)).start()
                    data=[value,time.time()+timeout]
                if len(key)<=32: #constraint for input key <= 32chars
                    Datastore[key]=data
            else:
                print("Memory limit reached")
        else:
            print("error: Invalind key:no special characters or numbers")
    with open("Datastore.json", "w") as createoutfile:  
        json.dump(Datastore, createoutfile)

        
def read(key):
    check()
    with open('Datastore.json') as readjson_file: 
        Datastore = json.load(readjson_file)
    if key not in Datastore:
        print("key does not exist/expired in database.") #error message4
    else:
        b=Datastore[key]
        if b[1]!=0.0:
            if time.time()<b[1]: #comparing the present time with expiry time
                string=str(key)+":"+str(b[0]) #to return the value in the format of JsonObject
                return string
            else:
                del Datastore[key]
                print("key has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri
    with open("Datastore.json", "w") as readoutfile:  
        json.dump(Datastore, readoutfile)
        
def Delete(key):
    check()
    with open('Datastore.json') as Deletejson_file: 
        Datastore = json.load(Deletejson_file)
    if key not in Datastore:
        print("Key do not exist")
    else:
        del Datastore[key]
    with open("Datastore.json", "w") as Deleteoutfile:  
        json.dump(Datastore, Deleteoutfile)
        
def timedelete(key,timeout):
    time.sleep(timeout)
    with open('Datastore.json') as json_file: 
        Datastore = json.load(json_file)
    if key in Datastore:
        del Datastore[key]
    with open("Datastore.json", "w") as timedeleteoutfile:  
        json.dump(Datastore, timedeleteoutfile)

