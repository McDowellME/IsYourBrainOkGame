#!/user/bin/env python3

""" Game to determine if your brain is ok from this pandemic """

# questions dictionary with question, choices, and scores
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

# ask questions, build question format
def askquestion(qno) :
    q = questions[qno]["question"]
    a = questions[qno]["choice"]["a"]["answer"]
    b = questions[qno]["choice"]["b"]["answer"]
    c = questions[qno]["choice"]["c"]["answer"]

    response = input(f"\n{q}\nYour choices are: \nA: {a} \nB: {b} \nC: {c} \nYour Answer ->  ").lower()

    return response

# calculate brain_meter by getting score based on response
def calculatemeter(qno, brain_meter):
    response = ""
    choices = questions[qno]["choice"]

    while response == "" or response not in choices:
        response = askquestion(qno)
        if response == "" or response not in choices:
            print("\nYour brain is not ok. Try again.") 

    brain_meter += choices[response]["score"]
    return brain_meter

# tell user how their brain scored
def isyourbrainok() :  
    
    brain_meter = 0

    # run for each question, redefine brain_meter after each
    for question in questions:
        brain_meter = calculatemeter(question, brain_meter)

    print()

    if brain_meter == 0:
        print("Your brain is definitely not ok.")
    elif brain_meter == 6:
        print("Your brain is totally ok.")
    else:
        print("You need a little brain healing")

def main() :
    isyourbrainok()

main()