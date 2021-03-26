import datetime
from datetime import date
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
from random import randint

a = input ("Please enter the name of the Google Sheet. Names are case-sensitive and space-sensitive.              ")
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret2.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here
sheet = client.open(a).sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

TITLE = "ENIGMA M3 - UKW-B Reflector - October 2020 - Code Book"
NUMBER_OF_DAYS = 30

def rotor_selection(numberOfRotors):
    rotors = ["I","II","III","IV","V"]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = randint(0, numberOfRotors-1)
    ii = randint(0, numberOfRotors-1)
    while ii==i:
      ii = randint(0, numberOfRotors-1)
    iii = randint(0, numberOfRotors-1)
    while iii==i or iii==ii:
      iii = randint(0, numberOfRotors-1)
    
    rotor_i = rotors[i]
    rotor_ii = rotors[ii]
    rotor_iii = rotors[iii]

    settings = rotor_i +  " " + rotor_ii + " " + rotor_iii
    settings = settings + (" "*(9-len(settings)))
    return settings
    
def ring_settings(numberOfRotors):  # returns ring settings
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    settings = ""
    for i in range(numberOfRotors):
      rotor = randint(0, 25)
      settings = settings + alphabet[rotor]
    return settings  

def plugboard_settings(numberOfPermutations):  # Plugboard steckering
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    settings = ""
    stecksA = []
    stecksB= []
    
    for i in range(numberOfPermutations):
      a = randint(0, 25)
      while a in stecksA:
        a = randint(0, 25)
      stecksA.append(a)
      
    for i in range(numberOfPermutations):
      b = randint(0, 25)
      while b in stecksA or b in stecksB:
        b = randint(0, 25)
      stecksB.append(b)

    stecksA.sort()        
    
    settings=""
    for i in range(numberOfPermutations):
       settings = settings + alphabet[stecksA[i]] + alphabet[stecksB[i]] + " "
            
        
    settings = settings[:-1]
    return settings
  
def rotor_positions(numberOfRotors):  # Rotor position
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    settings = ""
    for i in range(numberOfRotors):
      rotor = randint(0, 25)
      settings = settings + alphabet[rotor]
    return settings


def generateCodeBook(title, numberOfDays):
    print(title)
    pos = 1
    today = date.today()
    m = today.strftime("%m")
    d = today.strftime("%d")
    b = today.strftime("%B")
    y = today.strftime("%y")
    sheet.update_cell(1, 7, b)
    for day in range(numberOfDays,0,-1):
        print('+------------------------------------------------+')
        if day<10:
          settings = "|  " + str(day) + " | "
        else:
          settings = "| " + str(day) + " | "
        settings = settings  + rotor_selection(5) + " | "
        settings = settings + ring_settings(3) + " | "
        settings = settings + plugboard_settings(6) + " | "
        settings = settings + rotor_positions(3) + " |"
        print(settings)
        pos +=1
        sheet.update_cell(pos, 2, rotor_selection(5))
        sheet.update_cell(pos, 3, ring_settings(3))
        sheet.update_cell(pos, 4, plugboard_settings(6))
        sheet.update_cell(pos, 5, rotor_positions(3))
        time.sleep(5.2)
        print('+------------------------------------------------+')
    
            
generateCodeBook(TITLE, NUMBER_OF_DAYS)


