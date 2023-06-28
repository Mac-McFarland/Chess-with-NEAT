import pygame
from board import Board
from piece import Piece

pygame.init()

# Display
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chess Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (232, 235, 239)
DARK_SQUARE = (125, 135, 150)


# Board dimensions
board_size = min(screen_width, screen_height)
board_offset_x = (screen_width - board_size) // 2
board_offset_y = (screen_height - board_size) // 2
square_size = board_size // 8

pawnb_img = pygame.image.load("pieces/pawnb.png")
rookb_img = pygame.image.load("pieces/rookb.png")
knightb_img = pygame.image.load("pieces/knightb.png")
bishopb_img = pygame.image.load("pieces/bishopb.png")
queenb_img = pygame.image.load("pieces/queenb.png")
kingb_img = pygame.image.load("pieces/kingb.png")

pawnw_img = pygame.image.load("pieces/pawnw.png")
rookw_img = pygame.image.load("pieces/rookw.png")
knightw_img = pygame.image.load("pieces/knightw.png")
bishopw_img = pygame.image.load("pieces/bishopw.png")
queenw_img = pygame.image.load("pieces/queenw.png")
kingw_img = pygame.image.load("pieces/kingw.png")

# Resize the images to fit the square size
scale_factor = 0.6  # Adjust this value to set the desired percentage (e.g., 0.6 for 60%)
scaled_square_size = int(square_size * scale_factor)

# Resize the images to the scaled square size
pawnb_img = pygame.transform.scale(pawnb_img, (scaled_square_size, scaled_square_size))
rookb_img = pygame.transform.scale(rookb_img, (scaled_square_size, scaled_square_size))
knightb_img = pygame.transform.scale(knightb_img, (scaled_square_size, scaled_square_size))
bishopb_img = pygame.transform.scale(bishopb_img, (scaled_square_size, scaled_square_size))
queenb_img = pygame.transform.scale(queenb_img, (scaled_square_size, scaled_square_size))
kingb_img = pygame.transform.scale(kingb_img, (scaled_square_size, scaled_square_size))

pawnw_img = pygame.transform.scale(pawnw_img, (scaled_square_size, scaled_square_size))
rookw_img = pygame.transform.scale(rookw_img, (scaled_square_size, scaled_square_size))
knightw_img = pygame.transform.scale(knightw_img, (scaled_square_size, scaled_square_size))
bishopw_img = pygame.transform.scale(bishopw_img, (scaled_square_size, scaled_square_size))
queenw_img = pygame.transform.scale(queenw_img, (scaled_square_size, scaled_square_size))
kingw_img = pygame.transform.scale(kingw_img, (scaled_square_size, scaled_square_size))

# Chess piece class
class Piece:
    def __init__(self, color, image, row, col):
        self.color = color
        self.image = image
        self.row = row
        self.col = col

    def draw(self):
        x = board_offset_x + self.col * square_size
        y = board_offset_y + self.row * square_size
        screen.blit(self.image, (x, y))


        
    def move(self, row, col):
        self.row = row
        self.col = col    

# Create chess pieces
pieces = [
    # White pieces
    Piece("white", rookw_img, 7, 0),  
    Piece("white", rookw_img, 7, 7),
    Piece("white", knightw_img, 7, 1), 
    Piece("white", knightw_img, 7, 6),
    Piece("white", bishopw_img, 7, 2),  
    Piece("white", bishopw_img, 7, 5),
    Piece("white", queenw_img, 7, 3),  
    Piece("white", kingw_img, 7, 4),  
    Piece("white", pawnw_img, 6, 0),  
    Piece("white", pawnw_img, 6, 1),
    Piece("white", pawnw_img, 6, 2),
    Piece("white", pawnw_img, 6, 3),
    Piece("white", pawnw_img, 6, 4),
    Piece("white", pawnw_img, 6, 5),
    Piece("white", pawnw_img, 6, 6),
    Piece("white", pawnw_img, 6, 7),

    # Black pieces
    Piece("black", rookb_img, 0, 0),  
    Piece("black", rookb_img, 0, 7),
    Piece("black", knightb_img, 0, 1), 
    Piece("black", knightb_img, 0, 6),
    Piece("black", bishopb_img, 0, 2), 
    Piece("black", bishopb_img, 0, 5),
    Piece("black", queenb_img, 0, 3),  
    Piece("black", kingb_img, 0, 4),  
    Piece("black", pawnb_img, 1, 0),  
    Piece("black", pawnb_img, 1, 1),
    Piece("black", pawnb_img, 1, 2),
    Piece("black", pawnb_img, 1, 3),
    Piece("black", pawnb_img, 1, 4),
    Piece("black", pawnb_img, 1, 5),
    Piece("black", pawnb_img, 1, 6),
    Piece("black", pawnb_img, 1, 7),
]

#In this code, we handle mouse clicks in the game loop. 
# When the left mouse button is clicked, we determine the row 
# and column on the chessboard where the click occurred. 
# We then check if there is a piece at that position. 
# If a piece is clicked and no other piece is currently selected, 
# we mark it as the selected piece. If a piece is already selected 
# and a different piece of a different color is clicked, 
# we attempt to move the selected piece to the clicked position.
running = True
selected_piece = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row = (mouse_y - board_offset_y) // square_size
            clicked_col = (mouse_x - board_offset_x) // square_size

            if selected_piece is None:
                # Select a piece if clicked on a valid piece
                for piece in pieces:
                    if piece.row == clicked_row and piece.col == clicked_col:
                        if piece.color == turn:  # Ensure it is the player's turn
                            selected_piece = piece
                            selected_piece.selected = True
                        break
            else:
                # Move the selected piece or capture opponent's piece
                if (clicked_row, clicked_col) in selected_piece.get_valid_moves():
                    # Move the selected piece to the clicked position
                    selected_piece.move(clicked_row, clicked_col)

                    # Check for capturing opponent's piece
                    for piece in pieces:
                        if piece.row == clicked_row and piece.col == clicked_col and piece.color != selected_piece.color:
                            pieces.remove(piece)
                            break

                    # Switch turns
                    turn = "white" if turn == "black" else "black"

                selected_piece.selected = False
                selected_piece = None


    screen.fill(WHITE)


  # Draw the chessboard
    for row in range(8):
        for col in range(8):
            x = board_offset_x + col * square_size
            y = board_offset_y + row * square_size
            square_color = DARK_SQUARE if (row + col) % 2 == 0 else LIGHT_SQUARE
            pygame.draw.rect(screen, square_color, (x, y, square_size, square_size))

    # Draw the chess pieces
    for piece in pieces:
        piece.draw()

    pygame.display.flip()
# To quick run: python chess_game.py
# Quit the game
pygame.quit()
