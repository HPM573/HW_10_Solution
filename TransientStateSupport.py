import SimPy.FigureSupport as Figs
import SimPy.StatisticalClasses as Stat
import InputData as D


def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    rewards_stat = Stat.SummaryStat(name='Game Rewards', data=multi_cohort.meanGameRewards)

    # get mean and t-based confidence interval
    mean = rewards_stat.get_mean()
    pred_int = rewards_stat.get_PI(alpha=D.ALPHA)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean game reward for the gambler and {:.{prec}%} prediction interval:"
          .format(1 - D.ALPHA, prec=0), mean, pred_int)


def draw_histograms(multicohort_output_fair_coin, multi_cohort_output_biased_coin):
    """ draws the histograms of average survival time
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # histograms of average survival times
    set_of_game_rewards = [
        multicohort_output_fair_coin.meanGameRewards,
        multi_cohort_output_biased_coin.meanGameRewards
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of the gamblers average total',
        x_label='Mean Game Rewards',
        y_label='Counts',
        bin_width=0.5,
        legend=['Fair Coin', 'Biased Coin'],
        transparency=0.5
    )


def print_comparative_outcomes(multi_cohort_fair_coin, multi_cohort_biased_coin):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # increase in game reward
    increase_stat = Stat.DifferenceStatIndp(
        name='Increase in mean game reward',
        x=multi_cohort_biased_coin.meanGameRewards,
        y_ref=multi_cohort_fair_coin.meanGameRewards
    )
    # mean and prediction interval
    mean = increase_stat.get_mean()
    pred_int = increase_stat.get_PI(alpha=D.ALPHA)

    print("Expected increase in mean survival time (years) and {:.{prec}%} prediction interval:"
          .format(1 - D.ALPHA, prec=0), mean, pred_int)

