from graphics import *
import random

# Function to draw the archery target
def draw_target(win):
    colors = ['white', 'black', 'blue', 'red', 'yellow']
    radius = 100
    for color in colors:
        circle = Circle(Point(250, 250), radius)
        circle.setFill(color)
        circle.draw(win)
        radius -= 20

# Function to simulate a turn and return the score
def simulate_turn(win, player, scores):
    score = 0
    color = 'red' if player == 1 else 'blue'
    for _ in range(3):
        x = random.uniform(50, 450)
        y = random.uniform(50, 450)
        dart = Circle(Point(x, y), 5)
        dart.setFill(color)
        dart.draw(win)
        score += calculate_score(x, y)
    update_scores(scores, player, score)
    return score

# Function to calculate the score based on dart location
def calculate_score(x, y):
    distance = ((x - 250) ** 2 + (y - 250) ** 2) ** 0.5
    if distance <= 20:
        return 9
    elif distance <= 40:
        return 7
    elif distance <= 60:
        return 5
    elif distance <= 80:
        return 3
    elif distance <= 100:
        return 1
    else:
        return 0

# Function to update scores in the dictionary
def update_scores(scores, player, score):
    if player not in scores:
        scores[player] = 0
    scores[player] += score

# Function to display the scoreboard
def display_scoreboard(win, scores):
    scoreboard = Text(Point(250, 20), "Scoreboard")
    scoreboard.draw(win)
    y_position = 40
    for player, score in scores.items():
        scoreboard_entry = Text(Point(250, y_position), f"Player {player}: {score}")
        scoreboard_entry.draw(win)
        y_position += 20

# Function to display the winner
def display_winner(scores):
    player1_score = scores.get(1, 0)
    player2_score = scores.get(2, 0)

    if player1_score > player2_score:
        return "Player 1 wins!"
    elif player2_score > player1_score:
        return "Player 2 wins!"
    else:
        return "It's a tie!"

# Main function to run the game
def main():
    win = GraphWin("Archery Target", 500, 500)
    draw_target(win)

    # Database to store scores
    scores = {}

    # Label for advancing turns
    label = Text(Point(250, 470), "Click to advance to the next player's turn")
    label.draw(win)

    # Simulate 5 turns for each player
    for turn in range(1, 6):
        label.setText(f"Turn {turn}: Player 1's turn")
        win.getMouse()  # Wait for mouse click to proceed to next turn
        player1_score = simulate_turn(win, 1, scores)

        label.setText(f"Turn {turn}: Player 2's turn")
        win.getMouse()  # Wait for mouse click to proceed to next turn
        player2_score = simulate_turn(win, 2, scores)
    

    display_scoreboard(win, scores)
    label.setText(display_winner(scores))
    win.getMouse()  # Wait for mouse click to close the window
    win.close()

if __name__ == "__main__":
    main()
