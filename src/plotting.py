from typing import List

import matplotlib.pyplot as plt

from enums import Division
from Team import Team

# ------------------------------------------------------------------------------
def plot_division_standings(league: List[Team]) -> None:
    """
    
    """
    for division in Division:
        teams = [t for t in league if t.division == division]
        plot_points_over_season(teams)
# ------------------------------------------------------------------------------
def plot_points_over_season(teams: List[Team]) -> None:
    """
    
    """
    plt.figure()
    for team in teams:
        x = [*range(1, team.games_played() + 1)]
        y = team.points_over_season
        plt.plot(x, y, label=team.display_name)
    plt.legend()
    plt.show()
