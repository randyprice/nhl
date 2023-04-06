from typing import List

from sorting import sort_teams_by_rank
from Team import Team

# ------------------------------------------------------------------------------
def print_standings(teams: List[Team]) -> None:
    sort_teams_by_rank(teams)
    standings = []
    for (ii, team) in enumerate(teams):
        rank = str(ii + 1)
        abbrev = team.abbreviation.upper()
        games_played = str(team.games_played())
        wins = str(team.wins())
        losses = str(team.losses())
        ties = str(team.ties())
        points = str(team.points())
        stat_line = f"{rank}. {abbrev} {games_played} {wins}-{losses}-{ties} {points}"
        standings.append(stat_line)
    msg = "\n".join(standings)
    print(msg)
