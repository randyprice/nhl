import random
from typing import List

import config
from enums import Conference, Division, Subdivision
from exceptions import *
from Record import Record

# ==============================================================================
class Team:
    """
    
    """
    # --------------------------------------------------------------------------
    def __init__(self, location: str, nickname: str, abbreviation: str,
                 display_name: str, conference: Conference, division: Division,
                 subdivision: Subdivision):
        """
        
        """
        self._location = location
        self._nickname = nickname
        self._abbreviation = abbreviation
        self._display_name = display_name
        self._conference = conference
        self._division = division
        self._subdivision = subdivision
        self._rating = random.randint(config.MIN_RATING, config.MAX_RATING)
        self._home_record = Record()
        self._away_record = Record()
        self._points_over_season = []
    # --------------------------------------------------------------------------
    @property
    def abbreviation(self) -> str:
        return self._abbreviation
    @abbreviation.setter
    def abbreviation(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def away_record(self) -> Record:
        return self._away_record
    @away_record.setter
    def away_record(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def conference(self) -> Conference:
        return self._conference
    @conference.setter
    def conference(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def display_name(self) -> str:
        return self._display_name
    @display_name.setter
    def display_name(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def division(self) -> Division:
        return self._division
    @division.setter
    def division(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def home_record(self) -> Record:
        return self._home_record
    @home_record.setter
    def home_record(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def location(self) -> str:
        return self._location
    @location.setter
    def location(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def nickname(self) -> str:
        return self._nickname
    @nickname.setter
    def nickname(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def points_over_season(self) -> List[int]:
        return self._points_over_season
    @nickname.setter
    def nickname(self, val: List[int]) -> None:
        self._points_over_season = val
    # --------------------------------------------------------------------------
    @property
    def rating(self) -> int:
        return self._rating
    @rating.setter
    def rating(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def subdivision(self) -> Subdivision:
        return self._subdivision
    @subdivision.setter
    def subdivision(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    def games_played(self) -> int:
        """
        
        """
        return self.home_record.games_played() + self.away_record.games_played()
    # --------------------------------------------------------------------------
    def goal_difference(self) -> int:
        """

        """
        return (self.home_record.goal_difference()
                + self.away_record.goal_difference())
    # --------------------------------------------------------------------------
    def losses(self) -> int:
        """
        
        """
        return self.home_record.losses + self.away_record.losses
    # --------------------------------------------------------------------------
    def points(self) -> int:
        """

        """
        return self.home_record.points() + self.away_record.points()
    # --------------------------------------------------------------------------
    def ties(self) -> int:
        """
        
        """
        return self.home_record.ties + self.away_record.ties
    # --------------------------------------------------------------------------
    def wins(self) -> int:
        """
        
        """
        return self.home_record.wins + self.away_record.wins
