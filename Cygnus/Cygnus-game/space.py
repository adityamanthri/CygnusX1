import pygame
import random
import time
import sys
import os
import math
from pygame.locals import *
import threading


#Initializing Pygame
pygame.init()
w = 1280
h = 720
screen = pygame.display.set_mode((w, h))

#Title and Icon
pygame.display.set_caption('Exploration')
sprite = pygame.image.load('ship1.png')
pygame.display.set_icon(sprite)

#Declaring some key variables
score=0
BLACK = (0,0,0)
RED = (255,0,0)
CRED = (211,115,141)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (249, 215, 28)
LBLUE = (125, 249, 255)
NBLUE = (3,18,33)
clock = pygame.time.Clock()

#Filling the screen
screen.fill(NBLUE)

#fonts
myfont1 = pygame.font.SysFont("monospace", 30, True)
myfont2 = pygame.font.Font(os.path.join('orbitronm.ttf'), 30)
myfont3 = pygame.font.Font(os.path.join('pixelart.ttf'), 22)
myfont4 = pygame.font.SysFont("monospace", 26, True)



#Defining some helper functions
#===================================================================================
#===================================================================================
def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy

def set_timeout(func, sec):
    global t
    t.cancel()
    def func_wrapper():
        func()
        t.cancel()
    t = threading.Timer(sec, func_wrapper)
    t.start()

t = threading.Timer(1, set_timeout)
def returnEdgeDist():
    center = [w/2, h/2]
    dist_center = [math.fabs(ship.x - center[0]), math.fabs(ship.y - center[1])]
    return  dist_center

def rot_center(image, angle):
    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

def new_x(old_x,speed,angle_in_radians):
    newx = old_x + (speed*math.cos(angle_in_radians))
    return newx

def new_y(old_y,speed,angle_in_radians):
    newy = old_y + (speed*math.sin(angle_in_radians))
    return newy

def dtor(d):
    return math.radians(d)

def progress(count, total, status, name):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    pygame.display.update()
    screen.fill(BLACK)
    PROGRESS = myfont4.render('[%s] %s%s ...%s/r' + str(bar), 1, GREEN)
    screen.blit(PROGRESS, (PROGRESS.get_rect(center=(w/2, h/2))))
    DETAILS = myfont1.render(str(percents) + ' %  ' + str(status) + ' ' + str(name), 1, WHITE)
    screen.blit(DETAILS, (DETAILS.get_rect(center=(w/2, h/2+h/37))))

cur = 0
def inc():
    global cur
    cur+=1


def explodeanimationpart1(fileNumber_total):
  for file_name in os.listdir('images'):
      for file_name in os.listdir('images/'+str(file_name)):
          fileNumber_total+=1
  return fileNumber_total
fileNumber_total=explodeanimationpart1(0)

def explodeanimationpart2(fileNumber_expl,images):
  images = []
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  images.append([])
  fileNumber_expl = -1
  for file_name in os.listdir('images'):
      sub1=file_name
      images.append([])
      fileNumber_expl+=1
      i=0
      for file_name in os.listdir('images/'+str(file_name)):
          fileN = str(file_name)
          image = pygame.image.load('images/' + sub1 + '/' + str(i) + '.' + fileN[len(fileN)-3] + fileN[len(fileN)-2] + fileN[len(fileN)-1]).convert()
          images[int(sub1)].append(image)
          i+=1
          inc()
          progress(cur, fileNumber_total, image, str(i) + '.' + fileN[len(fileN)-3] + fileN[len(fileN)-2] + fileN[len(fileN)-1])
  return fileNumber_expl, images
fileNumber_expl,images = explodeanimationpart2(-1,[])

def load_image(name):
    image = pygame.image.load(name)
    return image
def gameoverlol():
	    gameover=myfont1.render("YOU HAVE FINISHED EXPLORING",True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	    screen.blit(gameover,(290,300))

asteroids_name = ["1 Ceres", "4 Vesta", "2 Pallas", "10 Hygiea", "704 Interamnia", "52 Europa", "511 Davida",
"65 Cybele", "15 Eunomia", "3 Juno", "31 Euphrosyne", "624 Hektor", "88 Thisbe", "324 Bamberga", "451 Patienta",
"532 Herculina", "48 Doris", "375 Ursula", "107 Camilla", "45 Eugenia", "7 Iris", "29 Amphirite", "423 Diotima",
"19 Fortuna", "13 Egeria", "24 Themis", "94 Aurora", "702 Ida", "121 Hermione", "Aletheia", "372 Palma", "128 Nemenios", "Eros", "Trojan", "Hebe"]

planetlist = []
planetlist.append(load_image('earth.png'))
planetlist.append(load_image('jupiter.png'))
planetlist.append(load_image('ganymade.png'))
planetlist.append(load_image('huamea.png'))
planetlist.append(load_image('Eris.png'))
planetlist.append(load_image('mercury.png'))
planetlist.append(load_image('neptune.png'))
planetlist.append(load_image('uranus.png'))
planetlist.append(load_image('venus.png'))
planetlist.append(load_image('ultima.png'))
planetlist.append(load_image('Mars.png'))
planetlist.append(load_image('kelper22b.png'))
planetlist.append(load_image('Gliese581b.png'))


#===================================================================================
#===================================================================================

#Creation of a class for all the individual components of the game
#This includes bullet, ship, planets, stars, explosion
class Bullet:
    def __init__(self, x, y, angle, speed):
        self.x = x+31
        self.y = y+31
        self.angle = angle
        self.speed = speed
        self.lifetime = 0
    def show(self):
        self.lifetime += 1
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 6, 0)
    def refreshPos(self):
        self.x += (self.x - new_x(self.x, self.speed, dtor(-(self.angle-90))))
        self.y += (self.y - new_y(self.y, self.speed, dtor(-(self.angle-90))))
class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed= 0
        #self.vel = 0.1
        self.images = []
        self.images.append(load_image('ship1.png'))
        self.images.append(load_image('ship2.png'))
        self.images.append(load_image('ship3.png'))
        self.images.append(load_image('ship4.png'))
        self.index = 0
        self.img = self.images[self.index]

        self.dirX = 0
        self.dirY = 0
        self.last_used = pygame.time.get_ticks()
        self.cooldown = 200
        self.maxSpeed = 12
        self.rotate = False
        self.altitude = 100
    def show(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.img = self.images[self.index]
        screen.blit(rot_center(self.img, self.angle),(self.x,self.y))
    def move(self):
        if (self.rotate and self.angle < 360 and self.speed > 0):
            self.angle+= 5
            self.speed -= 1
        else :
            self.rotate = False
        if (self.angle > 360):
            self.angle = 0
        if (self.angle < 0):
            self.angle = 360
        for i in range(len(asteroids)):
            self.dirX = (self.x - new_x(self.x, self.speed, dtor(-(self.angle + 90))))
            self.dirY = (self.y - new_y(self.y, self.speed, dtor(-(self.angle + 90))))
            asteroids[i].x += self.dirX
            asteroids[i].y += self.dirY
        for i in range(len(explosions)):
            explosions[i].x += self.dirX
            explosions[i].y += self.dirY
        for i in range(len(planets)):
            planets[i].x += self.dirX
            planets[i].y += self.dirY
        for i in range(len(stars)):
            stars[i].x += ((self.dirX * stars[i].radius)/2000)*30
            stars[i].y += ((self.dirY * stars[i].radius)/2000)*30
        for i in range(len(ground.posX)):
            ground.posX[i] += self.dirX
            ground.posY[i] += self.dirY
        self.altitude = int(ground.posY[0]-h/2-70)
        global score
        score=score+0.1*self.speed
        if (pressed_up and self.speed <= self.maxSpeed):
            self.speed += 0.1
        if (not pressed_up and self.speed >= 0.1):
            self.speed -= 0.1
        if (not pressed_down and self.speed <= 0.1):
            self.speed += 0.1
        if (pressed_down and self.speed >= -5):
            self.speed -= 0.1
        if (pressed_left):
            self.angle += 4
        if (pressed_right):
            self.angle -= 4
    def returnDir(self):
        self.dir = ""
        if (self.dirX <= self.maxSpeed/2 and self.dirX >= -self.maxSpeed/2 and self.dirY > 0):
            self.dir = "up"
        elif (self.dirX <= self.maxSpeed/2 and self.dirX >= -self.maxSpeed/2 and self.dirY < 0):
            self.dir = "down"
        elif (self.dirX <= self.maxSpeed+1 and self.dirX >= -self.maxSpeed/2 and self.dirY <= self.maxSpeed/2 and self.dirY >= -self.maxSpeed/2):
            self.dir = "left"
        elif (self.dirX >= -self.maxSpeed-1 and self.dirX <= -self.maxSpeed/2 and self.dirY <= self.maxSpeed/2 and self.dirY >= -self.maxSpeed/2):
            self.dir = "right"
        return self.dir
    def shoot(self):
        if (pressed_bar):
            now = pygame.time.get_ticks()
            if (now - self.last_used >= self.cooldown):
                self.last_used = now
                bullets.append(Bullet(self.x, self.y, self.angle, 20))
    def notControlable(self, intensity):
        self.dirX = -intensity*self.dirX
        self.dirY = -intensity*self.dirY
    def rotateSetTo(self, val):
        self.rotate = val
class Explosion:
    def __init__(self, x, y, size):
        global fileNumber;
        self.size = size
        self.frame = 0
        self.list = images[random.randint(0,fileNumber_expl)]
        self.image = pygame.transform.scale(self.list[self.frame], (self.size*2, self.size*2))
        self.x = x
        self.y = y
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 20
    def update(self):
        now = pygame.time.get_ticks()
        screen.blit(self.image,(self.x,self.y));
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            if (self.frame != len(self.list)):
                self.frame += 1
            if self.frame != len(self.list):
                self.image = pygame.transform.scale(self.list[self.frame], (self.size*2, self.size*2))
class Asteroid:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.spawnX = x
        self.spawnY = y
        self.size = size
        self.maxlife = int(size/20)
        self.life = self.maxlife
        self.dist = 1
        # generation of random variables
        self.nbrRandom = []
        for i in range(16):
            self.nbrRandom.append(random.randint(0, size))

        self.refreshPos()
        self.color = WHITE
        # each asteroid is moving in space, we generate the directions
        self.moveDir = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.name = asteroids_name[random.randint(0, len(asteroids_name)-1)]
    def refreshPos(self):
        # generation of the basic form of hexagon
        self.v1 = [self.x            , self.y]
        self.v2 = [self.x+self.size  , self.y-self.size]
        self.v3 = [self.x+self.size*2, self.y-self.size]
        self.v4 = [self.x+self.size*3, self.y]
        self.v5 = [self.x+self.size*3, self.y+self.size]
        self.v6 = [self.x+self.size*2, self.y+self.size*2]
        self.v7 = [self.x+self.size  , self.y+self.size*2]
        self.v8 = [self.x            , self.y+self.size]

        # we add our random values
        self.v1[0] += self.nbrRandom[0]
        self.v1[1] += self.nbrRandom[1]

        self.v2[0] += self.nbrRandom[2]
        self.v2[1] += self.nbrRandom[3]

        self.v3[0] += self.nbrRandom[4]
        self.v3[1] += self.nbrRandom[5]

        self.v4[0] += self.nbrRandom[6]
        self.v4[1] += self.nbrRandom[7]

        self.v5[0] += self.nbrRandom[8]
        self.v5[1] += self.nbrRandom[9]

        self.v6[0] += self.nbrRandom[10]
        self.v6[1] += self.nbrRandom[11]

        self.v7[0] += self.nbrRandom[12]
        self.v7[1] += self.nbrRandom[13]

        self.v8[0] += self.nbrRandom[14]
        self.v8[1] += self.nbrRandom[15]
    def show(self):
        self.bestY = self.v1[1];
        if (self.v2[1] < self.bestY):
            self.bestY = self.v2[1];
        if (self.v3[1] < self.bestY):
            self.bestY = self.v3[1];
        if (self.v4[1] < self.bestY):
            self.bestY = self.v4[1];

        self.mostInRight = self.v3[0];
        if (self.v4[0] > self.mostInRight):
            self.mostInRight = self.v4[0];
        if (self.v5[0] > self.mostInRight):
            self.mostInRight = self.v5[0];
        if (self.v6[0] > self.mostInRight):
            self.mostInRight = self.v6[0];

        self.mostInLeft = self.v2[0];
        if (self.v1[0] < self.mostInLeft):
            self.mostInLeft = self.v1[0];
        if (self.v8[0] < self.mostInLeft):
            self.mostInLeft = self.v8[0];
        if (self.v7[0] < self.mostInLeft):
            self.mostInLeft = self.v7[0];

        self.toDisplay=False
        if (self.v1[0]>0 and self.v1[0]<w and self.v6[1]>0 and self.v1[1]<h):
            self.toDisplay=True
        elif (self.v6[0]>0 and self.v6[0]<w and self.v6[1]>0 and self.v6[1]<h):
            self.toDisplay=True
        elif (self.v3[0]>0 and self.v3[0]<w and self.v3[1]>0 and self.v3[1]<h):
            self.toDisplay=True
        elif (self.v4[0]>0 and self.v4[0]<w and self.v4[1]>0 and self.v4[1]<h):
            self.toDisplay=True
        elif (self.v5[0]>0 and self.v5[0]<w and self.v5[1]>0 and self.v5[1]<h):
            self.toDisplay=True
        elif (self.v6[0]>0 and self.v6[0]<w and self.v6[1]>0 and self.v6[1]<h):
            self.toDisplay=True
        elif (self.v7[0]>0 and self.v7[0]<w and self.v7[1]>0 and self.v7[1]<h):
            self.toDisplay=True
        elif (self.v8[0]>0 and self.v8[0]<w and self.v8[1]>0 and self.v8[1]<h):
            self.toDisplay=True
        if (self.toDisplay):
            self.toDisplay=False

            pygame.draw.polygon(screen, self.color, [self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7, self.v8], 4)
            if (self.size > 80):
                NAME = myfont3.render(self.name, 1, (255, 255, 0))
                screen.blit(NAME, (self.mostInRight, (self.y+self.size)))

                SIZE = myfont3.render("SIZE  " + str(self.size), 1, (255, 255, 0))
                screen.blit(SIZE, (self.mostInRight, (self.y+self.size+self.size/4)))
        #pygame.draw.line(screen, (255, 255, 255), (self.spawnX, self.spawnY), ((self.x, self.y )))
    def move(self):
            self.x += (self.moveDir[0] * 100)/((self.size)*1)
            self.y += (self.moveDir[1] * 100)/((self.size)*1)
    def health(self):
        if (self.maxlife > 1):
            health = (self.life * self.size / self.maxlife)
            pygame.draw.rect(screen, RED, (self.mostInLeft, self.bestY, health*(self.mostInRight-self.mostInLeft)/70,self.size/3))
class Star:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = [WHITE, YELLOW, LBLUE, CRED, WHITE, LBLUE]
        random.shuffle(self.color)

    def show(self):
        if (self.radius > 0):
            pygame.draw.circle(screen, self.color[0], (int(self.x), int(self.y)),int(self.radius/20))
class Planet:
    def __init__(self, x, y, size):
        self.size = size
        self.num = random.randint(0,12)
        self.image = planetlist[self.num]
        img_size = self.image.get_size()
        self.size_X = int(img_size[0]*(self.size/img_size[0]))
        self.size_Y = int(img_size[1]*(self.size/img_size[0]))
        self.x = x
        self.y = y
    def update(self):
        dx, dy = (self.x)*2 - ship.x, (self.y)*2 - ship.y
        # We are looking for the hypotenuse of the triangle formed by dx and dy
        self.dist = math.hypot(dx, dy)
        dx, dy = dx / self.dist, dy / self.dist
        # move along this normalized vector towards the player at current speed
        self.x += -100 * (dx/1000  )
        self.y += -100 * (dy/1000  )
        TEXT = myfont3.render("planet", 1, (255, 255, 0))
        if self.num == 0:
          TEXT = myfont3.render("Earth, looks like you have made it back to our former stronghold!", 1, (255, 255, 0))
        if self.num == 1:
          TEXT = myfont3.render("Jupiter, the gas giant looks majestic as ever before!", 1, (255, 255, 0))
        if self.num == 2:
          TEXT = myfont3.render("Ganymade, Jupiter's largest moon! Nothing much here time to get going", 1, (255, 255, 0))
        if self.num == 3:
          TEXT = myfont3.render("Huamea, a dwarf planet!", 1, (255, 255, 0))
        if self.num == 5:
          TEXT = myfont3.render("Mercury, it's getting really hot we're close to the sun!", 1, (255, 255, 0))
        if self.num == 6:
          TEXT = myfont3.render("Neptune, the winds are so strong you can feel it inside the spaceship!", 1, (255, 255, 0))
        if self.num == 7:
          TEXT = myfont3.render("Uranus, what an interesting hue! You can even see the thin rings around it!", 1, (255, 255, 0))
        if self.num == 8:
          TEXT = myfont3.render("Venus, ouch the scorching heat can be felt till here!", 1, (255, 255, 0))
        if self.num == 9:
          TEXT = myfont3.render("Ultima Thule, we're outside the solar system in the kuiper belt!", 1, (255, 255, 0))
        if self.num == 10:
          TEXT = myfont3.render("Mars, red as blood! The god of war is smiling upon you!", 1, (255, 255, 0))
        if self.num == 11:
          TEXT = myfont3.render("Kepler 22b, We've reached the Kepler system! We're right in the middle of the habitable zone!", 1, (255, 255, 0))
        if self.num == 12:
          TEXT = myfont3.render("Gliese 581b, The Gliese system's gem! What a tiny system!", 1, (255, 255, 0))
        screen.blit(TEXT, (self.x+self.size+300, (self.y+self.size)))
        if (self.x>0-self.size and self.x<w+self.size and self.y>0-self.size and self.y<h+self.size):
            screen.blit(self.image,(self.x,self.y))
class Ground:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.posX = []
        self.posY = []

        for i in range(1000):
            self.posX.append(10*i)
            self.posY.append(5*h/6+random.randint(-5, 5))

    def show(self):
        for i in range(len(self.posX)):
            if (self.posX[i] > w):
                self.posX[i] = 0
            elif (self.posX[i] < 0):
                self.posX[i] = w
        if self.posY[0]-75<=h:
            if self.posY[0]-70<= h/2:
                ship.speed = -1*ship.speed
            try:
                for i in range(len(self.posX)):
                    pygame.draw.circle(screen, GREEN, (int(self.posX[i]), int(self.posY[i])), 3)
            except:
                pass

stars = []
explosions = []
asteroids = []
bullets = []
planets = []
rdm = 6
render_distance = [w*rdm, h*rdm]
minsize = 40
maxsize = 120

def spawnAsteroids(xMin,xMax, yMin, yMax):
    for i in range(2):
        for j in range(2):
            x = random.randint(xMin, xMax)
            y = random.randint(yMin, yMax)
            size = random.randint(minsize, maxsize)
            if y < 2*h:
                asteroids.append(Asteroid(x, y, size))

asteroids.append(Asteroid(w/2, -10*h, 40))
ground = Ground(0,0)
ship = Ship(w/2, h/2)
pressed_left,pressed_right,pressed_up,pressed_down,pressed_bar  = False, False, False, False, False
SCORE_COOLDOWN = 1000
SCORE_UP_AMOUNT = 0
SCORE_UP_SHOW = False
def scoreUpToFalse():
    global SCORE_UP_SHOW
    SCORE_UP_SHOW = False
def set_timeout(func, sec):
    t = None
    def func_wrapper():
        func()
        t.cancel()
    t = threading.Timer(sec, func_wrapper)
    t.start()

end_it=False
def opscreen(end_it,str):
  while (end_it==False):
      screen.fill(BLACK)
      background=load_image(str)
      screen.blit(background,(0,0))
      myfont=pygame.font.SysFont("Britannic Bold", 40)
      nlabel=myfont.render("", 1, (255, 0, 0))
      for event in pygame.event.get():
          if event.type==pygame.KEYDOWN:
              if event.key==pygame.K_RETURN:
                  end_it=True
      screen.blit(nlabel,(200,200))
      pygame.display.flip()

opscreen(end_it,'title.png')
opscreen(end_it,'title2.png')
opscreen(end_it,'title3.png')
opscreen(end_it,'title4.png')

end_it=False
while (end_it==False):
    ast_already_in_screen = False;
    pygame.display.update()
    screen.fill(BLACK)
    index_bullet_to_remove = [];
    index_asteroid_to_remove = [];
    index_explosion_to_remove = [];

    if (ship.altitude > 700 and len(stars) < 100):
         stars.append(Star(random.randint(0, w), random.randint(0, h), random.randint(1, 140)))
    if (ship.altitude > 10000 and len(planets) < 80):
        planets.append(Planet(random.randint(-w*50, w*50), random.randint(-h*100, -h*4), random.randint(500, 800)));

    for i in range(len(explosions)):
        explosions[i].update();
        if explosions[i].frame == len(explosions[i].list):
            index_explosion_to_remove.append(i);

    for i in range(len(planets)):
        planets[i].update();
        distFromCenterX = w/2 - planets[i].x;
        distFromCenterY = h/2 - planets[i].y;
        radiusX=int(math.fabs(distFromCenterX)/100)
        radiusY=int(math.fabs(distFromCenterY)/100)
        Show = True;
        if radiusX>30000:
            Show = False;
        elif radiusX>150:
            radiusX=150
        if radiusY>30000:
            Show = False;
        elif radiusY>150:
            radiusY=150
        if (Show):
            #Gauche
            if (planets[i].x < 0):
                pygame.draw.circle(screen, GREEN, (0, int(planets[i].y+planets[i].size/2)), radiusX, 1);
            #Droite
            if (planets[i].x > w):
                pygame.draw.circle(screen, GREEN, (w-10, int(planets[i].y+planets[i].size/2)), radiusX, 1);
            #Haut
            if (planets[i].y < 0):
                pygame.draw.circle(screen, GREEN, (int(planets[i].x+planets[i].size/2), 10), radiusY, 1);
            #Bas
            if (planets[i].y > h):
                pygame.draw.circle(screen, GREEN, (int(planets[i].x+planets[i].size/2), h-10), radiusY, 1);

    for i in range(len(asteroids)):
        #pygame.draw.lines(screen, WHITE, False, [[asteroids[i].x, asteroids[i].y], [ship.x, ship.y]], 1)
        asteroids[i].move();
        asteroids[i].refreshPos();
        asteroids[i].show();
        distFromCenterX = w/2 - asteroids[i].x;
        distFromCenterY = h/2 - asteroids[i].y;
        if (math.fabs(distFromCenterX) > render_distance[0]*1.4 and len(asteroids) > 1 or math.fabs(distFromCenterY) > render_distance[1]*1.4 and len(asteroids) > 1):
            index_asteroid_to_remove.append(i);
        if (asteroids[i].maxlife != asteroids[i].life):
            asteroids[i].health();
        if (asteroids[i].x < 0 and asteroids[i].x > -w*2):
            pygame.draw.circle(screen, asteroids[i].color, (0, int(asteroids[i].y)), int(math.fabs(distFromCenterX)/100), 1);
        elif (asteroids[i].x > w and asteroids[i].x < w*2):
            pygame.draw.circle(screen, asteroids[i].color, (w-10, int(asteroids[i].y)), int(math.fabs(distFromCenterX)/100), 1);
        elif (asteroids[i].y < 0 and asteroids[i].y > -h*2):
            pygame.draw.circle(screen, asteroids[i].color, (int(asteroids[i].x), 10), int(math.fabs(distFromCenterY)/100), 1);
        elif (asteroids[i].y > h and asteroids[i].y < h*2):
            pygame.draw.circle(screen, asteroids[i].color, (int(asteroids[i].x), h-10), int(math.fabs(distFromCenterY)/100), 1);

        if (asteroids[i].x > -w and asteroids[i].x < w and asteroids[i].y > -h and asteroids[i].y < h):
            ast_already_in_screen = True;
            if (ground.posY[0] <= asteroids[i].v2[1] or ground.posY[0] <= asteroids[i].v7[1]):
                xExpl = asteroids[i].x+asteroids[i].size
                yExpl = asteroids[i].y-2/asteroids[i].size
                explosions.append(Explosion(xExpl,yExpl,asteroids[i].size));
                index_asteroid_to_remove.append(i);

        if (ship.x + 31< asteroids[i].v4[0] and ship.x + 31 > asteroids[i].v1[0] and ship.y + 31> asteroids[i].v2[1] and ship.y + 31< asteroids[i].v7[1]):
            #random.choice(expl_sounds).play()
            xExpl = asteroids[i].x+asteroids[i].size
            yExpl = asteroids[i].y-2/asteroids[i].size
            explosions.append(Explosion(xExpl,yExpl,asteroids[i].size));
            if (asteroids[i].size/1.8 > 20):
                for e in range(2):
                    asteroids.append(Asteroid(asteroids[i].x, asteroids[i].y, int(asteroids[i].size/1.8)));
            index_asteroid_to_remove.append(i);
            ship.rotateSetTo(True);
            ship.notControlable(0.5);
            last_up=-10*asteroids[i].size
            if ((score+last_up)<=0):
                score=0;
            else:
                score+=last_up;
            SCORE_UP_SHOW = True;
            set_timeout(scoreUpToFalse, 1)

    for i in range(len(bullets)):
        bullets[i].refreshPos();
        bullets[i].show()
        for j in range(len(asteroids)):
            if (bullets[i].x >= asteroids[j].v1[0] and bullets[i].x <= asteroids[j].v4[0]  and bullets[i].y >= asteroids[j].v2[1] and bullets[i].y <= asteroids[j].v7[1]):
                #random.choice(expl_sounds).play()
                if (asteroids[j].life==1):
                    xExpl = asteroids[j].x+asteroids[j].size
                    yExpl = asteroids[j].y-2/asteroids[j].size
                    explosions.append(Explosion(xExpl,yExpl,asteroids[j].size));
                    index_asteroid_to_remove.append(j);

                    last_up=10*asteroids[j].size
                    score+=last_up
                    SCORE_UP_SHOW = True;
                    set_timeout(scoreUpToFalse, 1)

                    if (asteroids[j].size/1.8 > 20):
                        for e in range(2):
                            asteroids.append(Asteroid(asteroids[j].x, asteroids[j].y, int(asteroids[j].size/1.8)));
                else:
                    asteroids[j].life-=1
                index_bullet_to_remove.append(i);

        if (bullets[i].lifetime > 70 and i not in bullets):
            index_bullet_to_remove.append(i);


    for i in range(len(index_explosion_to_remove)):
        try:
            explosions.remove(explosions[index_explosion_to_remove[i]]);
        except:
            continue

    for i in range(len(index_bullet_to_remove)):
        try:
            bullets.remove(bullets[ index_bullet_to_remove[i]]);
        except:
            continue

    for i in range(len(index_asteroid_to_remove)):
        try:
            asteroids.remove(asteroids[ index_asteroid_to_remove[i]])
        except:
            spawnAsteroids(-w*2, w/2, -h*2, -h)
            pass;

    if (not ast_already_in_screen):
        if (pressed_up and ship.altitude > 6000):
            if (ship.returnDir() == "up"):
                for i in range(2):
                    spawnAsteroids(-render_distance[0], render_distance[0]/2, -render_distance[1], 0);
            if (ship.returnDir() == "down"):
                for i in range(2):
                    spawnAsteroids(-render_distance[0], render_distance[0], 1000, render_distance[1]);
            if (ship.returnDir() == "left"):
                spawnAsteroids(-render_distance[0], render_distance[0], -render_distance[1], render_distance[1]);
            if (ship.returnDir() == "right"):
                spawnAsteroids(-render_distance[0], render_distance[0], -render_distance[1], render_distance[1]);
    ship.show();
    ship.move();
    ship.shoot();
    ground.show();
    for i in range(len(stars)):
        stars[i].x += stars[i].radius/1000;
        stars[i].y += stars[i].radius/1000;
        stars[i].show();
        if (stars[i].x > w):
            stars[i].x = 0;
        if (stars[i].x < 0):
            stars[i].x = w;

        if (stars[i].y > h):
            stars[i].y = 0;
        if (stars[i].y < 0):
            stars[i].y = h;
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pressed_up = True;
            if event.key == pygame.K_DOWN:
                pressed_down = True;
            if event.key == pygame.K_RIGHT:
                pressed_right = True;
            if event.key == pygame.K_LEFT:
                pressed_left = True;
            if event.key == pygame.K_SPACE:
                pressed_bar = True;
            if event.key == pygame.K_ESCAPE:
                event.type = QUIT;

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pressed_up = False;
            if event.key == pygame.K_DOWN:
                pressed_down = False;
            if event.key == pygame.K_RIGHT:
                pressed_right = False;
            if event.key == pygame.K_LEFT:
                pressed_left = False;
            if event.key == pygame.K_SPACE:
                pressed_bar = False;
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    if ship.altitude < 10:
        gameoverlol()
        end_it=True
    if score < 0:
        gameoverlol()
        end_it=True
    scoretext = myfont2.render("SCORE: "+str(round(score)), 1, YELLOW)
    screen.blit(scoretext, (w-300, h-110))
    ALTITUDE = myfont2.render('ALTITUDE: ' + str(ship.altitude), 1, LBLUE)
    screen.blit(ALTITUDE, (w-350, h-70))
    #DIRECTION = myfont2.render('DIRECTION: ' + ship.returnDir(), 1, (77,255,77))
    #screen.blit(DIRECTION, (20, 100+55))
    #HUD = myfont3.render("FPS: "+str(round(clock.get_fps(), 2)), 1, WHITE)
    #screen.blit(HUD, (w-200, h-70))
    if (SCORE_UP_SHOW):
        if (last_up<=0):
            SCORE_UP = myfont1.render("- "+str(-1*(last_up)), 1, (255,77,77))
        else:
            SCORE_UP = myfont1.render("+ "+str(last_up), 1, (77,255,77))
        screen.blit(SCORE_UP, (w-200, h-150))
    clock.tick(60)

end_it = False
while (end_it==False):
    screen.fill(BLACK)
    myfont=pygame.font.SysFont("Britannic Bold", 40)
    nlabel=myfont.render("", 1, (255, 0, 0))
    scoretext = myfont2.render("SCORE: "+str(round(score)), 1, (77,255,77))
    screen.blit(scoretext, (w-200, h-110))
    #HUD = myfont3.render("FPS: "+str(round(clock.get_fps(), 2)), 1, WHITE)
    #screen.blit(HUD, (w-200, h-70))
    if score<=10:
        background=load_image('end.png')
        screen.blit(background,(0,0))
    if score>10 and score<5000:
        background=load_image('end2.png')
        screen.blit(background,(0,0))
    if score>=5000:
        background=load_image('end3.png')
        screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                end_it=True
                pygame.display.quit()
                pygame.quit()
                sys.exit()
    screen.blit(nlabel,(200,200))
    pygame.display.flip()
