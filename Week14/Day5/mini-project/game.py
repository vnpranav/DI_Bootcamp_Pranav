class Game:
    def __init__(self):
        self.items = ['r', 'p', 's']

    def __get_user_item(self):
        valid = False
        while valid == False:
            item = input("Select (r)ock, (p)aper or (s)cissors: ").lower()

            if item in self.items:
                valid = True
                return item
            else:
                print("Enter only one of the options")

    def __get_computer_item(self):
        from random import choice
        return choice(self.items) 
    
    def get_game_result(self, user_item, computer_item):
        roll = (user_item, computer_item)
        win = [('r', 's'), ('s', 'p'), ('p', 'r')]
        draw = [('r', 'r'), ('p', 'p'), ('s','s')]

        if roll in win:
            return 'Win'
        elif roll in draw:
            return 'Draw'
        else:
            return 'Loss'

    def play(self):
        self.user = self.__get_user_item()
        self.computer = self.__get_computer_item()
        self.result = self.get_game_result(self.user, self.computer)

        print(f"You chose: {self.user}")
        print(f"Computer chose: {self.computer}")
        print(f"Result : {self.result}")

        return self.result