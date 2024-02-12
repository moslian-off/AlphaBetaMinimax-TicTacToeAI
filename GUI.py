import pygame
from minimax import Find_winner, Game_Terminater, minimax_response,Edge

board = [[0 for _ in range(Edge)] for _ in range(Edge)]

def draw_board():
    for x in range(1, Edge):
        pygame.draw.lines(screen, LINE_COLOR, False, [(x*cell_size, 0), (x*cell_size, screen_h)], 5)
    for y in range(1, Edge):
        pygame.draw.lines(screen, LINE_COLOR, False, [(0, y*cell_size), (screen_w, y*cell_size)], 5)

def draw_XO():
    for x in range(Edge):
        for y in range(Edge):
            posX = y * cell_size + cell_size // 2
            posY = x * cell_size + cell_size // 2            
            if board[x][y] == 1:
                pygame.draw.line(screen, LINE_COLOR, (posX - 50, posY - 50),(posX + 50, posY + 50), 10)
                pygame.draw.line(screen, LINE_COLOR, (posX + 50, posY - 50),(posX - 50, posY + 50), 10)
            elif board[x][y] == -1:
                pygame.draw.circle(screen, LINE_COLOR, (posX, posY), 50, 10)

pygame.init()

screen_w, screen_h = 600, 600
screen = pygame.display.set_mode((screen_w, screen_h))

cell_size = 200
player_turn = True

WHITE = (255, 255, 255)
ORIG_LINE_COLOR = (0, 0, 0)
LINE_COLOR = (0, 0, 0)
FONT_COLOR = (0, 0, 0)
alpha = 255
running = True
fade_surface = pygame.Surface((screen_w, screen_h))
fade_surface.fill(WHITE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            mouseX, mouseY = pygame.mouse.get_pos()
            cellX, cellY = mouseX // cell_size, mouseY // cell_size
            if 0 <= cellX < Edge and 0 <= cellY < Edge and board[cellY][cellX] == 0:
                board[cellY][cellX] = 1
                player_turn = False

    if not player_turn:
        cellY,cellX = minimax_response(board)
        if 0 <= cellX < Edge and 0 <= cellY < Edge and board[cellY][cellX] == 0:
            board[cellY][cellX] = -1
            player_turn = True

    screen.fill(WHITE)
    draw_board()
    draw_XO()
    pygame.display.update()

    if Game_Terminater(board):
        winner = Find_winner(board)
        if winner == 1:
            game_result = 'You succeed!'
        elif winner == -1:
            game_result = 'You lose!'
        else:
            game_result = 'Draw!'
        
        font = pygame.font.Font(None, 72)
        result_surface = font.render(game_result, True, FONT_COLOR)
        screen.fill(WHITE)
        draw_board()
        draw_XO()
        screen.blit(result_surface, (screen_w // 2 - result_surface.get_width() // 2, screen_h // 2 - result_surface.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(2*1000)  # Game result appears for 3 seconds
        running = False

    pygame.display.update()

pygame.quit()