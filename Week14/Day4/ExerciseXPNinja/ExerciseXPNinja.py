import copy

class GameOfLife:
    def __init__(self, width, height, initial_state):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.next_board = [[0] * width for _ in range(height)]
        self.initialize_board(initial_state)

    def initialize_board(self, initial_state):
        for row, col in initial_state:
            self.board[row][col] = 1

    def print_board(self):
        for row in self.board:
            print(" ".join("■" if cell else "□" for cell in row))
        print()

    def count_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r = row + dr
            c = col + dc
            if 0 <= r < self.height and 0 <= c < self.width and self.board[r][c] == 1:
                count += 1
        return count

    def apply_rules(self):
        for r in range(self.height):
            for c in range(self.width):
                neighbors = self.count_neighbors(r, c)
                if self.board[r][c] == 1:  # Cell is alive
                    if neighbors < 2 or neighbors > 3:
                        self.next_board[r][c] = 0  # Dies
                    else:
                        self.next_board[r][c] = 1  # Lives on
                else:  # Cell is dead
                    if neighbors == 3:
                        self.next_board[r][c] = 1  # Becomes alive
                    else:
                        self.next_board[r][c] = 0  # Stays dead

    def update_board(self):
        self.board = copy.deepcopy(self.next_board)

    def run(self, generations):
        for generation in range(generations):
            print(f"Generation {generation + 1}:")
            self.print_board()
            self.apply_rules()
            self.update_board()

# Example usage:
initial_state = [(1, 1), (1, 2), (2, 1), (2, 2), (6, 6), (6, 7), (7, 6), (7, 7)]  # Blinker oscillator
game = GameOfLife(10, 10, initial_state)
game.run(10)  # Run for 10 generations
