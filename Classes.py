import numpy as np
import SimPy.StatisticalClasses as Stat


class Game:
    def __init__(self, id, prob_head):
        self.id = id
        self.rnd = np.random.RandomState(seed=id)
        self.probHead = prob_head
        self.countWins = 0

    def simulate(self):
        """
        simulates 20 coin tosses and counts the number of times {T, T, H} occurred
        """

        n_consecutive_tails = 0  # number of consecutive tails so far, set to 0

        # flip the coin 20 times
        for i in range(20):

            # find if this flip resulted in head or tail
            if self.rnd.random_sample() < self.probHead:

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
    def __init__(self, id, prob_head):

        self.id = id
        self.probHead = prob_head
        self.gameRewards = []
        self.gameIfLoss = []  # list of 0 and 1, where represents loss and 0 represents win.
        self.outcomes = None

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

        self.outcomes = SetOfGamesOutcomes(game_rewards=self.gameRewards,
                                           game_if_loss=self.gameIfLoss)


class SetOfGamesOutcomes:
    def __init__(self, game_rewards, game_if_loss):

        self.statRewards = Stat.SummaryStat('Reward', game_rewards)
        self.statIfLoss = Stat.SummaryStat('Probability  of loss', game_if_loss)

    def get_ave_reward(self):
        return self.statRewards.get_mean()

    def get_total_reward(self):
        return self.statRewards.get_total()

    def get_CI_reward(self, alpha):
        return self.statRewards.get_t_CI(alpha)

    def get_min_reward(self):
        return self.statRewards.get_min()

    def get_max_reward(self):
        return self.statRewards.get_max()

    def get_loss_prob(self):
        return self.statIfLoss.get_mean()

    def get_CI_prob_Loss(self, alpha):
        return self.statIfLoss.get_t_CI(alpha)


class MultipleGameSets:
    def __init__(self, ids, prob_head):
        self.ids = ids
        self.probHead = prob_head

        self.gameSetRewards = []
        self.statMultipleGameRewards = None

    def simulate(self, n_games_in_set):

        for i in self.ids:
            set_of_games = SetOfGames(id=i, prob_head=self.probHead)
            set_of_games.simulate(n_games=n_games_in_set)

            self.gameSetRewards.append(set_of_games.outcomes.get_total_reward())

        self.statMultipleGameRewards = Stat.SummaryStat('Mean Rewards', self.gameSetRewards)
