import Classes as Cls
import InputData as D
import SupportCasioOwnerModel as SupportCasio
import SupportGamblerModel as SupportGambler

# from casino owner's perspective
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
print("\nFrom the casio owner's perspective:")
SupportCasio.print_outcomes(set_of_games=gamesFair,
                            strategy_name='For a fair coin:')
SupportCasio.print_outcomes(set_of_games=gamesUnfair,
                            strategy_name='For an unfair coin:')

# plot histograms
SupportCasio.plot_histograms(set_of_games_fair_coin=gamesFair,
                             set_of_games_unfair_coin=gamesUnfair)

# print comparative outcomes
SupportCasio.print_comparative_outcomes(set_of_games_fair_coin=gamesFair,
                                        set_of_games_unfair_coin=gamesUnfair)


# from gambler's perspective
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
SupportGambler.print_outcomes(multi_game_sets=multiGamesFair,
                              strategy_name='For fair games:')
SupportGambler.print_outcomes(multi_game_sets=multiGamesUnfair,
                              strategy_name='For unfair games:')

# plot histograms of rewards from a set of games
SupportGambler.draw_histograms(multi_game_sets_fair_coin=multiGamesFair,
                               multi_game_sets_unfair_coin=multiGamesUnfair)

# print comparative outcomes
SupportGambler.print_comparative_outcomes(multi_game_sets_fair_coin=multiGamesFair,
                                          multi_game_sets_unfair_coin=multiGamesUnfair)
