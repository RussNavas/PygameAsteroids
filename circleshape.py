import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes mus override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        # all things that collide inherit this
        combined_radii = self.radius + other.radius
        dist = self.position.distance_to(other.position)
        if combined_radii >= dist:
            return True
        return False
