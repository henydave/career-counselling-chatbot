# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:24:54 2018

@author: henyd
"""
from sklearn import tree
from sklearn import svm
import numpy as np
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
def get_response(usrText):
    bot = ChatBot('Couns',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
		'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': "Sorry, I didn't understand."
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if usrText.strip()!= 'start':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        if usrText.strip()== 'start':
            z = []
            with open('features1.txt', 'r') as xf:
                for xline in xf:
                    x = xline.split(',')
                    for i in range(0,len(x)):
                        x[i] = int(x[i])
                    z.append(x)
            w = []
            with open('labels1.txt', 'r') as yf:
                for yline in yf:
                    y = yline
                    w.append(y)
            clf = tree.DecisionTreeClassifier()
            clf = clf.fit(z, w)
            abroad = input("Do you see yourself in some foreign country like USA, Canada, UK, Australia, Russia in about 5 years? [1/0]: ")
            job = input("Are you satisfied with your bachelor's degree and want to do no more furthur studies ? [1/0]: ")
            interest = input("Do you love doing coding and are you confident that you can solve the hardest problem if you are given plentiful of time ? [1/0]: ")
            mba = input("Do you feel so as if you can't perform well in IT and you think that you can't compete well with others from our branch ?: [1/0]: ")
            prediction = clf.predict([[abroad, job, interest, mba]])
            print("You should think of doing: ",prediction)
            return("Thats all")
            
