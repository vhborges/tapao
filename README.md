# Tapao
A terminal game based on the brazilian card game "tapão", its rules and additional information are described [here](http://jogosdecartas.hut.com.br/tapao/) (in portuguese).<br>
## Dependencies
- Python 3.6+
- pip module
## How to run
Install the requirements (append the `--user` flag if not in a virtual env):
```
pip install -r requirements.txt
```
Play:
```
python tapao.py
```
## Basic rules
- The game has 2 players
- Both players starts with 26 cards, randomly distributed
- Each round belongs to a player (starting with player 2 and alternating), which means that only that player can put the top card of his deck on the table (the center of the screen)
- On each round, the "counting" card (at the top of the screen) increases by 1
- Any player can "beat" on the table at any round
  - If, at the time of the beating, the card on the table equals the counting card, the other player receives all the tables' cards
  - Or else, if the player misses the timing, the same player receives the tables' cards
- The first player who has an empty deck that correctly hits the beating time wins the game!
- If both players reaches an empty deck, nobody wins
