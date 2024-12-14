#Fireworks Simulation Project

#The idea is to create a visual display of fireworks using particles

#Each firework will:

#1. Launch from bottom of screen

#2. Explode at a random height

#3. Create multiple colored particles that spread out

#4. Particles will fade and fall with gravity

#5. Multiple fireworks can be active at once



import pygame






# Initialize Pygame

pygame.init()



# Set up display

WIDTH = 800

HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Fireworks Simulation")



# Colors

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), 
          
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]



class Particle:

    def __init__(self, x, y, color):

        
        
        
        self.radius = 2

        # Random direction for particle spread

        angle = random.uniform(0, math.pi * 2)

        speed = random.uniform(2, 5)

        
        
        self.lifetime = 255  # Used for fade effect



    def update(self):

        self.x += self.dx

        self.y += self.dy

        self.dy += 0.1  # Gravity effect

        self.lifetime -= 5

        return self.lifetime > 0



    def draw(self, screen):

        alpha = max(0, min(255, self.lifetime))

        color = (self.color[0], self.color[1], self.color[2], alpha)

        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        pygame.draw.circle(surface, color, (self.radius, self.radius), self.radius)

        screen.blit(surface, (int(self.x - self.radius), int(self.y - self.radius)))



class Firework:

    def __init__(self):

        self.x = random.randint(50, WIDTH - 50)

        
        self.target_y = random.randint(50, HEIGHT - 200)

        self.speed = -10

        
        self.particles = []

        self.color = random.choice(COLORS)



    def update(self):

        if not self.exploded:

            
            if self.y <= self.target_y:

                self.explode()



        self.particles = [p for p in self.particles if p.update()]

        return len(self.particles) > 0 or not self.exploded



    def explode(self):

        
        for _ in range(50):  # Create 50 particles

            self.particles.append(Particle(self.x, self.y, self.color))



    def draw(self, screen):

        if not self.exploded:

            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)

        for particle in self.particles:

            particle.draw(screen)



def main():

    clock = pygame.time.Clock()

    fireworks = []

    

    
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                
            elif event.type == pygame.MOUSEBUTTONDOWN:

                fireworks.append(Firework())



        # Randomly create new fireworks

        if random.random() < 0.03:  # 3% chance each frame

            fireworks.append(Firework())



        screen.fill(BLACK)

        

        # Update and draw fir