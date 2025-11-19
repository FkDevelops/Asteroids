import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    #set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Clock object to keep track of time
    clock = pygame.time.Clock()
    #delta time
    dt = 0
    #create player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)

        #make the screen black
        screen.fill("black")
        
        #draw the player 
        player.draw(screen)

        pygame.display.flip()

        #limit to 60 fps and getting delta time in seconds
        dt = dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
