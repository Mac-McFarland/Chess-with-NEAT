
class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def get_valid_moves(self, board):
        #Get the number of valid moves on the board
        #Args: board 
        #Returns: number of valid moves
        raise NotImplementedError("Subclasses need to implement this method.")

    def move(self, row, col):
        #Move the piece to a specific position on the board
        #Args: row, col
        self.row = row
        self.col = col

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.has_moved = False

    def get_valid_moves(self, board):
        valid_moves = []
        direction = -1 if self.color == "white" else 1
        one_step_forward = (self.row + direction, self.col)
        if board.is_valid_position(*one_step_forward) and not board.is_piece_at(*one_step_forward):
            valid_moves.append(one_step_forward)

        two_steps_forward = (self.row + 2 * direction, self.col)
        if (
            not self.has_moved
            and board.is_valid_position(*two_steps_forward)
            and not board.is_piece_at(*two_steps_forward)
        ):
            valid_moves.append(two_steps_forward)

        capture_moves = [(self.row + direction, self.col - 1), (self.row + direction, self.col + 1)]
        for move in capture_moves:
            if board.is_valid_position(*move) and board.is_piece_at(*move) and board.get_piece(*move).color != self.color:
                valid_moves.append(move)

        return valid_moves

class Rook(Piece):
    def get_valid_moves(self, board):
        valid_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            for step in range(1, 8):
                move = (self.row + direction[0] * step, self.col + direction[1] * step)
                if not board.is_valid_position(*move):
                    break
                if not board.is_piece_at(*move):
                    valid_moves.append(move)
                else:
                    if board.get_piece(*move).color != self.color:
                        valid_moves.append(move)
                    break
        return valid_moves

class Knight(Piece):
    def get_valid_moves(self, board):
        valid_moves = []
        moves = [
            (self.row + 2, self.col + 1),
            (self.row + 2, self.col - 1),
            (self.row - 2, self.col + 1),
            (self.row - 2, self.col - 1),
            (self.row + 1, self.col + 2),
            (self.row + 1, self.col - 2),
            (self.row - 1, self.col + 2),
            (self.row - 1, self.col - 2),
        ]
        for move in moves:
            if board.is_valid_position(*move) and (not board.is_piece_at(*move) or board.get_piece(*move).color != self.color):
                valid_moves.append(move)
        return valid_moves

class Bishop(Piece):
    def get_valid_moves(self, board):
        valid_moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            for step in range(1, 8):
                move = (self.row + direction[0] * step, self.col + direction[1] * step)
                if not board.is_valid_position(*move):
                    break
                if not board.is_piece_at(*move):
                    valid_moves.append(move)
                else:
                    if board.get_piece(*move).color != self.color:
                        valid_moves.append(move)
                    break
        return valid_moves

class Queen(Piece):
    def get_valid_moves(self, board):
        valid_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            for step in range(1, 8):
                move = (self.row + direction[0] * step, self.col + direction[1] * step)
                if not board.is_valid_position(*move):
                    break
                if not board.is_piece_at(*move):
                    valid_moves.append(move)
                else:
                    if board.get_piece(*move).color != self.color:
                        valid_moves.append(move)
                    break
        return valid_moves

class King(Piece):
    def get_valid_moves(self, board):
        valid_moves = []
        moves = [
            (self.row + 1, self.col),
            (self.row - 1, self.col),
            (self.row, self.col + 1),
            (self.row, self.col - 1),
            (self.row + 1, self.col + 1),
            (self.row + 1, self.col - 1),
            (self.row - 1, self.col + 1),
            (self.row - 1, self.col - 1),
        ]
        for move in moves:
            if board.is_valid_position(*move) and (not board.is_piece_at(*move) or board.get_piece(*move).color != self.color):
                valid_moves.append(move)
        return valid_moves

