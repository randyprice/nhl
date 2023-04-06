import config
import random
from typing import List

from enums import Outcome, Subdivision, SubdivisionSchedule
from OutcomeProbabilityFactor import OutcomeProbabilityFactor
from Team import Team

# ------------------------------------------------------------------------------
def calculate_rating_difference_factor(home_rating: int, away_rating: int) -> OutcomeProbabilityFactor:
    """
    
    """
    adjustment = (home_rating - away_rating) * config.RATING_DIFF_SCALE_FACTOR
    return OutcomeProbabilityFactor(config.P_RATING_DIFF_WIN + adjustment,
                                    config.P_RATING_DIFF_LOSS - adjustment,
                                    config.RATING_DIFF_WEIGHT)
# ------------------------------------------------------------------------------
def determine_game_outcome(factors: List[OutcomeProbabilityFactor]) -> Outcome:
    """
    
    """
    p_win = sum(f.weight * f.win for f in factors)
    p_loss = sum(f.weight * f.loss for f in factors)
    roll = random.random()
    if roll < p_win:
        return Outcome.WIN
    elif roll < p_win + p_loss:
        return Outcome.LOSS
    else:
        return Outcome.TIE
# ------------------------------------------------------------------------------
def determine_goals_scored(outcome: Outcome) -> tuple[int, int]:
    """
    
    """
    match outcome:
        case Outcome.WIN:
            home_goals = random.randint(1, config.MAX_GOALS)
            away_goals = random.randint(0, home_goals - 1)
        case Outcome.LOSS:
            away_goals = random.randint(1, config.MAX_GOALS)
            home_goals = random.randint(0, away_goals - 1)
        case Outcome.TIE:
            home_goals = random.randint(0, config.MAX_GOALS)
            away_goals = home_goals
    return (home_goals, away_goals)
# ------------------------------------------------------------------------------
def determine_number_of_games(team: Team, opponent: Team,
                              schedule: SubdivisionSchedule) -> int:
    """
    
    """
    if team.division == opponent.division:
        return config.HOME_DIVISIONAL_GAMES
    elif team.conference == opponent.conference:
        match (schedule, team.subdivision, opponent.subdivision):
            case (SubdivisionSchedule.A_HOSTS_C, Subdivision.A, Subdivision.C) \
               | (SubdivisionSchedule.A_HOSTS_C, Subdivision.B, Subdivision.D) \
               | (SubdivisionSchedule.A_HOSTS_D, Subdivision.A, Subdivision.D) \
               | (SubdivisionSchedule.A_HOSTS_D, Subdivision.B, Subdivision.C):
                  return config.HOME_INTRACONF_SUBDIV_GAMES
            case _:
                return config.HOME_INTRACONF_GAMES
    else:
        return config.HOME_INTERCONF_GAMES
# ------------------------------------------------------------------------------
def simulate_regular_season(teams: List[Team], schedule: SubdivisionSchedule,
                            outcome_probability_factors: List[OutcomeProbabilityFactor]) -> None:
    """
    
    """
    for team in teams:
        for opponent in teams:
            if team is not opponent:
                simulate_regular_season_games(team, opponent, schedule,
                                              outcome_probability_factors)
            
# ------------------------------------------------------------------------------
def simulate_regular_season_games(team: Team, opponent: Team,
                                  schedule: SubdivisionSchedule,
                                  outcome_probability_factors: List[OutcomeProbabilityFactor]) -> None:
    """Simulate regular season games between two teams.
    
    """
    n_games = determine_number_of_games(team, opponent, schedule)
    for _ in range(0, n_games):
        simulate_regular_season_game(team, opponent,
                                     outcome_probability_factors)
# ------------------------------------------------------------------------------
def simulate_regular_season_game(home_team: Team, away_team: Team,
                                 outcome_probability_factors: List[OutcomeProbabilityFactor]) -> None:
    """
    
    """
    home_rating = home_team.rating
    away_rating = away_team.rating
    rating_difference_factor = calculate_rating_difference_factor(home_rating,
                                                                  away_rating)
    factors = outcome_probability_factors + [rating_difference_factor]
    outcome = determine_game_outcome(factors)
    (home_goals, away_goals) = determine_goals_scored(outcome)
    match outcome:
        case Outcome.WIN:
            home_team.home_record.wins += 1
            away_team.away_record.losses += 1
        case Outcome.LOSS:
            home_team.home_record.losses += 1
            away_team.away_record.wins += 1
        case Outcome.TIE:
            home_team.home_record.ties += 1
            away_team.away_record.ties += 1
    home_team.home_record.goals_for += home_goals
    home_team.home_record.goals_against += away_goals
    away_team.away_record.goals_for += away_goals
    away_team.away_record.goals_against += home_goals
    home_team.points_over_season.append(home_team.points())
    away_team.points_over_season.append(away_team.points())
