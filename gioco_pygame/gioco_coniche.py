import pygame
import random
import sys
  
pygame.display.set_caption("Gioco Coniche")
pygame.init()


sfondo = pygame.image.load('sfondo.png')
astronave = pygame.image.load('disco.png')
striscia = pygame.image.load('linea.png')
saturno = pygame.image.load('saturno.png')
meteorite = pygame.image.load('meteorite.png')
cuore = pygame.image.load('cuore.png')
game = pygame.image.load('over.png')
SCHERMO = pygame.display.set_mode((640, 380))
FPS = 60
FONT = pygame.font.SysFont("Arial", 28, bold=True)

vel_meteora = 12
vel_avanzamento = 10
def disegna_oggetti():
        SCHERMO.blit(sfondo, (0,0))
        for m in meteoriti:
                m.disegna_meteoriti()
        SCHERMO.blit(astronave, (astronaveX,astronaveY))
        SCHERMO.blit(striscia, (sfondoX,330))
        SCHERMO.blit(saturno, (320, -50))
        SCHERMO.blit(cuore, (65, 5))
        SCHERMO.blit(cuore, (35, 5))
        SCHERMO.blit(cuore, (5, 5))
        punti_render = FONT.render(str(punti), 1, (255, 255, 255))
        SCHERMO.blit(punti_render, (100, 4))

def hai_perso():
        SCHERMO.blit(game, (60, -91))
        aggiorna()
        ric = False
        while not ric:
                for event in pygame.event.get():
                        if ( event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE ):
                                inizializza()
                                ric = True
                        if event.type == pygame.QUIT:
                                pygame.quit()
                
        
class classe_meteore:
        def __init__(self):
                self.x = 600
                self.y = random.randint(-180,50)
        def disegna_meteoriti(self):
                self.x -= vel_meteora
                SCHERMO.blit(meteorite, (self.x,self.y+200))
        def collisione(self, astronave, astronaveX, astronaveY):
                to = 5
                nave_lato_d = astronaveX + astronave.get_width() - to
                nave_lato_s = astronaveX + to
                nave_lato_giu = astronaveY + astronave.get_height() - to
                nave_lato_su = astronaveY + to
                meteorite_d = self.x + meteorite.get_width()
                meteorite_s = self.x
                meteorite_su = self.y
                meteorite_giu = self.y + meteorite.get_height()
                if nave_lato_d > meteorite_s and nave_lato_s < meteorite_d:
                        if nave_lato_su < meteorite_su and nave_lato_giu > meteorite_giu:
                                hai_perso()
        def tra_i_meteoriti(self, astronave, astronaveY):
                to = 0
                nave_lato_giu = astronaveY + astronave.get_width() - to
                nave_lato_su = astronaveY + to
                meteorite_giu = self.y + meteorite.get_width()
                meteorite_su = self.y
                if nave_lato_giu > meteorite_su or nave_lato_su < meteorite_giu:
                        return True
def aggiorna():
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        

def inizializza():
        global astronaveX, astronaveY, astronave_velY
        global sfondoX
        global meteoriti
        global astronave
        global tra_i_meteoriti
        global punti
        global run
        astronaveX, astronaveY = 20, 110
        sfondoX = 0
        punti = 0
        meteoriti = []
        meteoriti.append(classe_meteore())
        tra_i_meteoriti = False
        run = True
        
inizializza()
while True:
        sfondoX -= vel_avanzamento
        if sfondoX < -650: sfondoX = 0
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
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
        for m in meteoriti:
                m.collisione(astronave, astronaveX, astronaveY)
        if not tra_i_meteoriti:
                for m in meteoriti:
                        if m.tra_i_meteoriti(astronave, astronaveX):
                                tra_i_meteoriti = True
                                break
        punti += 1
        disegna_oggetti()       
        aggiorna()
