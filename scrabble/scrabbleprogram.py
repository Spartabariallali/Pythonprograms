# base scrabble word calculator instructions
# given the below scoring create a scrabble word calculator 
# that will provide the corect scored dependent on the string provided



scrabble_word = str(input("please enter a scrabble word:\n ")).lower()

one = ["a","e","i","o","u","l","n","r","s","t"]
two = ["d","d"]
three = ["b","c","m","p"]
four = ["k","h","v","w","y"]
five = ["k"]
eight = ["j","k"]
ten = ["q","z"]

def word_calc(scrabble_word):
    score = 0

    for letter in scrabble_word:
        if letter in one:
            score += 1
        elif letter in two:
            score += 2
        elif letter in three:
            score += 3
        elif letter in four:
            score += 4
        elif letter in five:
            score += 5
        elif letter in eight:
            score += 8
        elif score in ten:
            score += 10        
    
    return score 


print(word_calc(scrabble_word))

