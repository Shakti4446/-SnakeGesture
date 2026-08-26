import cv2
import pygame
from hand_tracking import HandDetector
import snake_game as game

pygame.init()
# dector hand detector 
detector=HandDetector()

cap=cv2.VideoCapture(0,cv2.CAP_AVFOUNDATION)

clock=pygame.time.Clock()

running=True

while running:

    ret,frame=cap.read()

    if not ret:
        break

    frame=cv2.flip(frame,1)

    pos=detector.find_hand(frame)

    if pos:

        x=int(pos[0]*800/frame.shape[1])
        y=int(pos[1]*600/frame.shape[0])

        game.update_snake((x,y))

    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            running=False

    game.draw()

    cv2.imshow("Camera",frame)

    if cv2.waitKey(1)==27:

        break

    clock.tick(30)

cap.release()

cv2.destroyAllWindows()

pygame.quit()
