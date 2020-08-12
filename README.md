# Tapao
A terminal game based on the brazilian card game "tapão", its rules and additional information are described [here](http://jogosdecartas.hut.com.br/tapao/) (in portuguese).

This game was designed with the goal of learning and practicing the use of threads and their correct synchronization with the help of Locks and Events. Each of the two players has its own thread that catches and handles keyboard events, the screen is also managed by another thread and they all share the three decks in the game: two belonging to each player and one that "sits" on the table.

## Dependencies
- Python 3.6+
- pip module

## Basic rules
- The game has 2 players
- Both players starts with 26 cards, randomly distributed
- Each round belongs to a player (starting with player 2 and alternating), which means that only that player can put the top card of his deck on the table (the center of the screen)
- On each round, the "counting" card (at the top of the screen) increases by 1
- Any player can "beat" on the table at any round
  - If, at the time of the beating, the card on the table equals the counting card, the other player receives all the tables' cards
  - If the player misses the timing, the same player receives the tables' cards
- The first player who has an empty deck that correctly hits the beating time wins the game!
- If both players reaches an empty deck, nobody wins

## How to run
Install the requirements (append the `--user` flag if not in a virtual env):
```
pip install -r requirements.txt
```
Play:
```
python tapao.py
```
