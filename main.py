import random

questions = [
    ["What is the capital of France?\nA. Berlin\nB. Madrid\nC. Paris\nD. Rome", "C"],
    ["How many sides does a hexagon have?\nA. 5\nB. 6\nC. 7\nD. 8", "B"],
    ["What is 12 x 12?\nA. 132\nB. 144\nC. 124\nD. 148", "B"],
    ["What is the largest planet in the solar system?\nA. Saturn\nB. Neptune\nC. Earth\nD. Jupiter", "D"],
    ["What is the chemical symbol for water?\nA. HO\nB. H2O\nC. CO2\nD. H3O", "B"],
    ["How many continents are on Earth?\nA. 5\nB. 6\nC. 7\nD. 8", "C"],
    ["What is the fastest land animal?\nA. Lion\nB. Horse\nC. Cheetah\nD. Leopard", "C"],
    ["How many days in a leap year?\nA. 365\nB. 366\nC. 364\nD. 367", "B"],
    ["What color is the sun?\nA. Yellow\nB. Orange\nC. Red\nD. White", "D"],
    ["How many bones are in the human body?\nA. 207\nB. 206\nC. 212\nD. 198", "B"],
]

guesses = []
chosen_index = int(input("How many questions would you like to play? (1-10): "))
picked_quetions = random.sample(questions, chosen_index)
Correct = 0 
incorrect = 0 


question_nummer = 1
for question in picked_quetions: 
   print ("------------------------------")
   print (f"{question_nummer} / {chosen_index}")      #to print the 1/10 Titel 
   print (question [0])  
   guess = input("Enter (A, B, C, D):  ").upper()  
   guesses.append (guess)                             #to Print the Answers Later 
   if guess == question[1]:
    print ("CORRECT!")
    Correct = Correct + 1
    question_nummer += 1 
   else : 
     print (f"INCORRECT ! The answer was {question[1]}")
     incorrect = Correct - 1 
     question_nummer += 1 


print ("----------------------")
print ("       RESULT         ")  
print ("----------------------")

answers = []
for answer in picked_quetions: 
   answers.append(answer [1])
answers = ','.join(answers)
guesses = ','.join(guesses)

print (f"Input:- {guesses}")
print (f"Answers- {answers}")
print("----------------------------------")
total_percentage =  Correct / chosen_index *100   

print (f"Total_Point = {total_percentage :2}%")

if total_percentage < 50: 
  print ("--->>>> Lets Try Again !! ")
if total_percentage > 80: 
  print ("*** YOU ARE GENIUS!!")
if total_percentage >= 50 and total_percentage < 80: 
  print ("*** VERY GOOD JOB! ")
