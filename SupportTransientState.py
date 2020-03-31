import SimPy.Plots.Histogram as Hist
import SimPy.StatisticalClasses as Stat
import InputData as D


def print_outcomes(multi_game_sets, strategy_name):
    """ prints the outcomes of a simulated multiple game sets
    :param multi_game_sets: multiple game sets
    :param strategy_name: the name of the selected therapy
    """

    rewards_stat = Stat.SummaryStat(name='Game Rewards',
                                    data=multi_game_sets.gameSetRewards)

    # get mean and prediction interval
    mean = rewards_stat.get_mean()
    pred_int = rewards_stat.get_PI(alpha=D.ALPHA)

    # print survival time statistics
    print(strategy_name)
    print("  Average of total reward from 10 games and {:.{prec}%} prediction interval:"
          .format(1 - D.ALPHA, prec=0), mean, pred_int)


def draw_histograms(multi_game_sets_fair_coin, multi_game_sets_unfair_coin):
    """ draws the histograms of total rewards
    :param multi_game_sets_fair_coin: multiple game sets with fair coin
    :param multi_game_sets_unfair_coin: multiple game sets with unfair coin
    """

    # histograms of total rewards
    set_of_game_rewards = [
        multi_game_sets_fair_coin.gameSetRewards,
        multi_game_sets_unfair_coin.gameSetRewards
    ]

    # graph histograms
    Hist.plot_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of the gamblers total reward from 10 games',
        x_label='Mean Game Rewards',
        y_label='Counts',
        bin_width=100,
        legends=['Fair Coin', 'Unfair Coin'],
        transparency=0.5
    )


def print_comparative_outcomes(multi_game_sets_fair_coin, multi_game_sets_unfair_coin):
    """ prints expected increase in gambler's total reward
    :param multi_game_sets_fair_coin: multiple game sets with fair coin
    :param multi_game_sets_unfair_coin: multiple game sets with unfair coin
    """

    # increase in game reward
    increase_stat = Stat.DifferenceStatIndp(
        name='Increase in average total reward',
        x=multi_game_sets_unfair_coin.gameSetRewards,
        y_ref=multi_game_sets_fair_coin.gameSetRewards
    )
    # mean and prediction interval
    mean = increase_stat.get_mean()
    pred_int = increase_stat.get_PI(alpha=D.ALPHA)

    print("Increase in average of total reward from 10 games and {:.{prec}%} prediction interval:"
          .format(1 - D.ALPHA, prec=0), mean, pred_int)

