import pygame
import random

Blue = (64, 128, 255)
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,128,0)

m = 0

class MainClass:
    def __init__(self):

        pygame.init()
        width = 500
        height = 500
        self.screen = pygame.display.set_mode((width,height))
        self.screen.fill(White)

        self.MassivePeopleBlue = []
        self.MassivePeopleBlue.append(self.MakePeopleBlue())

        self.MassivePeopleBlack = []
        self.MassivePeopleBlack.append(self.MakePeopleBlack())

        self.MassivePeopleRed = []
        self.MassivePeopleRed.append(self.MakePeopleRed())

        self.MassiveFruit = []

        for x in range(49):
            self.MassiveFruit.append(self.MakeSweetFruties())

        while True:
            self.screen.fill(White)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

##################################
            self.UpdateFruitP(self.MassivePeopleBlue)
            self.NewPeople(self.MassivePeopleBlue)
##################################
            self.UpdateFruitP(self.MassivePeopleRed)
            self.NewPeople(self.MassivePeopleRed)
##################################
            self.UpdateFruitP(self.MassivePeopleBlack)
            self.NewPeople(self.MassivePeopleBlack)
##################################

            pygame.display.update()
            pygame.time.delay(60)
            
    def MakePeopleBlue(self):
        return BluePeoples(self.screen)
    def MakePeopleRed(self):
        return RedPeoples(self.screen)
    def MakePeopleBlack(self):
        return BlackPeoples(self.screen)
    
    def NewPeople(self,Massive):
        for o in range(len(Massive)):
            for argsFruit in self.MassiveFruit:
                OkBoomer = (Massive[o].x, Massive[o].y)
                if( argsFruit.x - 7 < OkBoomer[0] < argsFruit.x + 7 and argsFruit.y - 7 < OkBoomer[1] < argsFruit.y + 7):
                    if(Massive is self.MassivePeopleRed):
                        Massive.append(self.MakePeopleRed())
                        self.MassiveFruit.remove(argsFruit)
                    elif(Massive is self.MassivePeopleBlue):
                        Massive.append(self.MakePeopleBlue())
                        self.MassiveFruit.remove(argsFruit)
                    else:
                        Massive.append(self.MakePeopleBlack())
                        self.MassiveFruit.remove(argsFruit)
    
    def UpdateFruitP(self,MassivePeople):
        for argsPeople in MassivePeople:
                argsPeople.Draw()
                argsPeople.MovePeople()
        for argsFruit in self.MassiveFruit:
            argsFruit.Draw()

    def MakeSweetFruties(self):
        return SweetFruit(self.screen)

class Peoples:
    def __init__(self,screen):
        self.x = random.randint(30,470)
        self.y = random.randint(30,470)
        self.RandomX = 0
        self.RandomY = 0 
        self.RandomX += random.randint(0,1)
        self.RandomY += random.randint(0,1)
        self.screen = screen
        self.MovePeople()
        self.Draw()

    def MovePeople(self):

        if(self.RandomX == 1):
            self.x -= 5

        if(self.x < 30):
            self.RandomX = 0

        if(self.RandomX == 0):
            self.x += 5

        if(self.x > 470):
            self.RandomX = 1

##########################################################

        if(self.RandomY == 1):
            self.y -= 5

        if(self.y < 30):
            self.RandomY = 0

        if(self.RandomY == 0):
            self.y += 5
            
        if(self.y > 470):
            self.RandomY = 1


class BluePeoples(Peoples):

    def __init__(self,screen):
        self.screen = screen
        Peoples.__init__(self,self.screen)
    def Draw(self):
        pygame.draw.circle(self.screen, Blue, (self.x, self.y), 2, 2)

class RedPeoples(Peoples):

    def __init__(self,screen):
        self.screen = screen
        Peoples.__init__(self,self.screen)
    def Draw(self):
        pygame.draw.circle(self.screen, Red, (self.x, self.y), 2, 2)

class BlackPeoples(Peoples):

    def __init__(self,screen):
        self.screen = screen
        Peoples.__init__(self,self.screen)
    def Draw(self):
        pygame.draw.circle(self.screen, Black, (self.x, self.y), 2, 2)



class SweetFruit:
    def __init__(self,screen):
        self.screen = screen
        self.x = random.randint(30,470)
        self.y = random.randint(30,470)

    def Draw(self):
        pygame.draw.circle(self.screen, Green, (self.x, self.y), 7, 7)


if __name__ == "__main__":
    App = MainClass()
