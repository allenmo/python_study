# -*- coding:UTF-8 -*-
import pickle
import pprint

#dictionary = {'apple':'苹果', 'orange':'橙子'}
dict_file = open('dictionary_en_ch.pkl', 'rb')
dictionary = pickle.load(dict_file)
pprint.pprint(dictionary)
print "Total : ", len(dictionary), " words"

input_word = raw_input("Input a English word: ")
while input_word != '':
    if input_word in dictionary:
        print dictionary[input_word]
    else:
        chinese = raw_input("not found, if you know the Chinese, please input:")
        if chinese != '':
            dictionary[input_word] = chinese
    input_word = raw_input("Input a English word: ")

dict_file.close()

output = open('dictionary_en_ch.pkl', 'wb')
pickle.dump(dictionary, output, -1)
output.close()
