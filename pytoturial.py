import pygame,sys
from Rocket import Rocket
class Game(object):
    def __init__(self):
        #Configurations
        self.max_tps=60.0
        #Init
        pygame.init()
        self.speed=5
        self.screen = pygame.display.set_mode((860,480))
        self.box = pygame.Rect(10,10,50,50)
        self.tps_delta = 0.0
        self.clock = pygame.time.Clock()
        self.player = Rocket(self)
        
        #Loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                    sys.exit(0)
            #Ticking
            self.tps_delta += self.clock.tick()/1000.0
            while self.tps_delta > 1/self.max_tps:
                self.tick()
                self.tps_delta-=1/self.max_tps
            self.screen.fill((0,0,0))
            self.player.draw()
            pygame.display.update()
    def tick(self):
        if pygame.key.get_pressed()[pygame.K_d]:
            self.player.x+=self.speed
        if pygame.key.get_pressed()[pygame.K_a]:
            self.player.x-=self.speed
        if pygame.key.get_pressed()[pygame.K_s]:
            self.player.y+=self.speed
        if pygame.key.get_pressed()[pygame.K_w]:
            self.player.y-=self.speed
    def draw(self):
        pygame.draw.rect(self.screen,(100,0,100),self.box)

if __name__== "__main__":
    Game()
    
    
        
