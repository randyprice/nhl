from enums import SubdivisionSchedule

from plotting import plot_division_standings
from simulate import simulate_regular_season
from utils import init_teams, init_outcome_probability_factors

# ------------------------------------------------------------------------------
def main() -> None:
    teams = init_teams()
    schedule = SubdivisionSchedule.A_HOSTS_C
    outcome_probability_factors = init_outcome_probability_factors()
    simulate_regular_season(teams, schedule, outcome_probability_factors)
    plot_division_standings(teams)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
