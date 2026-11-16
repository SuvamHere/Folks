import time 
import random 

sentences = [
    "Robotics Club of Valmiki is the best and nothing comes close",
    "We are going to have a pizza anytime now ",
    "Hey there stranger why are u here lol",
    "Sakxem is so peak gang i can't appreciate him enough",
    "Who don't love 3D printer like what is wrong with you",
    "Roshan GC got his HC campfire Tshirt and he is happy with it lol",
    "Aayush Poudel is loved by 50 girls of class 12",
    "Hack Club is so goated i can't stop talking good about it",
    "This is so peak yet I still think about her",
]

target= random.choice(sentences)

print("-----------------------TERMINAL TYPING TEST-----------------------")
print("Type the sentence below as fast and accurately as you can..\n")


print("\nTYPE THIS:")
print(f"  {target}\n")
input("Press Enter when you are ready to start the timer...")


start_time = time.time()
typed= input("GO: ")
end_time = time.time()

elapsed_seconds = max(end_time - start_time,0.1)
minutes = elapsed_seconds/60

word_count = len(typed)/5
wpm = word_count/minutes

corect_characters = 0 

for target_char, typed_char in zip(target,typed):
    if target_char == typed_char:
        corect_characters +=1

accuracy = (corect_characters/ len(target)) * 100

print("\n==== YOUR RESULTS =====")
print(f"time taken: {elapsed_seconds:.2f} seconds")
print(f"Speed: {wpm:.1f} WPM (Words Per Minute)")
print(f"Accuracy: {accuracy:.1f}%")

if typed == target:
    print("Flawless! Every single character matched")
