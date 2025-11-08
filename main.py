from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        clock.tick(60)
        dt = clock.tick(60) / 1000
        print(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
