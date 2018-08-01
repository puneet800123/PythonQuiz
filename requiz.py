import sys
def quiz_level(): #this function welcomes the player to select the difficulty level.
    print "\nHi! Welcome to Puneet Singh's quiz game.\n\nPlease choose your preferred difficulty level from the below metioned categories" #this statement is to ensure the smooth functioning of the game.
    easy_level=0
    medium_level=1
    hard_level=2
    easy_ques= "one __1__ three four __2__ six seven __3__ nine __4__" 
    easy_ans=["two","five","eight","ten"]
    medium_ques= "__1__ is the CEO of Google. \nCEO of facebook is __2__. \n__3__ and __4__ were the leading stars in TITANIC."
    medium_ans=["pichai", "zuckerberg", "leonardo", "winslet"]
    hard_ques="the most sensitive organ in body is __1__.the body has __2__ senses.__3__ is used to listen and __4__ is used to smell."
    hard_ans=["skin","five","ears","nose"]
    difficulty_level=int(raw_input("\nEasy = 0 \nMedium = 1 \nHard = 2\n")) #difficulty levels as the input from the player.
    if difficulty_level==easy_level:
        quiz(easy_ques,easy_ans)
    elif difficulty_level==medium_level:
        quiz(medium_ques,medium_ans)
    elif difficulty_level==hard_level:
        quiz(hard_ques,hard_ans)
"""
    Short description of behavior of quiz.

    Args:
        input1 (str): predefined question as input
        input2 (str): predefined ans as input

    Returns:
        result (str): If supplied answer and user input matches ,it goes for next blank
		if all are correct then message appears you won and games exits
"""    		

def quiz(ques,ans):#takes question and answer as input. Prompts user for answer.If supplied answer and user input matches ,it goes for next blank.
    chances=3                                       
    print "\n",ques
    max_blanks=4
    count=0 #this variable is defined to reach till the max_blanks.
    while count!=max_blanks:
        value="\n"+"answer "+str(count+1)+"\t"
        user_answer=str(raw_input(value)).lower()
        if user_answer == ans[count] :
            string="__"+str(count+1)+"__"
            ques=ques.replace(string,user_answer) 
            print "\n",ques
            count=count+1
        else:
            chances=decrement_chances(chances)
    print "\n All answers are correct!. You won.Congratulations!"
   
#NOW WE WILL DEFINE A FUNCTION CALLED decrement_chances WHICH WILL REDUCE THE CHANCES VALUE BY 1 IF THE USER ENTERS THE WRONG ANSWER. AND IF THE CHANCES LEFT ARE 0 THEN THE PROGRAM DISPLAYS A MESSAGE THAT THE PLAYER HAS LOST THE QUIZ.
def decrement_chances(chances):
 chances=chances-1 #this variable indicates the reduction of chances value by 1.
 print "\nCHANCES YOU ARE LEFT WITH ARE",chances
 if chances==0:
		print "\n YOU CHANCES ARE OVER FOR THIS QUIZ."
		print "\n GAMEOVER. TRY AGAIN."
		sys.exit(0)
 return chances
quiz_level()