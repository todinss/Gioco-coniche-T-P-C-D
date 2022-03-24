import pygame
import random
import sys
  
pygame.display.set_caption("Gioco Coniche")
pygame.init()


sfondo = pygame.image.load('sfondo.png')
astronave = pygame.image.load('images\disco.png')
striscia = pygame.image.load('images\linea.png')
saturno = pygame.image.load('images\saturno.png')
meteorite = pygame.image.load('images\meteorite.png')
cuore = pygame.image.load('images\cuore.png')

SCHERMO = pygame.display.set_mode((640, 380))
FPS = 60

vel_meteora = 12
vel_avanzamento = 10

def disegna_oggetti():
        SCHERMO.blit(sfondo, (0,0))
        for m in meteoriti:
                m.disegna()
        SCHERMO.blit(astronave, (astronaveX,astronaveY))
        SCHERMO.blit(striscia, (sfondoX,330))
        SCHERMO.blit(saturno, (320, -50))
        SCHERMO.blit(cuore, (65, 5))
        SCHERMO.blit(cuore, (35, 5))
        SCHERMO.blit(cuore, (5, 5))
class classe_meteore:
        def __init__(self):
              self.x = 600
              self.y = random.randint(-180,50)
        def disegna(self):
                 self.x -= vel_meteora
                 SCHERMO.blit(meteorite, (self.x,self.y+200))
        def collisione(self, astronave, astronaveX, astronaveY):
                t = 5
                lato_d = astronaveX+astronave.get_width()-t
                lato_s = astronaveX+t
                metiorite_d = self.x + meteorite.get_width()
                metiorite_s = self.x
                lato_giu = astronaveY+astronave.get_width()-t
                lato_su = astronaveY+t
                metiorite_su = self.y+110
                metiorite_giu = self.y+110
                if lato_d > metiorite_s and lato_s < metiorite_d:
                        astronaveY -= vel_avanzamento
            
def aggiorna():
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        

def inizializza():
        global astronaveX, astronaveY, astronave_velY
        global sfondoX
        global meteoriti
        global text
        global counter
        astronaveX, astronaveY = 20, 110
        sfondoX = 0
        meteoriti = []
        meteoriti.append(classe_meteore())
        
inizializza()
run = True
while run:
        sfondoX -= vel_avanzamento
        if sfondoX < -650: sfondoX = 0
        for event in pygame.event.get():
                if ( event.type == pygame.KEYDOWN
                        and event.key == pygame.K_UP ):
                        astronaveY -= vel_avanzamento
                elif ( event.type == pygame.KEYDOWN
                        and event.key == pygame.K_DOWN ):
                        astronaveY += vel_avanzamento
        if  meteoriti[-1].x < 200: meteoriti.append(classe_meteore())
        if astronaveY > 200:
                astronaveY -= vel_avanzamento
        if astronaveY < -70:
                astronaveY += vel_avanzamento

        disegna_oggetti()
        aggiorna()

if __name__ == "__main__":
        run()

