import random

def possible_riddles():
    riddles = [
        {
            "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "answer": "an echo"
        },
        {
            "question": "The more you take, the more you leave behind. What am I?",
            "answer": "footsteps"
        },
        {
            "question": "What has a heart that doesn’t beat?",
            "answer": "an artichoke"
        }
        # Add more riddles as needed
    ]
    return riddles

def present_riddle():
    riddles = possible_riddles()
    selected_riddle = random.choice(riddles)
    print(selected_riddle["question"])
    player_answer = input("Your answer: ").lower()

    if player_answer == selected_riddle["answer"]:
        print("You solved the riddle.")
        return True
    else:
        print("Incorrect. The correct answer is:", selected_riddle["answer"])
        return False