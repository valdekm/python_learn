f = open("scores.txt", "w")

while True:
    participant = raw_input("participant name > ")

    if participant == "quit":
        print("Quitting...")
        break

    score = raw_input("Score for " + participant + "> ")
    f.write(participant + "," + score + "\n")

f.close()

f = open("scores.txt", "r")
for line in f:
    print(line.strip())
    #print(line)
