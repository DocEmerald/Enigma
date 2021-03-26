# Enigma
A python package based on the WWII Enigma machine used by the Germans - is an encryption device and can be linked to personal Google Sheets to provide full lists of rotaries, codes, etc. 

# Installation

Installation may seem a little intimidating at first-glance, but overall it is a pretty simple process. Have a folder/directory ready to put all the files in. Much of the installation tutorial comes from here: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

First and foremost, you, of course, want to create a Google Sheet. I recommend creating a copy of this:

https://docs.google.com/spreadsheets/d/1IMNXLtodyI6F8uLw60mSW5CI8ikVssbnwhanvVPJVMo/edit?usp=sharing

You can then use that as the template, as it is formatted for the Enigma sheet. The boxes which are filled in will auto-update.

Then, go to the [Google API Dashboard](https://console.cloud.google.com/apis/dashboard?pli=1). 
From here, create a new project, enable API Services, and search for the Google Drive API. Enable it, click create credentials.
Choose the Google Drive API when it asks which one you are using, say no to the App/Compute Engine prompt, then click "What Credentials Do I Need?"
From here, name the Service Account, give it the role of a Project Editor, then download the JSON file. Put it in your directory, then name it client_secret2 (If you do not name it this, the program WILL NOT WORK!)
Now, open the JSON file (you can do it in any text editor such as notepad), find "client_email", then copy the email.
Now, share the email to the Google Sheets by pasting it in after clicking the "Share" button.

After you've done this, download either the .exe or the .py (I'd recommend downloading both, as it's most stable then) from the [releases page](https://github.com/DocEmerald/Enigma/releases). It may say the .exe is not trusted, you can download it anyway by clicking the up arrow then "keep". If you don't trust it, take a look at the .py and just download that, but keep in mind that could lead to instability.

Put both downloaded files in your directory along with the JSON file, then run either. It'll prompt you to enter the sheet name, at which point you should enter *the full and exact name, case sensitive, space sensitive*.

Once this is done, it should work, and you can decode the characters with any online enigma decoder.
