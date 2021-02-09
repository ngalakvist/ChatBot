import nltk
from nltk import stem
from nltk.stem.lancaster import LancasterStemmer
from tflearn.layers.core import activation
stemmer = LancasterStemmer()
 
import numpy
import tflearn
import tensorflow
import random
import json
import pickle

#Get data
with open("c:/ML/chat_bot/data/intents-mdh.json") as file:
    data = json.load(file)

""" try:
    with open("data.pickle", "rb") as f:
        words,labels,training,output = pickle.load(f)
except:  """
words = []
labels = []
docs_x = []
docs_y = []

# Preprocessing 
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))
labels = sorted(labels)

#Bag of words [ 0,2,,0,0,0,0]
training = []
output = []
out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag =[]
    wrds = [stemmer.stem(w) for w in doc]
    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])]= 1

    training.append(bag)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

with open("data.pickle", "wb") as f:
    pickle.dump((words,labels,training,output),f)

#AI Model with tensorflow
net = tflearn.input_data(shape=[None,len(training[0])])
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,len(output[0]),activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)
model.fit(training,output,n_epoch=5quit000,batch_size=8, show_metric=True)
model.save("model.tflearn")

#Test and Predict
def bag_of_word(s,words):
    bag = [ 0 for _ in range(len(words))]

    s_words= nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words :
        for i, w in enumerate(words):
            if w== se:
                bag[i] ==1
    return numpy.array(bag)

   #"Chat function for testing"      
def chat():
    print("Börja prata med Mdh chat-bot(type quit to quit")
    responses = ""
    while True:
        inp = input("Du: ")
        if(inp.lower()=="quit"):
             break
        
        results =  model.predict([bag_of_word(inp,words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if(tg["tag"]) == tag:
                responses = tg["responses"]

        print(random.choice(responses))  

chat()


