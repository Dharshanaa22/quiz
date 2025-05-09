print("Guess it")
c = 0
ready = input("Ready to begin...?? (Yes/No): ").strip().lower()

if ready != "yes":
    print("Okay, bye!")
    quit()

print("\nLet's start!\n")

a = input("1. What gets wetter the more it dries? ").strip().lower()
if  a == "towel":
    print("Correct")
    c += 1
else:
    print("Incorrect")
print("You scored", c, "out of 1\n")

a = input("2. What comes once in a minute, twice in a moment, but never in a thousand years? ").strip().lower()
if a == "m":
    print("Correct")
    c += 1
else:
    print("Incorrect")
print("You scored", c, "out of 2\n")

a = input("3. I’m not alive, but I grow. I don’t have lungs, but I need air. What am I? ").strip().lower()
if a == "fire":
    print("Correct")
    c += 1
else:
    print("Incorrect")
print("You scored", c, "out of 3\n")

a = input("4. I have keys but no locks. I have space but no room. You can enter but can’t go outside. What am I? ").strip().lower()
if a == "keyboard":
    print("Correct")
    c += 1
else:
    print("Incorrect")
print("You scored", c, "out of 4\n")

a = input("5. The more of me you take, the more you leave behind. What am I? ").strip().lower()
if a == "footsteps":
    print("Correct")
    c += 1
else:
    print("Incorrect")
print("You scored", c, "out of 5")

print("\nThanks for playing!")
