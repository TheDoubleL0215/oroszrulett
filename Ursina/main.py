from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time
import random
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

#FOBB VALTOZOK/ADATOK

app = Ursina()
Sky()
player = FirstPersonController(position=(0, 5, 0))

fo_szam = random.randint(1, 8)
lehet = ""
szamok = [1, 2, 3, 4, 5, 6, 7, 8]
talalat = False
#KARAKTER NEVEK MEGADASA
p1 = input("Mi legyen az elso vertanu neve?: ")
p2 = input("Mi legyen az masodik vertanu neve?: ")
p3 = input("Mi legyen az harmadik vertanu neve?: ")

#-----------------------------------------------------------------------------
#FUNKCIOK

def generalas():
    global rand_szam
    rand_szam = random.choice(szamok)
    print(f"A valasztott a {rand_szam}, a szam pedig {fo_szam}")

def halal():
        getEnemy = mouse.hovered_entity
        getEnemy.rotation_z = 90
        halal_message = Text(text=f"Meghalt: {getEnemy.name}!", origin=(0, 0), scale=5)

#-----------------------------------------------------------------------------
#INPUT KEZELES

def input(key):
    if key == 'h':
        getloc = player.get_position()
        print(getloc)
    if key == 'r':
        weapon.rotation_y = -50
        Audio('assets/revolver_spin.mp3')
        generalas()
    if key == 't':
        weapon.rotation_y = -20
        Audio("assets/revolvercock1-6924.mp3")
    if key == 'left mouse down':
        try:
            if rand_szam == fo_szam:
                Audio("assets/shoot.mp3")   #amikor van talalat 
                talalat = True

                halal()
            else:
                try:
                    Audio('assets/gun-dry.mp3')    #amikor nincs talalat
                    szamok.remove(rand_szam)
                    print(szamok)
                except ValueError:
                    Audio('assets/gun-dry.mp3')
        except NameError:
            Audio('assets/gun-dry.mp3')

#-----------------------------------------------------------------------------




ground = Entity(
    model = "plane",
    texture = "grass",
    collider = "mesh",
    scale = (50, 1, 50)
)

wall = Entity(
    model = "assets/wall2.obj",
    collider = "box", 
    scale = (1, 1, 1),
    position = (0, 0, 7),
    texture = "brick",
    rotation_y = 90,
    color = color.orange,
)


weapon = Entity(
    model = "assets/gun.obj",
    parent = camera.ui,
    scale = 2.5,
    texture = "shore",
    position = (0.2, -0.4),
    rotation = (-10, -20, -10),
    color = color.gray
)

enemy = Entity(
    name = p1,
    model = "assets/RPG Player.obj",
    color = color.black,
    collider = "mesh",
    scale = (1, 1, 1),
    position = (0, 0, 5),
    rotation = (0, 180, 0),
)

enemy2 = duplicate(enemy, x=-1.5, name = p2)

enemy3 = duplicate(enemy, x=-3, name = p3)

enemy_text = Text(text=p1, origin=(-2, -6), scale=3, parent = camera.ui)  
enemy2_text = Text(text=p2, origin=(0, -6), scale=3, parent = camera.ui) 
enemy3_text = Text(text=p3, origin=(2, -6), scale=3, parent = camera.ui) 

if p3 != None:
    app.run()
