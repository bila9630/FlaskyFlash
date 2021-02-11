from flask import Flask, render_template, url_for, request, redirect
from ai import ultimateAI
app = Flask(__name__)

moves = ["rock", "paper", "scissors"]


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        if not ('wins' in globals()):
            global wins
            wins = 0

        # getting respond from player
        player_move = request.form['content']
        # check if input is legit
        if not player_move in moves:
            return render_template('index.html',
                                   result="can't process input. Pls enter rock, paper or scissor",
                                   wins_score=wins)

        # AI responds xD
        AI_move = ultimateAI(player_move)

        wins += 1

        if wins >= 6:
            wins = 1

        return render_template('index.html',
                               player_text=f"you picked: {player_move}",
                               AI_text=f"AI picked: {AI_move}",
                               losing_text=f"you lose this round!",
                               score=f"You: 0    AI: {wins}",
                               wins_score=wins)
    else:
        return render_template('index.html', wins_score=0)


if __name__ == "__main__":
    app.run(debug=True)
