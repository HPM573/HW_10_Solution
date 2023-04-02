import deampy.plots.histogram as hist
import deampy.statistics as stats

import InputData as D


def print_outcomes(set_of_games, strategy_name):
    """ prints the outcomes of a simulated set of games under steady state
    :param set_of_games: a simulated set of games
    :param strategy_name: the name of the selected therapy
    """

    # create a summary statistics
    rewards_stat = stats.SummaryStat(name='Game Rewards',
                                     data=set_of_games.gameRewards)

    # get mean and confidence interval
    mean = rewards_stat.get_mean()
    conf_int = rewards_stat.get_t_CI(alpha=D.ALPHA)

    # print survival time statistics
    print(strategy_name)
    print("  Expected casino owner's payment to the gambler "
          "(if negative, it means that the gambler is paying to the casino owner):\n  {:.{prec}%} confidence interval:"
          .format(1 - D.ALPHA, prec=0), mean, conf_int)


def plot_histograms(set_of_games_fair_coin, set_of_games_unfair_coin):
    """ plots the histograms of casio owner's rewards
    :param set_of_games_fair_coin: a simulated set of games with fair coin
    :param set_of_games_unfair_coin: a simulated set of games with unfair coin
    """

    # get survival curves of both treatments
    set_of_game_rewards = [
        set_of_games_fair_coin.gameRewards,
        set_of_games_unfair_coin.gameRewards
    ]

    # graph histograms
    hist.plot_histograms(
        data_sets=set_of_game_rewards,
        title="Histogram of the casino owner's payment to the gambler",
        x_label='Payment',
        y_label='Counts',
        bin_width=100,
        legends=['Fair Coin', 'Unfair Coin'],
        transparency=0.5
    )


def print_comparative_outcomes(set_of_games_fair_coin, set_of_games_unfair_coin):
    """ print the increase in casio owner's rewards
    :param set_of_games_fair_coin: a simulated set of games with fair coin
    :param set_of_games_unfair_coin: a simulated set of games with unfair coin
    """

    # create a difference statistics for the increase in game reward
    increase_reward = stats.DifferenceStatIndp(
        name='Increase in game reward',
        x=set_of_games_unfair_coin.gameRewards,
        y_ref=set_of_games_fair_coin.gameRewards
    )

    # get mean and t-based confidence interval for the increase in game reward
    mean = increase_reward.get_mean()
    conf_int = increase_reward.get_t_CI(alpha=D.ALPHA)

    print("Change in casino owner's payment to the gambler due to using the unfair coin "
          "and {:.{prec}%} confidence interval:"
          .format(1 - D.ALPHA, prec=0), mean, conf_int)
