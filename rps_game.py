import cv2
import mediapipe as mp
import random
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

gestures = ['Rock', 'Paper', 'Scissors']
rules = {
    ('Rock', 'Scissors'): 'Player wins!',
    ('Scissors', 'Paper'): 'Player wins!',
    ('Paper', 'Rock'): 'Player wins!',
    ('Scissors', 'Rock'): 'Computer wins!',
    ('Paper', 'Scissors'): 'Computer wins!',
    ('Rock', 'Paper'): 'Computer wins!',
    ('Rock', 'Rock'): 'It\'s a draw!',
    ('Paper', 'Paper'): 'It\'s a draw!',
    ('Scissors', 'Scissors'): 'It\'s a draw!'
}

player_score = 0
computer_score = 0

def get_hand_gesture(image):
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_up = [(hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y) for i in [8, 12, 16, 20]]
            if all(fingers_up):
                return 'Paper'
            if fingers_up[0] and fingers_up[1] and not fingers_up[2] and not fingers_up[3]:
                return 'Scissors'
            if not any(fingers_up):
                return 'Rock'
    return 'Unknown'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    player_gesture = get_hand_gesture(frame)
    if player_gesture != 'Unknown':
        computer_gesture = random.choice(gestures)
        result = rules.get((player_gesture, computer_gesture), 'Invalid gestures')

        if result == 'Player wins!':
            player_score += 1
        elif result == 'Computer wins!':
            computer_score += 1

        for text, y in [(f"Player: {player_gesture}", 30), 
                        (f"Computer: {computer_gesture}", 70), 
                        (result, 110), 
                        (f"Player Score: {player_score}", 150), 
                        (f"Computer Score: {computer_score}", 190)]:
            cv2.putText(frame, text, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('Rock Paper Scissors', frame)
        time.sleep(1)

    cv2.imshow('Rock Paper Scissors', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
