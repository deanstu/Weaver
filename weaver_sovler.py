from tkinter import N
from anytree import Node, RenderTree, PreOrderIter
import pickle

# get starting word
start = input("Starting Word: ").lower()

#get end word
end = input('Ending Word: ').lower()

in_file = open('weaver_dictionary.pkl', 'rb')
words = pickle.load(in_file)
in_file.close()


words_set = {start}



def get_next_words(word):
    
    next_words = []
    for i in range(4):
        #print(s[0:i] + "_" + s[i+1:4])
        begin = word[0:i]
        end = word[i+1:4]
        for w in words:
            if w != word and w[0:i] == begin and w[i+1:4] == end:
                #print(w)
                next_words.append(w)
    
    return next_words

def remove_bad_words():

    wait = input('Hit enter once bad guesses entered into form: ')
    with open('nonwords.txt') as bad_words:
        nonos = set()
        for word in bad_words:
            nonos.add(word.strip())

    for word in words:
        if word in nonos:
            words.remove(word)

    pickle.dump(words, open("weaver_dictionary.pkl", "wb"))

def add_levels(tree,stop,level):
    
    print(level)
    paths = {}
    for node in PreOrderIter(tree):
        if node.is_leaf:
            paths[node.name] = []
            next_guesses=get_next_words(node.name)
            for guess in next_guesses:
                if guess not in words_set:
                    paths[node.name].append(guess)
                    words_set.add(guess)
                    

    for key in paths:
        for node in PreOrderIter(tree):
            if node.is_leaf and node.name == key:
                for value in paths[key]:
                    if value == stop:
                        new = Node(value,parent=node)
                        print(new.ancestors[-1])
                        return True
                    else :
                        new = Node(value,parent=node)
    
    return False



root = Node(start)
next_guesses = get_next_words(root.name)
for guess in next_guesses:
    print(guess)
    if guess not in words_set:
        words_set.add(guess)
        node = Node(guess,parent=root)
good_first = input("good guesses? ").lower().strip()

if good_first == 'y':
    level = 1
    keep_going = add_levels(root, end, level)

    while(not keep_going):
        print('adding more levels')
        level += 1
        keep_going = add_levels(root, end,level)
    
    remove_bad_words()

else:
    remove_bad_words()

def add_words(word):

    added = input('Word to be added: ')
    words.add(word)
    pickle.dump(words, open("weaver_dictionary.pkl", "wb"))