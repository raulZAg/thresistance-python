# The Resistance Bot - "MyBot_Raul"

This repository contains a Python agent for the card game The Resistance, developed using The Resistance Python framework by Joseph Walton-Rivers. The bot, named "MyBot_Raul", uses a combination of decision trees and Bayesian statistics to make decisions during gameplay.

## Project Overview

"The Resistance" is a social deduction game for 5-10 players. Players are either members of the Resistance or Spies. In several rounds, teams are selected to go on missions. Spies aim to sabotage missions while the Resistance tries to succeed. The game's outcome is decided when a certain number of missions have either succeeded (Resistance wins) or failed (Spies win). In this project, I've developed a bot that can play The Resistance in different groups of previously programmed bots.

The logic of "MyBot_Raul" is based on a combination of decision trees and Bayesian statistics. The bot uses a series of decision rules, based on the current state of the game, to make its decisions. It also incorporates a probability function to update the bot's knowledge state and make decisions accordingly.

## Getting Started

Here are the steps to run "MyBot_Raul" in a Hanabi game:

Make sure Python is installed on your system.
Clone this repository to your local machine.
Navigate to the directory where the bot file (MyBot_Raul.py) is located.

To run a game with "MyBot_Raul" against intermediate bots, use the following command:

```python
python competition.py 10000 bots/intermediates.py bots/MyBot_Raul.py
```

To run a game with "MyBot_Raul" against expert bots, use the following command:

```python
python competition.py 10000 bots/experts.py bots/MyBot_Raul.py
```

## File Overview

MyBot_Raul.py: This is the main bot file. It contains the logic and decision rules for the bot to play The Resistance.
In 'The Resistance' folder is everything needed to run the project. This is what I used to play The Resistance with my bot. 

## Bot Strategy

"MyBot_Raul" uses a series of decision trees based on the current state of the game, as well as Bayesian statistics to update the bot's knowledge state and make decisions accordingly.

## Decision Trees
The bot makes decisions based on several factors including the current turn, the number of game wins, and whether it is a spy. Decisions include team selection and whether to sabotage.

## Bayesian Statistics
The bot uses Bayesian statistics to update its knowledge state. It uses a probability function to determine the likelihood of certain events, which it then uses to make decisions.


### License

This project is open source under the MIT License.
