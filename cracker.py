import time 
import pandas as pd 
import hashlib

def task1() :                                           #Take Hash from user input and store it in an a list
    while True :
        print("Please enter one or more hashes") 
        hash1 = input("HASH >>")
        if hash1 == "." : 
            break
        hashes_user.append(hash1)
        
def task2(filename) :        
#Function which takes filename as parameter and reads      it                                                                                                                                                        #Open CSV file and store the first column which are the hashes
    df = pd.read_csv("sha256_hashes.csv")
    for i in df["hash"] : 
        
        hashes_file.append(i)
      
        
def decrypt(filee, listofhashes):                       
    """
    Decrypt hashes by hashing some words in a specific file and 
    Then comapring the hashes together (Dictionary attack)
    Code to crack an SHA256 hash using a dictionary

    @param filee:  List of dictionary Words
    @param listofhashes:    The Hash we want to crack
    """
    
    for text in filee:
        theHash = hashlib.sha256(text.strip().encode()).hexdigest()
        
        
      
        
        for target in listofhashes :
            theHash = theHash.upper()                                       # Nested for loop to compare multiple targets 
                                                                        # With the the same hashed plaintext 
            
            
            if theHash == target :                                  
                print("-----CRACKED-----")
                print("TEXT {0} ".format(text))
                print("HASH :{0} ".format(theHash))
                print("------------------")
                
 

    
        
if _name_ == "_main_" :
    hashes = open("passwords.txt", "r").readlines()
    """
    Opens a CSV file , Read 1st column , Store in a list , Compare hashes with hashed plaintext 
    """
   
    hashes_file = []
   
    task2("sha256_hashes.csv")
    startTime = time.time()
    decrypt(hashes,hashes_file)
    endTime = time.time()
    print ("Total of {0} Seconds".format(endTime - startTime
