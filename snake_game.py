import pygame
import random
import math
import pyttsx3
import threading

pygame.init()

WIDTH,HEIGHT=800,600

screen=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("GOD VOICE Gesture Snake")

snake=[(200,200)]

food=(400,300)

score=0

game_over=False

start_voice=False

font=pygame.font.SysFont(None,40)

big_font=pygame.font.SysFont(None,80)


# -------- GOD VOICE --------

engine=pyttsx3.init()

engine.setProperty("rate",170)


def speak(text):

    def run():

        engine.say(text)

        engine.runAndWait()

    threading.Thread(target=run).start()



# -------- RESET --------

def reset_game():

    global snake,food,score,game_over,start_voice

    snake=[(200,200)]

    food=(random.randint(50,750),
          random.randint(50,550))

    score=0

    game_over=False

    start_voice=False



# -------- UPDATE --------

def update_snake(pos):

    global food,score,game_over,start_voice

    if game_over:
        return

    # FIRST TIME VOICE

    if not start_voice:

        speak("Welcome Player")

        start_voice=True


    snake.insert(0,pos)

    head=snake[0]


    # FOOD EAT

    if abs(head[0]-food[0])<20 and abs(head[1]-food[1])<20:

        score+=1

        speak(f"Score {score}")

        food=(random.randint(50,750),
              random.randint(50,550))

    else:

        if len(snake)>30:

            snake.pop()


    # COLLISION

    for body in snake[6:]:

        if math.hypot(

            head[0]-body[0],

            head[1]-body[1]

        )<10:

            game_over=True

            speak("Game Over. Try Again")



# -------- DRAW --------

def draw():

    screen.fill((10,20,40))


    pygame.draw.circle(screen,(255,50,50),food,12)


    for i,part in enumerate(snake):

        pygame.draw.circle(

            screen,(0,200,150),

            part,14)

        pygame.draw.circle(

            screen,

            (0,max(255-i*6,60),120),

            part,8)


    head=snake[0]


    pygame.draw.circle(

        screen,(0,255,0),

        head,10)


    # EYES

    pygame.draw.circle(

        screen,(255,255,255),

        (head[0]-4,head[1]-2),2)

    pygame.draw.circle(

        screen,(255,255,255),

        (head[0]+4,head[1]-2),2)



    text=font.render(

        f"Score : {score}",

        True,

        (255,255,255))

    screen.blit(text,(10,10))


    if game_over:

        over=big_font.render(

            "GAME OVER",

            True,

            (255,0,0))

        screen.blit(over,(240,230))

        pygame.display.update()

        pygame.time.delay(2000)

        reset_game()


    pygame.display.update()