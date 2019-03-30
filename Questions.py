import InputData as D
import Classes as Cls
import SupportSteadyState as Support
import TransientStateSupport as Transient


#STEADY STATE
gamesFair = Cls.SetOfGames(
    id=1,
    prob_head=D.prob_head)
# simulate the cohort
gamesFair.simulate(n_games=D.n_games)

# create a cohort of patients for when the drug is available
gamesBiased = Cls.SetOfGames(
    id=2,   # since we don't have a mechanism to pair the simulated patients in
            # cohorts with and without the drug, we chose a different random number seed
            # for these two cohorts so that they remain independent from each other.
    prob_head=D.prob_head * D.unfairness_ratio)
# simulate the cohort
gamesBiased.simulate(n_games=D.n_games)

# print outcomes of each cohort
Support.print_outcomes(simulated_cohort=gamesFair,
                       strategy_name='When probability of heads is 0.5:')
Support.print_outcomes(simulated_cohort=gamesBiased,
                       strategy_name='When probability of heads is 0.45:')

# draw survival curves and histograms
Support.draw_survival_curves_and_histograms(cohort_fair_coin=gamesFair,
                                            cohort_biased_coin=gamesBiased)

# print comparative outcomes
Support.print_comparative_outcomes(output_fair_coin=gamesFair,
                                   output_biased_coin=gamesBiased)


#TRANSIENT STATE
multi_gamesFair = Cls.MultipleGameSets(
    ids=range(D.n_simulated_games),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    prob_head=[D.prob_head] * D.n_simulated_games  # [p, p, ...]
)
# simulate all cohorts
multi_gamesFair.simulate(n_games_in_set=D.games_in_set)

# create multiple cohorts for when the drug is available
multi_gamesBiased = Cls.MultipleGameSets(
    ids=range(D.n_simulated_games),
        # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
        # since we don't have a mechanism to pair the simulated patients in
        # cohorts with and without the drug, we chose a different random number seed
        # for these two cohorts so that they remain independent from each other.
    prob_head=[D.prob_head * D.unfairness_ratio] * D.n_simulated_games
)
# simulate all cohorts
multi_gamesBiased.simulate(n_games_in_set=D.games_in_set)

# print outcomes of each cohort
Transient.print_outcomes(multi_cohort=multi_gamesFair, strategy_name='When the probability of heads is 0.5:')
Transient.print_outcomes(multi_cohort=multi_gamesBiased, strategy_name='When the probability of heads is 0.45:')

# draw histograms of average survival time
Transient.draw_histograms(multicohort_output_fair_coin=multi_gamesFair,
                          multi_cohort_output_biased_coin=multi_gamesBiased)

# print comparative outcomes
Transient.print_comparative_outcomes(multi_cohort_fair_coin=multi_gamesFair,
                                   multi_cohort_biased_coin=multi_gamesBiased)
