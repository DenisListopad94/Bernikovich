
1.
class ChessPiece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def can_attack(self, x, y):
        raise NotImplementedError("Метод должен быть переопределен в подклассах")

class Queen(ChessPiece):
    def can_attack(self, x, y):
        if self.x == x or self.y == y or abs(self.x - x) == abs(self.y - y):
            return True
        return False

class Pawn(ChessPiece):
    def can_attack(self, x, y):
        if (self.color == "white" and (x == self.x + 1 and (y == self.y + 1 or y == self.y - 1))) or \
           (self.color == "black" and (x == self.x - 1 and (y == self.y + 1 or y == self.y - 1))):
            return True
        return False

class Knight(ChessPiece):
    def can_attack(self, x, y):
        if abs(x - self.x) * abs(y - self.y) == 2 and abs(x - self.x) != abs(y - self.y):
            return True
        return False