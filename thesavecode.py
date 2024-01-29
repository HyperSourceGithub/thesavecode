import random
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

savecode = None
count = 0
hamburger = None
bullets = 0

def generate_randoms(counter):
  for x in range(counter):
    rand = f"{random.randint(0,counter)}{x}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters).upper()}{random.choice(letters).upper()}{random.choice(letters).upper()}{random.choice(letters).upper()}"
  return rand

mode = input("Enter mode (read/write): ").lower()

if mode == "write":
  upto = input("Enter a number to count up to (max 4 digits): ")
  maxcount = upto[0:4]
  print(" ")
  while (count < int(maxcount)):
    print ("\033[A\033[A")
    count += 1
    print(f"Count: {count}")


  food = input("Enter yes/no: ").lower()
  if food == "yes":
    hamburger = "yes"
  elif food == "no":
    hamburger == "-no"
  else: 
    print("Error: invalid answer, defaulting to yes")

  load = input("Enter magazine bullet count for pistol (max 4 digits): ")
  maxbullets = load[0:4]
  print(" ")
  while (bullets < int(maxbullets)):
    print ("\033[A\033[A")
    bullets += 1
    print(f"Bullets: {bullets}")

  print("Generating save code...")
  savecode = f"{count}{hamburger}{bullets}{generate_randoms(random.randint(0,50000))}"
  print(f"Save code: {savecode}")

elif mode == "read":
  savecode = input("Enter save code: ")
  count = savecode[0:4]
  hamburger = savecode[4:7]
  bullets = savecode[7:11]
  if hamburger == "yes":
    print(f'''
Count: {count}
Hamburger: Yes
Bullets: {bullets}
''')
  elif hamburger == "-no":
    print(f'''
Count: {count}
Hamburger: No
Bullets: {bullets}
''')
else:
  print("Invalid mode. Please restart the program.")

