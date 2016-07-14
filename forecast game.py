import random
 
written = [""]
left  =  5
words = ['Orange','Apple','Cucumber','Little','Banana']
random = random.randint(0,4)
words_len = len(words[random])
data= raw_input("Write ok for start   = ")
number_of_letter_in_word = 0
if data == "ok":
    while True:
        if left == 0:
            print "Lose." 
            break
        if words_len == 0:
            print "Win."
            break
        print "                                                           "+str(left) + "left" 
        
        entry = raw_input(str(words_len) + " word left, enter a word  : ")
        
        if entry in words[random] and entry not in written:
            for  g in words[random]: 
                if g == entry:
                    number_of_letter_in_word = number_of_letter_in_word + 1
            words_len-=number_of_letter_in_word
        else:
            left-=1 
        written.append(entry)
        number_of_letter_in_word = 0
         
