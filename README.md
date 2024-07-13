# Rock-Paper-Scissors with AI using MediaPipe and OpenCV
# Features
Real-time Hand Gesture Recognition: The application captures video from a webcam and uses MediaPipe to identify hand landmarks.
Gesture Detection: Recognizes 'Rock', 'Paper', and 'Scissors' gestures based on finger positions.
Interactive Gameplay: Plays Rock-Paper-Scissors against the computer, with real-time updates on the screen.
Score Tracking: Keeps track of the player's and computer's scores throughout the game.

pip install opencv-python mediapipe

# Usage
Run the Game

python rock_paper_scissors.py
Play and Enjoy

The webcam will start capturing your hand gestures.
Show 'Rock', 'Paper', or 'Scissors' gestures to the camera.
The AI will recognize your gesture, make its move, and display the result on the screen.
Press 'q' to quit the game.
How it Works
MediaPipe Hands: Utilized for detecting hand landmarks and identifying finger positions.
Gesture Recognition: Based on the positions of specific landmarks, the program determines which gesture is being shown.
Game Logic: The game logic compares the player's gesture with a randomly chosen gesture by the computer and updates the scores accordingly.

# Example

Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.
