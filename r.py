import random
print("         RANDOM WORD WRITING GAME")
print("→→→→→→→ By Milankan Codes←←←←←")
print("****************************************")
positions = ["0th","1st","2nd","3rd","4th","5th"] 
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
pos_rand = random.randint(1,4) #4
let_rand = random.randint(0,25)  #21
#Corrected the index range
words = open('wordlist.txt','r')
word_list = words.read().splitlines()  # Read and split the word list
words_add=open('wordlist.txt','a')
position = positions[pos_rand] #4 4th
letter = letters[let_rand] #21 v
real_pos=int(pos_rand-1) #3
def ask_rate():
    print("****************************************")
    print("****************************************")
    print("Please rate our code (Out of 10)")
    rate=int(input("→"))
    if rate>=10:
        print("You rated",str(rate[0]),"/10","(It was Assigned)")
        print("Please Tell Us what needed to be changed? or hit enter to skip")
        param0=str(input("→"))
        if param0=="":
            print("Or you can send feedback at milankan.official@gmail.com")
    elif rate<=4:
        print("You rated",rate,"/10")
        print("Please Tell Us what needed to be changed? or hit enter to skip")
        param=str(input("→"))
        if param=="":
            print("Or you can send feedback at milankan.official@gmail.com")
    elif rate>=4 and rate<=7:
        print("You rated",rate,"/10")
        print("Seems to be somehow disturbed!Tell Us how. Or hit enter to skip")
        param2=str(input("→"))
        if param=="":
            print("Or You can Send feedback at @milankan.official@gmail.com")
    elif rate<=10:
        print("You rated",rate,"/10")
        print("Thank You, If any upgradation needed please tell us at milankan.official@gmail.com")
    print("｡ﾟﾟ･｡･ﾟﾟ｡")
    print("ﾟ。  From Milankan Codes")
    print("  ･｡･")
def get_inp():
    pos_rand= random.randint(1,4)
    let_rand= random.randint(0,25)
    position=positions[pos_rand]
    letter=letters[let_rand]
    print("Write a word with ",position,"letter as -",letter)
    user_word=input("→")
    if user_word in word_list:
        if user_word[positions.index(positions[pos_rand])-1] == letter:
            print("Correct Answer!")
            print("****************************************")
            get_inp()
        else:
            print("GAME OVER!!")
            print("****************************************")
            print("Refresh For a new Game!!")
            ask_rate()
    else:
        print("GAME OVER!!")
        print("****************************************")
        print("No such word found")
        print("If such word exist please add to the dictionary.If you want to add-",user_word,",hit enter")
        new_word=str(input("→"))
        if new_word=="":
            words_add.write(user_word)
            print(user_word,"was added")
            added_word=user_word
        else:
            words_add.write(new_word)
            if new_word in word_list:
                print(new_word,"was added")
                added_word=new_word
            else:
                print('An error occurred , Sorry!')
        print("Thanks for helping to add word",added_word)
        ask_rate()

if __name__=="__main__":
    get_inp()