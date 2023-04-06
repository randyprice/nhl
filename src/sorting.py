from typing import List

from Team import Team

# ------------------------------------------------------------------------------
def sort_teams_by_rank(teams: List[Team]) -> None:
    """
    
    """
    teams.sort(key=lambda team: (-team.points(), -team.wins(),
                                 -team.goal_difference()))
