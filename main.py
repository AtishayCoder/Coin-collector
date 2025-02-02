from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

fox  = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text(f"Score: {score}", color="black", topleft=(10, 10))

    if game_over:
        screen.fill("red")
        screen.draw.text(f"Final Score: {score}", topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        fox.x -= 2
    elif keyboard.right:
        fox.x += 2
    elif keyboard.up:
        fox.y -= 2
    elif keyboard.down:
        fox.y += 2

    if fox.colliderect(coin):
        score += 10
        place_coin()

clock.schedule(time_up, 7.0)
place_coin()

# Use pgzrun main.py to play!
