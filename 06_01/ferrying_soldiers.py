"""
Ferrying Soldiers Puzzle Python Implementation
Robin Andrews - https://compucademy.net/
"""

NUM_SOLDIERS = 20


def print_state(state, moves_taken):
    print(("*" * 50))
    left_bank, right_bank, bank = state["left_bank"], state["right_bank"], state["bank"]
    print("#### FERRYING SOLDIERS PUZZLE - CURRENT STATE ####\n")
    print("Moves taken: ", moves_taken, "\n")
    print(left_bank['boys'], "boys,", left_bank['soldiers'], "soldiers | ", right_bank['boys'], "boys,",
          right_bank['soldiers'], "soldiers\n")
    print("Boat is on", bank, "bank")


def get_move(state):
    print("\nPuzzle options: \n")
    print("1. Ferry both boys from left to right bank")
    print("2. Ferry both boys from right to left bank")
    print("3. Ferry one boy from left to right bank")
    print("4. Ferry one boy from right to left bank")
    print("5. Ferry a soldier from left to right bank")
    print("6. Ferry a soldier from right to left bank\n")
    choice = 0
    while choice not in [1, 2, 3, 4, 5, 6]:
        try:
            choice = int(eval(input("Choose an action(1-4): ")))
        except:
            continue

    return choice


def process_move(move, state, moves_taken):
    # We can allow 1 boy, 2 boys or one soldier to cross only
    bank = state["bank"]
    legal_move = False
    # Move both boys from left to right bank
    if move == 1 and bank == "left":
        if state["left_bank"]["boys"] == 2:
            state["left_bank"]["boys"] -= 2
            state["right_bank"]["boys"] += 2
            legal_move = True
            state["bank"] = "right"
    elif move == 2 and bank == "right":
        if state["right_bank"]["boys"] == 2:
            state["right_bank"]["boys"] -= 2
            state["left_bank"]["boys"] += 2
            legal_move = True
            state["bank"] = "left"
    elif move == 3 and bank == "left":
        if state["left_bank"]["boys"] > 0:
            state["left_bank"]["boys"] -= 1
            state["right_bank"]["boys"] += 1
            legal_move = True
            state["bank"] = "right"
    elif move == 4 and bank == "right":
        if state["right_bank"]["boys"] > 0:
            state["right_bank"]["boys"] -= 1
            state["left_bank"]["boys"] += 1
            legal_move = True
            state["bank"] = "left"
    elif move == 5 and bank == "left":
        if state["left_bank"]["soldiers"] > 0:
            state["left_bank"]["soldiers"] -= 1
            state["right_bank"]["soldiers"] += 1
            legal_move = True
            state["bank"] = "right"
    elif move == 6 and bank == "right":
        if state["right_bank"]["soldiers"] > 0:
            state["right_bank"]["soldiers"] -= 1
            state["left_bank"]["soldiers"] += 1
            legal_move = True
            state["bank"] = "left"

    if legal_move:
        moves_taken += 1
        return state, moves_taken
    else:
        print("That move is not possible at this time.")
        return state, moves_taken


def is_win(state):
    return state == {"left_bank": {"boys": 2, "soldiers": 0},
                     "right_bank": {"boys": 0, "soldiers": NUM_SOLDIERS},
                     "bank": "left"}


def main():
    state = {"left_bank": {"boys": 2, "soldiers": NUM_SOLDIERS},
             "right_bank": {"boys": 0, "soldiers": 0},
             "bank": "left"}
    moves_taken = 0
    while not is_win(state):
        print_state(state, moves_taken)
        move = get_move(state)
        state, moves_taken = process_move(move, state, moves_taken)

    print("Well done - you solved the puzzle! You took", moves_taken, "moves.")


main()
