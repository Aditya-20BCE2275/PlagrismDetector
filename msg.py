import pywhatkit as kit
import datetime
import pandas as pd

df = pd.read_csv('exported.csv')
print(df)

def msg():
    print(f"WhatsApp message sent to +918169394959")
    message = f"Your Data is found to be plagarised which is part of a website more than alllowed limits"
    kit.sendwhatmsg(
        "+918169394959",
        message,
        datetime.datetime.now().hour,
        datetime.datetime.now().minute + 1,
        15,
        True,
        1,
    )
    
if(df['Similarity (%)'][0] > 5):
    msg()
