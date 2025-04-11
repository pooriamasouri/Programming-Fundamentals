import pygame
import sys
import Player_minimax
from Tic_Tac_Toe import reset_board, is_board_full, is_game_won, is_move_legal

# Constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)
LINE_WIDTH = 3
CELL_SIZE = WIDTH // 3
FONT_SIZE = 80

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.SysFont(None, FONT_SIZE)

# Draw the grid
def draw_grid():
    screen.fill(BG_COLOR)
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)

# Draw symbols
def draw_board(board):
    for y in range(3):
        for x in range(3):
            symbol = board[y][x]
            if symbol != " ":
                color = X_COLOR if symbol == "X" else O_COLOR
                text = font.render(symbol, True, color)
                rect = text.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, rect)

# Translate click to board move (1-9)
def get_click_position(pos):
    x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
    return y * 3 + x + 1

def main():
    board = reset_board()
    current_player = "X"
    running = True
    game_over = False

    while running:
        draw_grid()
        draw_board(board)
        pygame.display.flip()

        if game_over:
            continue

        if current_player == "X":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    move = get_click_position(pygame.mouse.get_pos())
                    if is_move_legal(board, move):
                        board[(move - 1) // 3][(move - 1) % 3] = "X"
                        if is_game_won(board):
                            print("X wins!")
                            game_over = True
                        elif is_board_full(board):
                            print("It's a tie!")
                            game_over = True
                        else:
                            current_player = "O"
        else:
            pygame.time.wait(500)
            move = Player_minimax.getMove(board)
            if is_move_legal(board, move):
                board[(move - 1) // 3][(move - 1) % 3] = "O"
                if is_game_won(board):
                    print("O wins!")
                    game_over = True
                elif is_board_full(board):
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = "X"

if __name__ == "__main__":
    main()
