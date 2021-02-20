import pgzrun
import sys
mod = sys.modules['__main__']

from random import randint

a = True
score = 0
c = True

TITLE = 'croc!'
WIDTH = 1000
HEIGHT = 1000

skin = 0
skins = ['crocim']
player = mod.Actor(skins[skin])
coin = mod.Actor("coin")
enemy = mod.Actor("fish")

game_over = False
lives = 3


 



def draw():
    if not game_over:
        mod.screen.clear()
        mod.screen.fill((10,50,255))
        player.draw()

        
        coin.draw()
        enemy.draw()
        

        mod.screen.draw.text("$" + str(score), (0, 0))
        mod.screen.draw.text("" + str(lives), (0, 20))
    else:
        mod.screen.fill((0, 0, 0))
        mod.screen.draw.text('$' + str(score), (0, 0))
        mod.screen.draw.text('Press \'SPACE\' to start again', (mod.screen.width / 2, mod.screen.height / 2))
        player.x = 400
        player.y = 400 + 18
        player.draw()
    
        

    

    
    
        
def place_actors():
    player.x = randint(40, 300)
    player.y = randint(40, 300)
    
    coin.x = randint(20, 400)
    coin.y = randint(20, 400)
    
    enemy.x = randint(20, 400)
    enemy.y = randint(20, 400)
    
def place_coin():
    coin.x = randint(10, 800)
    coin.y = randint(10, 800)
    
def place_enemy():
    enemy.x = randint(10, 800)
    enemy.y = randint(10, 800)

def update():
    global score
    global lives
    global coin_count
    global live_count
    global game_over
    global a
    global skins, skin
    if lives > 0:
        if mod.keyboard.left:
            player.x -= 5
        if mod.keyboard.right:
            player.x += 5
        if mod.keyboard.down:
            player.y += 5
        if mod.keyboard.up:
            player.y -= 5
        coin_count = player.colliderect(coin)
        if coin_count:
            score += 10
            place_coin()
        live_count = player.colliderect(enemy)
        if live_count:
            lives -= 1
            place_enemy()
        
        chasePlayer()
        b = coin.colliderect(enemy)
        if b:
            place_coin
        
    else:
        End()
        if mod.keyboard.space:
            lives = 3
            place_actors()

            game_over = False
        
            
            

def chasePlayer():
    if enemy.x < player.x:
        enemy.x = enemy.x + 1
    if enemy.x > player.x:
        enemy.x = enemy.x - 1
    if enemy.y < player.y:
        enemy.y = enemy.y + 1
    if enemy.y > player.y:
        enemy.y = enemy.y - 1
     
   
                
def End():
    global game_over
    game_over = True
    a = True
    
def on_mouse_down(pos):
    global skin
    global score
    if player.collidepoint(pos):
            if len(skins) == 1:
                skin = 1
                skins.append('fish')
                player.image = (skins[skin])
                score -= 100
                
   
    
    



place_coin()
place_enemy()


place_actors()
pgzrun.go()