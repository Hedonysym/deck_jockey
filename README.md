this is a placeholder readme for now.
this repo will eventually hold a textbased card game called deck_jockey.
this game is solitaire for now but may be updated later to allow multiple players.
the goal is to use 3 card types in conjunction to reach the production goal in the least number of turns, command cards, loop cards, and operator cards.
commands can be played stright to the board and do a one time effect before being discarded.
loops can be used to play the same command for multiple turns at the cost of more resources.
operators can modify both commands and loops for additional effect.
fututre versions may allow players to interact wiyth eachother and disrupt their plays to get their own plays done faster, and other versions may have
other decks to play around with.

for now this game will only require python and bash, idk how this is gonna go fully yet.


upon running main:
- opens a prompt for player name and decklist
- creates a deck object of the proper list and applys it to the player
- runs the game

the game:
- each turn shows current production level and increments max resource
- draws to fill handsize 5
- activates any loops and decrements thir counts
- lists hand and waits for input
- after turn is passed checks to see if production is 10 or more, ends the game and displays final turn count or goes to next turn

player actions:
- show hand - lists hand
- show {card} - displays card text of selected card
- play {card} - plays card of appropriate action
    - operator - prompts an applicable card
    - loop - prompts an applicable card and appends itself and the card it loops to looper
    - command - activates with any modifiers applied
- trash {card} - discards a card without playing
- quit