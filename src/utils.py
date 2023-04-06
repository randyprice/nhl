import json
from typing import List

import config

from enums import Conference, Division, Subdivision
from OutcomeProbabilityFactor import OutcomeProbabilityFactor
from Team import Team

# ------------------------------------------------------------------------------
def init_outcome_probability_factors() -> List[Team]:
    """
    
    """
    home_ice_advantage = OutcomeProbabilityFactor(config.P_HOME_ICE_WIN,
                                                  config.P_HOME_ICE_LOSS,
                                                  config.HOME_ICE_WEIGHT)
    random_chance = OutcomeProbabilityFactor(config.P_RANDOM_CHANCE_WIN,
                                             config.P_RANDOM_CHANCE_LOSS,
                                             config.RANDOM_CHANGE_WEIGHT)
    return [home_ice_advantage, random_chance]
# ------------------------------------------------------------------------------
def init_teams() -> List[Team]:
    """
    
    """
    # read json
    with open(config.TEAMS_JSON_PATH, "r") as json_file:
        json_data = json.load(json_file)
    # create teams
    teams = []
    for conference_name in json_data:
        conference = Conference.from_string(conference_name)
        conference_data = json_data[conference_name]
        for division_name in conference_data:
            division = Division.from_string(division_name)
            division_data = conference_data[division_name]
            for (ii, team_display_name) in enumerate(division_data):
                if division == Division.ATLANTIC or division == Division.CENTRAL:
                    if ii < len(division_data) / 2:
                        subdivision = Subdivision.A
                    else:
                        subdivision = Subdivision.B
                else:
                    if ii < len(division_data) / 2:
                        subdivision = Subdivision.C
                    else:
                        subdivision = Subdivision.D
                team_data = division_data[team_display_name]
                nickname = team_data["nickname"]
                location = team_data.get("location", team_display_name)
                abbreviation = team_data.get("abbreviation", location[0:3])
                team = Team(location, nickname, abbreviation, team_display_name,
                            conference, division, subdivision)
                teams.append(team)
    return teams
