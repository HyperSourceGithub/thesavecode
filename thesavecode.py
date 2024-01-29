savecode = None
count = 0
hamburger = None
bullets = 0

mode = input("Enter mode (read/write): ").lower()

if mode == "write":
  upto = input("Enter a number to count up to (max 4 digits): ")
  while (count < upto[1:4]):
    print(f"Count: {count}", end = '\r')

  food = input("Enter yes/no: ").lower()
  if food == "yes":
    hamburger = "yes"
  elif food == "no":
    hamburger == "-no"
  else: 
    print("Error: invalid answer, defaulting to yes")

  load = input("Enter magazine bullet count for pistol (max 4 digits): ")
  while (bullets < load[1:4]):
    print(f"Bullets: {bullets}", end = '\r')

  print("Generating save code...")
  savecode = f"{count}{hamburger}{bullets}"
  print(f"Save code: {savecode}")

elif mode == "read":
  savecode = input("Enter save code: ")
  count = savecode[1:4]
  hamburger = savecode[5:7]
  bullets = savecode[8:11]
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

