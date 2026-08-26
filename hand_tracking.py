import cv2
import mediapipe as mp

class HandDetector:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mpDraw = mp.solutions.drawing_utils


    def find_hand(self, frame):

        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        result=self.hands.process(rgb)

        if result.multi_hand_landmarks:

            for hand in result.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(
                    frame,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )

                h,w,c=frame.shape

                lm=hand.landmark[8]

                cx=int(lm.x*w)

                cy=int(lm.y*h)

                return (cx,cy)
   return none
