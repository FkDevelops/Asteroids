import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField




def main():
    pygame.init()
    #set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Clock object to keep track of time
    clock = pygame.time.Clock()
    #creating groups for draw and updatable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #group for asteroids
    asteroids = pygame.sprite.Group()

    #adding objects to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    #delta time
    dt = 0
    #creating objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    A_field = AsteroidField()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update all objects in this group
        updatable.update(dt)

        #make the screen black
        screen.fill("black")
        
        #draw everything in the group
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        #limit to 60 fps and getting delta time in seconds
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
