# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

text_censored = ""

def censor_words(text,words):
    new_text = text
    for term in words:
      new_text = new_text.replace(term, "XXXX")
      #print(term)
      #print(new_text)
   
#text2_censored = censor_words(email_two, proprietary_terms)
#print(text2_censored)


def censor_neg(text, negs, words, count):
    new_text2 = text
    counter = 0
    for neg in negs:
        if text.find(neg):
            counter += 1
            if counter >= count:
                print("Count hit")
                new_text2 = new_text2.replace(neg, "XXXX")
                
    
   censor_words(new_text2, words)    
     

text3_censored = censor_neg(email_three, negative_words, proprietary_terms, 2)
print(text3_censored)



