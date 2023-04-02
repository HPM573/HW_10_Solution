import deampy.statistics as stat
import numpy as np


class Game:
    def __init__(self, id, prob_head):
        self.id = id
        self.probHead = prob_head
        self.countWins = 0

    def simulate(self):
        """
        simulates 20 coin tosses and counts the number of times {T, T, H} occurred
        """

        # random number generator
        rnd = np.random.RandomState(seed=self.id)

        n_consecutive_tails = 0  # number of consecutive tails so far, set to 0

        # flip the coin 20 times
        for i in range(20):

            # find if this flip resulted in head or tail
            if rnd.random_sample() < self.probHead:

                # if it is head, check if the last 2 tosses resulted in {T, T}
                if n_consecutive_tails >= 2:
                    # if so, {T, T, H} has occurred
                    self.countWins += 1

                # if this is tail, we set the number of consecutive tails to 0
                n_consecutive_tails = 0

            else:
                # this flip resulted in tail, so we increment the number of consecutive tails by 1
                n_consecutive_tails += 1

    def get_reward(self):
        """
        :return: the reward from this game = 100 * (number of {T, T, H}) - 250
        """
        return 100 * self.countWins - 250


class SetOfGames:
    # class to simulate the game multiple times

    def __init__(self, id, prob_head):

        self.id = id
        self.probHead = prob_head
        self.gameRewards = []
        self.gameIfLoss = []  # list of 0 and 1, where 1 represents loss and 0 represents win.
        self.statRewards = None # stat to collect total rewards
        self.statIfLoss = None  # stat to collect number of losses

    def simulate(self, n_games):

        for i in range(n_games):
            # create a new game
            game = Game(id=self.id*n_games+i, prob_head=self.probHead)
            # simulate the game with 20 flips
            game.simulate()
            # get the reward
            reward = game.get_reward()
            # store the reward
            self.gameRewards.append(reward)
            # find if we lost in this game
            if reward < 0:
                self.gameIfLoss.append(1)
            else:
                self.gameIfLoss.append(0)

        self.statRewards = stat.SummaryStat(name='Reward', data=self.gameRewards)
        self.statIfLoss = stat.SummaryStat(name='Probability  of loss', data=self.gameIfLoss)


class MultipleGameSets:
    # class to simulate multiple game sets

    def __init__(self, ids, prob_head):

        self.ids = ids
        self.probHead = prob_head

        self.gameSetRewards = []
        self.statGameSetRewards = None

    def simulate(self, n_games_in_set):

        for i in self.ids:
            set_of_games = SetOfGames(id=i, prob_head=self.probHead)
            set_of_games.simulate(n_games=n_games_in_set)

            self.gameSetRewards.append(set_of_games.statRewards.get_total())

        self.statGameSetRewards = stat.SummaryStat(name='Mean Rewards', data=self.gameSetRewards)
