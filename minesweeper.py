import random

class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.flags = set()
        self.revealed = set()
        self._place_mines()
        self._calculate_adjacent_mines()

    def _place_mines(self):
        while len(self.mines) < self.num_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if (r, c) not in self.mines:
                self.mines.add((r, c))

    def _calculate_adjacent_mines(self):
        self.adjacent_mines = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r, c in self.mines:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < self.rows and 0 <= cc < self.cols:
                        self.adjacent_mines[rr][cc] += 1

    def reveal(self, r, c):
        if (r, c) in self.revealed or (r, c) in self.flags:
            return False
        if (r, c) in self.mines:
            return True
        self._reveal_recursive(r, c)
        return False

    def _reveal_recursive(self, r, c):
        if (r, c) in self.revealed or (r, c) in self.mines:
            return
        self.revealed.add((r, c))
        if self.adjacent_mines[r][c] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < self.rows and 0 <= cc < self.cols:
                        self._reveal_recursive(rr, cc)

    def toggle_flag(self, r, c):
        if (r, c) in self.flags:
            self.flags.remove((r, c))
        else:
            self.flags.add((r, c))

    def display(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.flags:
                    print('F', end=' ')
                elif (r, c) not in self.revealed:
                    print('.', end=' ')
                elif (r, c) in self.mines:
                    print('M', end=' ')
                else:
                    print(self.adjacent_mines[r][c], end=' ')
            print()

    def is_solved(self):
        return len(self.revealed) == self.rows * self.cols - self.num_mines

    def get_neighbors(self, r, c):
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < self.rows and 0 <= cc < self.cols:
                    neighbors.append((rr, cc))
        return neighbors

    def is_in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def get_cell(self, r, c):
        if self.is_in_bounds(r, c):
            if (r, c) in self.revealed:
                return self.adjacent_mines[r][c]
            else:
                return None
        else:
            return None
