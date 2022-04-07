#!/user/bin/env python3

""" Game to determine if your brain is ok from this pandemic """


# questions and answers
# DONE: make dict
q1 = "When you meet somebody new, how do you greet them?"
q1a = "Hello!" # 2
q1b = "Goodbye!" # 1
q1c = "Potato!" # 0

q2 = "A friend has invited you to brunch; how do you respond?"
q2a = 'Say "Sure", knowing you absolutely will not show up.' # 1
q2b = 'Say "That will be lovely", then go to brunch.' # 2
q2c = "Hide in your closet." # 0

q3 = "What kind of pants are you wearing?" 
q3a = "Pajama" # 1
q3b = "Slacks or Jeans" # 2
q3c = "None" # 0

questions = {
    "q1": 
    {"question": "When you meet somebody new, how do you greet them?", 
    "choice": {
        "a": {"answer": "Hello!", "score": 2}, 
        "b": {"answer": "Goodbye!", "score": 1}, 
        "c": {"answer": "Potato!", "score": 0}
            }
    }, 
    "q2":
    {"question": "A friend has invited you to brunch; how do you respond?", 
    "choice": {
        "a": {"answer": 'Say "Sure", knowing you absolutely will not show up.', "score": 1}, 
        "b": {"answer": 'Say "That will be lovely", then go to brunch.', "score": 2}, 
        "c": {"answer": "Hide in your closet.", "score": 0}
            }
    },
    "q3":
    {"question": "What kind of pants are you wearing?", 
    "choice": {
        "a": {"answer": "Pajama", "score": 1}, 
        "b": {"answer": "Slacks or Jeans", "score": 2}, 
        "c": {"answer": "None", "score": 0}
            }
    }
            }
# build question format
def questionbuilder(qno) :
    q = questions[qno]["question"]
    a = questions[qno]["choice"]["a"]["answer"]
    b = questions[qno]["choice"]["b"]["answer"]
    c = questions[qno]["choice"]["c"]["answer"]

    question = input(f"{q}\nYour choices are: \nA: {a} \nB: {b} \nC: {c} \nYour Answer ->  ").lower()

    return question

# ask questions, each answer associates ok or not ok brain
def askquestions() :        
    q1response = questionbuilder("q1")
    q2response = questionbuilder("q2")
    q3response = questionbuilder("q3")

    # brain meter
    brain_meter = 0

    # calculate brain_meter
    while q1response != "c":
        if q1response == "a":
            brain_meter += 2
            break
        else: 
            brain_meter += 1
            break

    while q2response != "c":
        if q2response == "a":
            brain_meter += 1
            break
        else:
            brain_meter += 2
            break

    while q3response != "c":
        if q3response == "a":
            brain_meter += 1
            break
        else:
            brain_meter += 2
            break
    
    if brain_meter == 0:
        print("Your brain is definitely not ok.")
    elif brain_meter == 6:
        print("Your brain is totally ok.")
    else:
        print("You need a little brain healing")

def main() :
    askquestions()

main()