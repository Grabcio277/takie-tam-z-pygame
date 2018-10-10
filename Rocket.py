class Rocket(object):
    def __init__(self,game):
        self.game = game
    def tick(self):
        pass
    def draw(self):
        pygame.draw.rect(self.game.screen,(0,150,255),pygame.Rect(50,30,50,50))
        
