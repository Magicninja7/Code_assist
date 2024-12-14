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

        
        
        
        self.lifetime = 255

        # Random direction for particle spread

        angle = random.uniform(0, math.pi * 2)

        speed = random.uniform(2, 5)

        
        
        self.gravity = 0.1



    def update(self):

        self.x += self.vx

        self.y += self.vy

        
        self.lifetime -= 5

        return self.lifetime > 0



    def draw(self, screen):

        alpha = max(0, min(255, self.lifetime))

        color = (self.color[0], self.color[1], self.color[2], alpha)

        surface = pygame.Surface((3, 3), pygame.SRCALPHA)

        pygame.draw.circle(surface, color, (1, 1), 1)

        screen.blit(surface, (int(self.x), int(self.y)))



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

            pygame.draw.line(screen, self.color, 
                             
                           (self.x, self.y), 

                           (self.x, self.y + 10), 2)

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



        # Randomly add new fireworks

        if random.random() < 0.05:  # 5% chance each frame

            fireworks.append(Firework())



        screen.fill(BLACK)

        

        # Update and draw fireworks

        fireworks = [fw for fw]