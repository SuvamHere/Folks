
import time
import random
from colorama import Fore, Style, init

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
    "When I am far from home,don't call me on phone"
]

best_wpm = 0
playing = True

while playing:

    target = random.choice(sentences)

    print(Fore.CYAN + "===================================================================")
    print(Style.BRIGHT + Fore.GREEN + "                    RCoV TYPING ARENA")
    print(Fore.CYAN + "===================================================================")
    print("Type the sentence as fast and accurately as you can!\n")

    print("\nGet ready...")
    time.sleep(0.9)
    print(Style.BRIGHT + Fore.RED + "  3...")
    time.sleep(0.9)
    print(Style.BRIGHT + Fore.YELLOW + "  2...")
    time.sleep(0.9)
    print(Style.BRIGHT + Fore.GREEN + "  1... GO!")
    time.sleep(0.5)

    print(Fore.CYAN + "\nTYPE THIS:")
    print(f"  {target}\n")

    input("Press Enter when you are ready to start the timer...")

    start_time = time.time()
    typed = input(": ")
    end_time = time.time()

    elapsed_seconds = max(end_time - start_time, 0.1)
    minutes = elapsed_seconds / 60

    word_count = len(typed) / 5
    wpm = word_count / minutes

    correct_characters = 0

    for target_char, typed_char in zip(target, typed):
        if target_char == typed_char:
            correct_characters += 1

    accuracy = (correct_characters / len(target)) * 100

    if wpm > best_wpm:
        previous_wpm = best_wpm
        best_wpm = wpm
        new_record = True
    else:
        new_record = False

    print("\n" + Fore.CYAN + "========================== YOUR RESULTS ===========================")
    print(f"Time Taken : {round(elapsed_seconds, 2)} seconds")
    print(f"Speed      : {round(wpm, 1)} WPM")
    print(f"Accuracy   : {round(accuracy, 1)}%")
    print(f"High Score : {round(best_wpm, 1)} WPM")
    print(Fore.CYAN + "===================================================================")
    if new_record:
        print(Style.BRIGHT + Fore.GREEN + "\nNEW HIGH SCORE!")
        print(Fore.YELLOW + f"Previous Best : {round(previous_wpm, 1)} WPM")
        print(Fore.GREEN + f"New Best      : {round(best_wpm, 1)} WPM")
        
    if typed == target:
        print(Style.BRIGHT + Fore.GREEN + "Flawless! Every single character matched!")
    else:
        print(Fore.RED + "\nWhere you missed:")
        print(f"  Target: {target}")
        print(f"  You   : {typed}")

    again = input("\nPlay another round? (y/n): ").strip().lower()

    if again != "y":
        print(Fore.CYAN + "\nThanks for playing! And W Hack Club!")
        playing = False

    print("")
