import Classes as Cls
import InputData as D
import SupportSteadyState as SupportSteady
import SupportTransientState as SupportTransient

# STEADY STATE
# fair game
gamesFair = Cls.SetOfGames(
    id=1,
    prob_head=D.prob_head_fair)
# simulate
gamesFair.simulate(n_games=D.n_games)

# unfair game
gamesUnfair = Cls.SetOfGames(
    id=2,   # since we don't have a mechanism to pair the simulated games,
            # we chose a different random number seed for these two
            # games so that they remain independent of each other.
    prob_head=D.prob_head_unfair)
# simulate
gamesUnfair.simulate(n_games=D.n_games)

# print outcomes of each set of games
print("From the casio owner's perspective:")
SupportSteady.print_outcomes(set_of_games=gamesFair,
                             strategy_name='For a fair coin:')
SupportSteady.print_outcomes(set_of_games=gamesUnfair,
                             strategy_name='For an unfair coin:')

# plot histograms
SupportSteady.plot_histograms(set_of_games_fair_coin=gamesFair,
                              set_of_games_unfair_coin=gamesUnfair)

# print comparative outcomes
SupportSteady.print_comparative_outcomes(set_of_games_fair_coin=gamesFair,
                                         set_of_games_unfair_coin=gamesUnfair)


# TRANSIENT STATE
# for fair coin
multiGamesFair = Cls.MultipleGameSets(
    ids=range(D.n_simulated_games),
    prob_head=D.prob_head_fair)
# simulate all sets of games
multiGamesFair.simulate(n_games_in_set=D.games_in_set)

# for unfair coin
multiGamesUnfair = Cls.MultipleGameSets(
    ids=range(D.n_simulated_games, 2*D.n_simulated_games),
        # since we don't have a mechanism to pair the simulated games,
        # we chose a different random number seed for these two
        # games so that they remain independent of each other.
    prob_head=D.prob_head_unfair)
# simulate all cohorts
multiGamesUnfair.simulate(n_games_in_set=D.games_in_set)

# print outcomes of each cohort
print("\nFrom the gambler's perspective:")
SupportTransient.print_outcomes(multi_game_sets=multiGamesFair,
                                strategy_name='For fair games:')
SupportTransient.print_outcomes(multi_game_sets=multiGamesUnfair,
                                strategy_name='For unfair games:')

# plot histograms of rewards from a set of games
SupportTransient.draw_histograms(multi_game_sets_fair_coin=multiGamesFair,
                                 multi_game_sets_unfair_coin=multiGamesUnfair)

# print comparative outcomes
SupportTransient.print_comparative_outcomes(multi_game_sets_fair_coin=multiGamesFair,
                                            multi_game_sets_unfair_coin=multiGamesUnfair)
