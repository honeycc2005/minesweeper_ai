class MinesweeperAI:
    def __init__(self, game):
        self.game = game
        self.safe_moves = set()
        self.mine_moves = set()

    def make_move(self):
        self.update_knowledge()
        if self.safe_moves:
            r, c = self.safe_moves.pop()
            is_mine = self.game.reveal(r, c)
            return is_mine
        else:
            return self.make_random_move()

    def update_knowledge(self):
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                if self.game.is_in_bounds(r, c) and self.game.get_cell(r, c) is not None:
                    self.update_cell_knowledge(r, c)

    def update_cell_knowledge(self, r, c):
        if self.game.get_cell(r, c) == 0:
            for rr, cc in self.game.get_neighbors(r, c):
                if (rr, cc) not in self.safe_moves and (rr, cc) not in self.mine_moves:
                    self.safe_moves.add((rr, cc))
        else:
            num_mines = self.game.adjacent_mines[r][c]
            num_flags = sum(1 for rr, cc in self.game.get_neighbors(r, c) if (rr, cc) in self.game.flags)
            if num_flags == num_mines:
                for rr, cc in self.game.get_neighbors(r, c):
                    if (rr, cc) not in self.game.flags and (rr, cc) not in self.safe_moves:
                        self.safe_moves.add((rr, cc))
            elif num_flags + len([1 for rr, cc in self.game.get_neighbors(r, c) if (rr, cc) not in self.game.revealed]) == num_mines:
                for rr, cc in self.game.get_neighbors(r, c):
                    if (rr, cc) not in self.game.flags and (rr, cc) not in self.safe_moves:
                        self.game.toggle_flag(rr, cc)
                        self.mine_moves.add((rr, cc))

    def make_random_move(self):
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                if (r, c) not in self.game.revealed and (r, c) not in self.game.flags:
                    is_mine = self.game.reveal(r, c)
                    return is_mine
        return False
