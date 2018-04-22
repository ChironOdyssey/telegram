# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:24:06 2018

@author: resha
"""

# initiate telegram
import telepot
import pandas as pd
from telepot.loop import MessageLoop

# input token
token = str(open('chatbot_token.txt', 'r').read()).strip()
token = token
TelegramBot = telepot.Bot(token)

#Defining global variables
global counter 
global Label

#Instantiating global variables
counter = 0
Label = []
#TelegramBot.getMe()

#Reading the images from the source
df = pd.read_json('input_images.json')
image_urls = list(df['image_url'])

# load input data
def on_chat_message(msg):
    # define message and labels
    global counter
    message = 'what is in the picture?'
    label = str(df['labels'].iloc[0]).split(',')
    button = { 'inline_keyboard': [[{'text':label[0],'callback_data':str(label[0])}],
                               [{'text':label[1],'callback_data':str(label[1])}]]}

    # display images
    TelegramBot.sendPhoto(chat_id=393309954,
                          photo=image_urls[counter],
                          caption=message,
                          reply_markup=button)

#If the worker selected a label, display the next image
def on_callback_query(msg):
    global counter, Label
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    Label.append(query_data)
    
    #does not work for now
    #if(counter == (len(df)-1)):
    #    result_df = pd.DataFrame(data = [df["image_id"], Label], index = None)
    #    print(result_df)

    #works but the logic is not clear yet
    if(query_data is not None):
        counter = counter + 1
        print(counter)
        on_chat_message(TelegramBot)
        
    if(counter == 4):
        TelegramBot.sendMessage(393309954,"Thank you for your work, your account has been credited with x tokens, your reputation has increased by x Rp.")

TelegramBot.sendMessage(393309954,"Hi Resham, I am Chiron chatbot, thank you for joining the platform.")
TelegramBot.sendMessage(393309954,"Chiron is a decentralised platform for training Artificial Intelligence, on Chiron's Network we are combining efforts to label images so that machines can learn to see as humans.Enter the correct label and we pay you in crypto! The network itself has the responsibility to validate that your answer is the correct one, not single centralised authority.")

#def InitialConversation(msg):
    #TelegramBot.sendMessage(393309954,"Hi Resham, I am Chiron chatbot, thank you for joining the platform.")
    #TelegramBot.sendMessage(393309954,"Chiron is a decentralised platform for training Artificial Intelligence, on Chiron's Network we are combining efforts to label images so that machines can learn to see as humans.Enter the correct label and we pay you in crypto! The network itself has the responsibility to validate that your answer is the correct one, not single centralised authority.")

#button1 = {'inline_keyboard' : [[{'text': "option 1: computer vision for online retail",'callback_data':"option 1: computer vision for online retail"}],
#                                [{'text': "option 2: computer vision for defect detection on airplanes",'callback_data':"option 2: computer vision for defect detection on airplanes"}]]}
TelegramBot.sendMessage(393309954,"Lets work on Cats/Dogs")
    #query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
#updates = TelegramBot.getUpdates()
#num_updates = len(updates["result"])
#last_update = num_updates - 1
#text = updates['message']['text'] #["result"]
#if(text is "option 1: computer vision for online retail"):
#TelegramBot.sendMessage(393309954,"The goal here is to train an algorithm to recognise different types of clothes.")
#TelegramBot.sendMessage(393309954,"What kind of clothes do you see here?")
MessageLoop(TelegramBot, {'chat': on_chat_message,
                                  'callback_query': on_callback_query}).run_as_thread()

