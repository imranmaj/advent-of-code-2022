# part 1
BEATS = {
    "X": "C",
    "Y": "A",
    "Z": "B"
}
DRAWS = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}
MOVE_SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
with open("input.txt") as f:
    lines = f.readlines()
score = 0
for line in lines:
    if line.isspace():
        continue
    opp, me = line.strip().split()
    if BEATS[me] == opp:
        score += 6
    elif DRAWS[me] == opp:
        score += 3
    score += MOVE_SCORE[me]
print(score)

# part 2
MOVE = {
    "A": {
        "X": "S",
        "Y": "R",
        "Z": "P"
    },
    "B": {
        "X": "R",
        "Y": "P",
        "Z": "S"
    },
    "C": {
        "X": "P",
        "Y": "S",
        "Z": "R"
    }
}
MOVE_SCORE = {
    "R": 1,
    "P": 2,
    "S": 3
}
with open("input.txt") as f:
    lines = f.readlines()
score = 0
for line in lines:
    if line.isspace():
        continue
    opp, result = line.strip().split()
    if result == "X":
        score += 0
    elif result == "Y":
        score += 3
    elif result == "Z":
        score += 6
    score += MOVE_SCORE[MOVE[opp][result]]
print(score)
