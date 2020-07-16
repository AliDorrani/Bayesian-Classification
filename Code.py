from pandas import DataFrame, read_csv
import pandas as pd
import matplotlib.pyplot as plt
import math
import re
import numpy as np
import random


file = 'train_test.csv'
file_evaluate = 'evaluate.csv'
Data = pd.read_csv(file)

poems = Data['text']
statuses = Data['label']
numberOfpoems = len(poems)




train_index = random.sample(range(0,numberOfpoems), int(.8 * numberOfpoems))
test_index = list(set([item for item in range(0, numberOfpoems)]) - set(train_index))
hafez_poems_in_train_data = []
saadi_poems_in_train_data = []
total_vocab_in_train_data = {}
hafez_vocab_in_train_data = {}
saadi_vocab_in_train_data = {}


train_index.sort()
test_index.sort()




for index in train_index:
    poem = poems[index]
    words = poem.split(' ')
    if statuses[index] == 'hafez' :
        hafez_poems_in_train_data.append(poems[index])
    elif statuses[index] == 'saadi' :
        saadi_poems_in_train_data.append(poems[index])
    for word in words:
        if word not in total_vocab_in_train_data:
            total_vocab_in_train_data[word] = 0
        else:
            total_vocab_in_train_data[word]+=1


probability_hafez = (len(hafez_poems_in_train_data) / float(len(train_index)) )
probability_saadi = (len(saadi_poems_in_train_data) / float(len(train_index)) )

total_vocab_size_unique_word = len(total_vocab_in_train_data)

num_total_word_vocab_not_unique = 0
for key in total_vocab_in_train_data :
    num_total_word_vocab_not_unique+=total_vocab_in_train_data[key]
    


def recognizer(poems_td, vocab_td):
    for poem in poems_td:
        words = poem.split(' ')
        for word in words:
            if word not in vocab_td:
                vocab_td[word] = 0
            else:
                vocab_td[word]+=1
    return vocab_td



hafez_vocab_in_train_data = recognizer(hafez_poems_in_train_data,hafez_vocab_in_train_data)
saadi_vocab_in_train_data = recognizer(saadi_poems_in_train_data,saadi_vocab_in_train_data)
   

num_total_word_saadi_unique = len(saadi_vocab_in_train_data) 
num_total_word_saadi_not_unique = 0
for key in saadi_vocab_in_train_data :
    num_total_word_saadi_not_unique += saadi_vocab_in_train_data[key]


num_total_word_hafez_unique = len(hafez_vocab_in_train_data) 
num_total_word_hafez_not_unique = 0
for key in hafez_vocab_in_train_data :
    num_total_word_hafez_not_unique+=hafez_vocab_in_train_data[key]




print("Total Number Of Poems in train_test:",numberOfpoems)
print("hafez poems count in 80% train data:",len(hafez_poems_in_train_data))
print("saadi poems count in 80% train data:",len(saadi_poems_in_train_data))
print("probability hafez:" , probability_hafez)
print("probability saadi:" , probability_saadi)
print("num_total_word_vocab_not_unique",num_total_word_vocab_not_unique)
print("total_vocab_size_unique_word",len(total_vocab_in_train_data))
print("num poem in train data",len(train_index))
print("num_total_word_hafez_not_unique:",num_total_word_hafez_not_unique)
print("num_total_word_hafez_unique",num_total_word_hafez_unique)
print("num_total_word_saadi_not_unique:",num_total_word_saadi_not_unique  )
print("num_total_word_saadi_unique",num_total_word_saadi_unique)




unique_words = 0 
unique_words = len(total_vocab_in_train_data)
def calculate_probability_conditional(word,saadi_vocab_in_train_data,total_vocab_in_train_data,
                                        num_total_word_saadi_not_unique ,unique_words, condition):
    
    if(condition == "Laplace"):    
        num_word_in_saadi = 0
        if word in saadi_vocab_in_train_data:
            num_word_in_saadi = saadi_vocab_in_train_data[word]
        x =  num_word_in_saadi + 1
        y = float( num_total_word_saadi_not_unique + len(total_vocab_in_train_data))
        return x/y
    

    elif(condition == "Simple"):
        num_word_in_saadi = 0
        if word in saadi_vocab_in_train_data:
            num_word_in_saadi = saadi_vocab_in_train_data[word]
        x = num_word_in_saadi + .3
        y = float(num_total_word_saadi_not_unique + len(total_vocab_in_train_data))
        return x/y


def Unit_Test(test_index,
                statuses,
                poems,
                probability_hafez,
                probability_saadi,
                total_vocab_in_train_data,
                unique_words,
                num_total_word_vocab_not_unique,
                hafez_vocab_in_train_data,
                saadi_vocab_in_train_data,
                num_total_word_hafez_unique,
                num_total_word_saadi_unique,
                num_total_word_hafez_not_unique,
                num_total_word_saadi_not_unique):
    
    hafez_poems_in_test_data = []
    saadi_poems_in_test_data = []
    num_total_word_vocab_not_unique = 0
    total_vocab_in_test_data = {}
    hafez_vocab_in_test_data = {}
    saadi_vocab_in_test_data = {}
    correct_detected_hafezes = 0
    detected_hafezes = 0
    correct_detected = 0
    select_op = 0
    num_total_word_hafez_not_unique = 0
    num_total_word_saadi_not_unique = 0

    for index in test_index :
        if statuses[index] == 'hafez' :
            hafez_poems_in_test_data.append(poems[index])
        elif True:
            saadi_poems_in_test_data.append(poems[index])
            
    hafez_numberOfpoems_in_test_data = len(hafez_poems_in_test_data)
    saadi_numberOfpoems_in_test_data = len(saadi_poems_in_test_data)
 

    for index in test_index:
        poem = poems[index]
        words = poem.split(' ')
        for word in words:
            if word not in total_vocab_in_test_data:
                total_vocab_in_test_data[word] = 0
            elif True:
                total_vocab_in_test_data[word]+=1
            
    unique_words = len(total_vocab_in_test_data)

    

    for key in total_vocab_in_test_data :
        num_total_word_vocab_not_unique += total_vocab_in_test_data[key]
    

    hafez_vocab_in_test_data = recognizer(hafez_poems_in_train_data,hafez_vocab_in_train_data)
    saadi_vocab_in_test_data = recognizer(saadi_poems_in_train_data,saadi_vocab_in_train_data)

              
                
    num_total_word_hafez_unique = len(hafez_vocab_in_test_data) 
    for key in hafez_vocab_in_test_data :
        num_total_word_hafez_not_unique += hafez_vocab_in_test_data[key]
    
    num_total_word_saadi_unique = len(saadi_vocab_in_test_data) 

    
    for key in saadi_vocab_in_test_data :
        num_total_word_saadi_not_unique += saadi_vocab_in_test_data[key]

    print("\n\n Unit Test Initialization OutPut :")
    print("hafez poems count in 20% test data:",hafez_numberOfpoems_in_test_data)
    print("saadi poems count in 20% test data:",saadi_numberOfpoems_in_test_data)
    print("num_total_word_vocab_not_unique in 20% test",num_total_word_vocab_not_unique)
    print("total_vocab_size_unique_word in 20 % test",len(total_vocab_in_train_data))
    print("num poem in train data in 20% test",len(test_index))
    print("num_total_word_hafez_not_unique in 20% test:",num_total_word_hafez_not_unique)
    print("num_total_word_hafez_unique in 20% test: ",num_total_word_hafez_unique)
    print("num_total_word_saadi_not_unique in 20% test:",num_total_word_saadi_not_unique  )
    print("num_total_word_saadi_unique in 20 % test",num_total_word_saadi_unique)
    print("Unit Test Initialization OutPuts Ends \n")
        
    
    all_hafezes = len(hafez_poems_in_test_data)
    total = len(test_index)
    
    
    select_op = int(input("\n\n\n '1'.... Laplace \n '2' ....Simple \n\n\n"))
    
    for index in test_index:
        poem = poems[index]
        words = poem.split(' ')
        p_hafez = probability_hafez
        p_saadi = probability_saadi
        for word in words:
            if(select_op == 2):
                p_hafez *= calculate_probability_conditional(word,hafez_vocab_in_train_data,
                                                                total_vocab_in_train_data,
                                                                num_total_word_hafez_not_unique ,
                                                                len(total_vocab_in_train_data),"Simple")
                
                p_saadi *= calculate_probability_conditional(word,saadi_vocab_in_train_data,
                                                            total_vocab_in_train_data,
                                                                num_total_word_saadi_not_unique ,
                                                            len(total_vocab_in_train_data),"Simple"  )
            if(select_op == 1): 
                p_hafez *= calculate_probability_conditional(word,hafez_vocab_in_train_data,
                                                           total_vocab_in_train_data,
                                                            num_total_word_hafez_not_unique ,
                                                            len(total_vocab_in_train_data),"Laplace")
                p_saadi *= calculate_probability_conditional(word,saadi_vocab_in_train_data,total_vocab_in_train_data,
                                                            num_total_word_saadi_not_unique , len(total_vocab_in_train_data),"Laplace")

        if p_hafez > p_saadi:

            detected_hafezes += 1
            if statuses[index] == 'hafez':
                correct_detected_hafezes += 1
                correct_detected += 1
          
        ##model decide saadi
        elif p_hafez < p_saadi:
            if statuses[index] =='saadi':
                correct_detected+=1

    recall = correct_detected_hafezes/float(all_hafezes)
    precision =  correct_detected_hafezes/ float(detected_hafezes)  
    accuracy = correct_detected / float(total)
            
    if(select_op == 2):
        print("Recall in simple:",recall)
        print("Precision in simple:",precision)
        print("Accuracy in simple:",accuracy)
    if (select_op == 1):
        print("Recall in Laplace:",recall)
        print("Precision in Laplace:",precision)
        print("Accuracy in Laplace:",accuracy)



Unit_Test(test_index,
            statuses,
            poems,
            probability_hafez,
            probability_saadi,
            total_vocab_in_train_data,
            len(total_vocab_in_train_data),
            num_total_word_vocab_not_unique,
            hafez_vocab_in_train_data,
            saadi_vocab_in_train_data,
            num_total_word_hafez_unique,
            num_total_word_saadi_unique,
            num_total_word_hafez_not_unique,
            num_total_word_saadi_not_unique)
        




# def make_evalute_file( evalute_filename ,
#                     probability_hafez,
#                     probability_saadi,
#                     total_vocab_in_train_data,
#                     unique_words,
#                     num_total_word_vocab_not_unique,
#                     hafez_vocab_in_train_data,
#                     saadi_vocab_in_train_data,
#                     num_total_word_hafez_unique,
#                     num_total_word_saadi_unique,
#                     num_total_word_hafez_not_unique,
#                     num_total_word_saadi_not_unique):
    
#     Data = pd.read_csv(evalute_filename)
#     index = Data['id']
#     poems = Data['text']
#     statuses = []
#     for poem in poems:
#         words = poem.split(' ')
#         p_hafez = probability_hafez
#         p_saadi = probability_saadi
#         for word in words:
#             p_hafez *= calculate_probability_conditional(word,hafez_vocab_in_train_data,
#                                                            total_vocab_in_train_data,
#                                                             num_total_word_hafez_not_unique ,
#                                                             len(total_vocab_in_train_data),"Laplace")
#             p_saadi *= calculate_probability_conditional(word,saadi_vocab_in_train_data,total_vocab_in_train_data,
#                                         num_total_word_saadi_not_unique , len(total_vocab_in_train_data),"Laplace")
            
#         if p_hafez > p_saadi:
#             statuses.append('hafez')
#         elif p_hafez < p_saadi:
#             statuses.append('saadi')
#     Data.insert(2,'label',statuses)
#     print(Data.head(20))
#     Data.to_csv("output.csv")
    
# make_evalute_file(file_evaluate ,
#                     probability_hafez,
#                     probability_saadi,
#                     total_vocab_in_train_data,
#                     len(total_vocab_in_train_data),
#                     num_total_word_vocab_not_unique,
#                     hafez_vocab_in_train_data,
#                     saadi_vocab_in_train_data,
#                     num_total_word_hafez_unique,
#                     num_total_word_saadi_unique,
#                     num_total_word_hafez_not_unique,
#                     num_total_word_saadi_not_unique)





