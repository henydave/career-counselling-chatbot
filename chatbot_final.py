# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:11:35 2018

@author: henyd
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Couns',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',                  
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('G:/Sgp/english/'):
        convData = open(r'G:/Sgp/english/' + file ,encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)	     
        chatbot.train(convData)
        #print("Training completed")

setup()
