import SimPy.StatisticalClasses as Stat
import InputData as D
import SimPy.FigureSupport as Figs


def print_outcomes(simulated_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param simulated_cohort: a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # create a summary statistics
    rewards_stat = Stat.SummaryStat(name='Game Rewards', data=simulated_cohort.gameRewards)

    # get mean and confidence confidence interval
    mean = rewards_stat.get_mean()
    conf_int = rewards_stat.get_t_CI(alpha=D.ALPHA)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean reward for casino owner and {:.{prec}%} confidence interval:"
          .format(1 - D.ALPHA, prec=0), mean, conf_int)


def draw_survival_curves_and_histograms(cohort_fair_coin, cohort_biased_coin):
    """ draws the survival curves and the histograms of survival time
    :param cohort_no_drug: a cohort simulated when drug is not available
    :param cohort_with_drug: a cohort simulated when drug is available
    """

    # get survival curves of both treatments
    set_of_game_rewards = [
        cohort_fair_coin.get_rewards(),
        cohort_biased_coin.get_rewards()
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


def print_comparative_outcomes(output_fair_coin, output_biased_coin):
    """ prints expected and percentage increase in survival time when drug is available
    :param cohort_no_drug: a cohort simulated when drug is not available
    :param cohort_with_drug: a cohort simulated when drug is available
    """

    # create a difference statistics for the increase in game reward
    increase_reward = Stat.DifferenceStatIndp(
        name='Increase in game reward',
        x=output_biased_coin.get_rewards(),
        y_ref=output_fair_coin.get_rewards()
    )

    # get mean and t-based confidence interval for the increase in game reward
    mean = increase_reward.get_mean()
    conf_int = increase_reward.get_t_CI(alpha=D.ALPHA)

    print("Average increase in survival time (years) and {:.{prec}%} confidence interval:"
          .format(1 - D.ALPHA, prec=0), mean, conf_int)
