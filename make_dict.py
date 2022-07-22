import pickle
special_characters = '"!@#$%^&*()-+?_=,<>/".1234567890' + "''"
in_file = open('words.txt', 'r')
out_file = open('four_letter_dict.txt', 'w')


for line in in_file:
    line = line.strip()
    if len(line) == 4:
        if  not any(c in special_characters for c in line):
            out_file.write(line.lower()+"\n")
    
in_file.close()
out_file.close()

words = []
with open('four_letter_dict.txt') as four_letter_dict:
    for word in four_letter_dict:
        words.append(word.strip())

pickle.dump(words, open("weaver_dictionary.pkl", "wb"))