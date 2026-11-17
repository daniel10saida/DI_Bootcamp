def display_hangman(mistakes=6):
    parts = [" ", " ", " ", " ", " ", " "]
    symbols = ["O", "|", "/", "\\", "/", "\\"]

    for i in range(mistakes):
        parts[i] = symbols[i]

    print("  +---+")
    print("  |   |")
    print(f"  |   {parts[0]}")
    print(f"  |  {parts[2]}{parts[1]}{parts[3]}")
    print(f"  |  {parts[4]} {parts[5]}")
    print("__|_____")

display_hangman()