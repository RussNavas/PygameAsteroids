import pygame
from player import Player
from constants import (SCREEN_WIDTH,
                       SCREEN_HEIGHT,
                       ASTEROID_MIN_RADIUS,
                       ASTEROID_KINDS,
                       ASTEROID_SPAWN_RATE,
                       ASTEROID_MAX_RADIUS)


def main():
    # initialize pygame
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # set the screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create Clock object
    fps = pygame.time.Clock()
    # init variable for delta time
    dt = 0

    # init player 1
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    p1 = Player(x1, y1)

    # Begin game loop
    while True:
        # iterate through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # set and capture the frame rate each iteration
        dt = fps.tick(60)/1000

        # set the background to black
        screen.fill("black")
        # call update on player before render
        p1.update(dt)
        # draw the player
        p1.draw(screen)

        # update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
