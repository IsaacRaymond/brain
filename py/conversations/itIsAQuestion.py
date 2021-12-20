#####################Is it a question?###############
import pandas as pd
import numpy as np
import csv

#from tensorflow import keras
import tensorflow as tf

import sys

sys.path.append('/home/pi/brain/py/')

from playText import playText


questions_statements = pd.read_csv('/Users/isaacraymond/Desktop/ai/questions_vs_statements_v1.0.csv')
most_common_words = pd.read_csv('/Users/isaacraymond/Desktop/ai/most_common_words.csv')

results = []
with open('/Users/isaacraymond/Desktop/ai/most_common_words.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row[0])

word_to_ind = {word:ind for ind,word in enumerate(results)}

is_it_question_model = tf.saved_model.load("/Users/isaacraymond/Desktop")

def itIsAQuestion(audioFile):
    coded_list = []
    crappy = []

    for word in audioFile.split():
        try:
            coded_list.append(word_to_ind[word])
        except:
            coded_list.append(4342)

    crappy.append(coded_list)

    crappy = tf.ragged.constant(crappy)

    if (is_it_question_model(crappy)>0):
        return True

    else:
        return False
