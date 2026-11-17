import time 
import random 
from colorama import Fore,Style, init

init(autoreset=True)

sentences = [
    "Robotics Club of Valmiki is simply the best!!!",
    "We will be having pizza, why are you even here lol?",
    "Sakxem is so peak, words cannot describe his vibe",
    "Who doesn't love 3d printers? That's just crazy!",
    "Roshan got his Hack Club shirt and loves it so much", 
    "Aayush Poudel has so many fans in grade twelve lol",
    "Hack Club is so goated, nothing beats its vibe!!",
    "Life is so peak, but I still think about her lol",
    "Life is beautiful when you find your own purpose!"
]

target= random.choice(sentences)

print(Fore.CYAN + "===================================================================")
print(Style.BRIGHT + Fore.GREEN + "                    RCoV TYPING ARENA                       ")
print(Fore.CYAN + "===================================================================")
print("Type the sentence as fast and accurately as you can!\n")


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
