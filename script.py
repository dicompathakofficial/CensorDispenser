###### PROBLEM SET ######
# Task 1: Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.
# Task 2: Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well.


# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# Lowercasing all the emails
lower_case_email_one = email_one.lower()
lower_case_email_two = email_two.lower()
lower_case_email_three = email_three.lower()
lower_case_email_four = email_four.lower()

# Words to work on/variables
word_to_censor = ["learning algorithms"]
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]


# converting all the lowercase emails into functions
def first_email():
    return lower_case_email_one


def second_email():
    return lower_case_email_two


def third_email():
    return lower_case_email_three


def fourth_email():
    return lower_case_email_four


# CODE on Just Censoring a [list] of word(s)

def censorship(lower_case_email):
    email = lower_case_email
    for words in proprietary_terms:
        if words in email:
            mail = email.replace(words, "CENSORED")
            email = mail
    return email


# CODE on removing both negative words occuring twie or more than twice and censoring everything on proprietory_terms variable

def negativity(lower_case_email):
    email = lower_case_email
    for words in negative_words:
        if email.count(words) >= 1:
            mail = email.replace(words, "CENSORED")
            email = mail

    for words in proprietary_terms:
        if words in email:
            mail = email.replace(words, "CENSORED")
            email = mail

    return email


###### TEST AREA ######
# print(function_to_use(on the email on which to use))
print(negativity(fourth_email()))
