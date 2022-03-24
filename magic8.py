# https://www.codecademy.com/courses/learn-python-3/projects/python-magic-8-ball
import random

name = "Mohamed"
question = "Will I win the lottery?"
answer = ""
random_number = random.randint(1, 10)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Signs point to yes"
else:
  answer = "Error"

# All these three does the same
# if name: 
# if name != "": 
# if len(name) > 0: 

if name:
  if question:
    print(name + " asks: " + question)
  else:
    print("Dear " + name + " The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
  print("Question: " + question)

if name and question:
  print("Magic 8-Ball's answer: " + answer)
else:
  print("No name no answer for exclusive members only!")