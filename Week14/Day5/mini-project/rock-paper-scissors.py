from game import Game

def get_user_menu_choice():
    print("------Menu-------")
    print("(g) : Play a new game")
    print("(s) : Show scores")
    print("(x) : Quit")
    print("\n")

    choice = input("Enter choice: ").lower()
    if choice not in ['g', 's', 'x']:
        print("not a valid choice")
        print("\n")
        return ""
    else:
        return choice
    
def print_results(results):
    print(f"Wins : {results["Win"]}")
    print(f"Losses : {results["Loss"]}")
    print(f"Draws : {results["Draw"]}")
    print("\n")

def main():
    results = {
    "Win" : 0,
    "Loss": 0,
    "Draw": 0
    }

    party = Game()

    while True:
        choice = get_user_menu_choice()

        if choice == "x":
            break
        elif choice == "s":
            print_results(results)
        elif choice == "g":
            result = party.play()

            results[result] += 1

if __name__ == "__main__":
    main()