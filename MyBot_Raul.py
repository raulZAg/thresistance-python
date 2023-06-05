from player import Bot
from game import State
import random

# run this with python competition.py 10000 bots/intermediates.py bots/MyBot_Raul.py  
# We can also run it with experts bots with this line: python competition.py 10000 bots/experts.py bots/MyBot_Raul.py

class MyBot_Raul(Bot):



    def __init__(self, game, index, spy):

        """Constructor called before a game starts.  It's recommended you don't
        override this function and instead use onGameRevealed() to perform
        setup for your AI.
        @param game     the current game state
        @param index    Your own index in the player list.
        @param spy      Are you supposed to play as a spy?
        """
        super(Bot, self).__init__(self.__class__.__name__, index)

        self.game = game
        self.spy = spy

        list_info = () # list to store information
        Theta = [.25, .25, .25, .25]  # final probability used
        alpha = 0.5 #if a spy screws up, make it a little bit bigger
        beta = .01  # if memeber of the resistance screws up big time, we make it almost zero so it doesn't have big implications







    def select(self, players, count):
        if self.spy == True:
            if self.game.turn == 1:
                return [self] + self.game.resistance[random.choice(self.game.resistance)] 
            else:
                if self.game.turn == 2:
                    if self.game.wins == 0 and self.have_sabotaged == True:
                        return self.other_spies[0] + random.sample(self.game.resistance,len(self.game.resistance))[0:2] 
                    else:
                        return [self] + random.sample(self.game.resistance,len(self.game.resistance))[0:2] 
                else:
                    if self.game.turn == 3:
                        if self.game.wins != 0:
                            if self.game.wins == 1:
                                return [self] + self.other_spies[0]
                            else:
                                if Theta[self] > Theta[self.other_spies]:
                                    return self.other_spies + self.game.resistance[random.choice(self.game.resistance)]
                                else:
                                    return [self] + self.game.resistance[random.choice(self.game.resistance)]
                        else: 
                            if self.game.leader.player_index == self.game.other_spies.player_index-1 or self.game.leader.player_index == self.game.other_spies.player_index-2: #his turn is in 1 or 2 after mine
                                if Theta[self] > Theta[self.other_spies]:
                                    return self.other_spies + self.game.resistance[random.choice(self.game.resistance)] 
                                else: 
                                    return [self] + self.game.resistance[random.choice(self.game.resistance)]
                            else: 
                                return self.game.resistance
                    else:                                   # up from this we want to decide others based on who has the most probabily 
                        if self.game.turn == 4:
                            if self.game.wins == 1:
                                if min(Theta[self], Theta[self.other_spies]) >= min(Theta[self.game.resistance]):
                                    if self.game.leader.player_index == self.game.other_spies.player_index-1: # other spy goes one turn after
                                        return self.game.others
                                    else:
                                        return [self] + min(Theta[self.game.resistance])
                                else:
                                    return [self] + min(Theta[self.game.resistance]) 
                            else:
                                return min(Theta[self], Theta[self.other_spies]) + min(Theta[self.game.resistance]) # need to return two of the resistance
                        else:
                            return min(Theta[self], Theta[self.other_spies]) + min(Theta[self.game.resistance]) # need to return two of the resistance

        else:  # we always return ourselves and others based on their probability of being spies

            if self.game.turn == 1 or self.game.turn == 3:

                return self + min(Theta[self.others]) #need to be the correct number of othe players returned

            else: 

                return self + min(Theta[self.others]) #need to be the correct number of othe players returned



    def vote(self, team):

            # depending if your position and the other spy's position is the optimal we decide to vote or not

        if self.spy == True:
            if self.game.turn != 1:
                if self.game.other_spies[0] in self.game.team:

                    return True 

                else:
                    return False
            else: 
                return True 

        else:  # using our function we would determine the probability of those players being spies 

            if self.game.team == min(Theta[self.others]):
                return True 
            else: 
                return False
                
    def sabotage(self):

        if self.spy == True:
            if (self.game.turn == 1 or self.game.turn == 3):
                if (self.game.turn == 3 and self.game.wins == 2):
                    self.have_sabotaged = True
                    return True
                else:
                    return False

            if (self.game.turn == 2 or self.game.turne == 4 or self.game.turn ==5):
                if (self.game.turn == 4 or self.game.turn == 5):
                    self.have_sabotaged = True
                    return True

                else: 
                    if self.game.wins != 0:
                        self.have_sabotaged = True
                        return True 
                    else:
                        other_spies = []
                        for player in self.game.spies:
                            if player != self:
                                other_spies.append(player)
                                if player in self.game.team: #This means you have another spy on the current team
                                    if self.have_sabotaged == False:
                                        return True

                                    else:
                                        return False

        return False 

    def update_function(self, x=()):  #function used to update the probability function, it needs adjustments because of the missing three functions I explained on the written report

        for i in range (len(x)):
            Theta *= update_function(self, i)

            for j in range(len(x)):
                Theta[j] +=prob_function(j)

    def prob_function(x):  # probability function used to determine the probabities. It is missing the three functions I explained on the written report and therefore it is not complete

        r = self.turn 
        w = self.wins


        if x["D_type"]==1:
            member1 = list_info[i-2]["Nom1"]
            member2 = list_info[i-2]["Nom2"]
            theta_i = Theta[member1]
            theta_j = Theta[member2]


            return (1-(1-theta_i)*(1-theta_j)) * ((1-alpha)*(x["Sabo"]>=1)*(r==3 and w==1)+(x["Sabo"]==0)*(alpha)*(not(r==3 and w==1)))+(1-theta_i)*(1-theta_j)*((1-beta)(x["Sabo"]==0) + beta*(x["Sabo"]>=1)) 

 
        else:

            return None

           # This is where I would add the other functions instead of returning None. They would be based on "D_type" == 2, 3 or 4
           # 2 - add member3
           # 3 - add vote 
           # 4 - selection 


    def fill_list(self, d_type, sab, nom1, nom2, nom3, vote_mission, team_leader):  # this is how we fill the list of information using the dictionary

        dict_info = {"D_type":d_type, "Sabo":sab, "Nom1":nom1, "Nom2":nom2, "Nom2":nom2, "Vote_mission":vote_mission, "Team_leader":team_leader}

        return dict_info

        
    def onVoteComplete(self, votes):
        """Callback once the whole team has voted.
        @param votes        Boolean votes for each player (ordered).
        """

        self.round_game = 0
        self.vote_result = votes 

        if sum(votes) >= 3:
            self.round_game += 1


        list_info.append(fill_list(3, None, None, None, None, self.vote_result, None))    # what information I store depending on the callback


        pass 
    def onGameRevealed(self, players, spies):
        """This function will be called to list all the players, and if you're
        a spy, the spies too -- including others and yourself.
        @param players  List of all players in the game including you.
        @param spies    List of players that are spies, or an empty list.
        """

        self.have_sabotaged = False
        self.other_spies = []
        self.resistance = []

        for player in spies:
            if player != self:
                self.other_spies.append(player)
        for player in self.game.players:
            if player != self and self.spy == True:
                self.resistance.append(player)

        for player in players:
            player_index = self.player.split('-') 

        pass # TODO complete this function
    def onMissionComplete(self, num_sabotages):
        """Callback once the players have been chosen.
        @param num_sabotages    Integer how many times the mission was sabotaged.
        """

        list_info.append(fill_list(self.team_size==2 + 2*(self.team_size==3), num_sabotages, None, None, None, None, None)) # what information I store depending on the callback


        pass # TODO complete this function
    def onGameComplete(self, win, spies):
        """Callback once the game is complete, and everything is revealed.
        @param win          Boolean true if the Resistance won.
        @param spies        List of only the spies in the game.
        """
        pass 

    def onTeamSelected(self, leader, team):
        """Called immediately after the team is selected to go on a mission,
        and before the voting happens.
        @param leader   The leader in charge for this mission.
        @param team     The team that was selected by the current leader.
        """
        self.team_size=len(self.team)
        self.team_leader= leader 

        member3 = None
        if self.team_size == 3: 
            member3 = self.game[2]

        list_info.append(fill_list(4, None, self.game.team[0], self.game.team[1], member3, None, self.team_leader))  # what information I store depending on the callback

        pass


