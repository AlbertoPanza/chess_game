class Piece:
    def __init__(self, color: str): # This says: When I make a Piece, it must know its color.
        self.color = color
    def get_legal_moves(self, position: tuple[int, int], board: list[list]):
        # To be overidden by subclasses
        pass
    def __str__(self):
        return "?"

class Pawn(Piece):
    def __init__(self, color: str):
        super().__init__(color) # Asks the parent constructor to set the color
        self.has_moved = False
    def get_legal_moves(self, position: tuple[int, int], board: list[list]):
        pass
    def __str__(self):
        return "♙" if self.color == "white" else "♟"