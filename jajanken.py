import time
import random

print("******* Jajanken Game *******\n")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player = input("Enter Player Name: ")
print(player + "\n" + " VS " + "\n" + "CPU\n")

value = input("choose between rock, paper, scissors: ")

print("ROCK\n" + rock)
time.sleep(1)
print("PAPER\n" + paper)
time.sleep(1)
print("SCISSORS\n" + scissors)
time.sleep(1)

print("\n" + player + ":\n")

if value == "rock":
    print(rock)
elif value == "paper":
    print(paper)
elif value == "scissors":
    print(scissors)
else:
    print("Cosa non hai capito del gioco?")

print("\nCPU\n")

cpu = random.choice(["rock", "paper", "scissors"])

if cpu == "rock":
    print(rock)
elif cpu == "paper":
    print(paper)
else:
    print(scissors)

if cpu == "rock" and value == "scissors":
    print("CPU WIN")
elif cpu == "paper" and value == "rock":
    print("CPU WIN")
elif cpu == "scissors" and value == "paper":
    print("CPU WIN")
elif cpu == "paper" and value == "scissors":
    print(player + " WIN")
elif cpu == "scissors" and value == "rock":
    print(player + " WIN")
elif cpu == "rock" and value == "paper":
    print(player + " WIN")
else:
    print("SPARE")
