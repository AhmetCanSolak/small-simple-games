import sys
import pygame
from helperLib import Board

# Initialize game details
pygame.init()
displayInfo = pygame.display.Info()
screen = pygame.display.set_mode( (displayInfo.current_w, displayInfo.current_h), pygame.FULLSCREEN )
pygame.display.set_caption("Tic Tac Toe - ACS Games")
clock = pygame.time.Clock()

# Set background color
screen.fill((235, 235, 235))

# Put a header to game
font = pygame.font.SysFont("papyrus", 192)
text = font.render("Tic-Tac-Toe", True, (255, 1, 0))
screen.blit(text, ( (displayInfo.current_w - text.get_width())//2, 0 ))
# Draw the board
board = Board(displayInfo,text,screen)


# Event listener loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            board.handleClick(event.pos[0],event.pos[1])

    pygame.display.update()
    clock.tick(45)
