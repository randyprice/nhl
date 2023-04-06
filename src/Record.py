import config

# ==============================================================================
class Record:
    def __init__(self):
        """
        
        """
        self._wins            = 0
        self._losses          = 0
        self._ties            = 0
        self._goals_for       = 0
        self._goals_against   = 0
    # --------------------------------------------------------------------------
    @property
    def goals_against(self) -> int:
        return self._goals_against
    @goals_against.setter
    def goals_against(self, val: int) -> None:
        self._goals_against = val
    # --------------------------------------------------------------------------
    @property
    def goals_for(self) -> int:
        return self._goals_for
    @goals_for.setter
    def goals_for(self, val: int) -> None:
        self._goals_for = val
    # --------------------------------------------------------------------------
    @property
    def losses(self) -> int:
        return self._losses
    @losses.setter
    def losses(self, val: int) -> None:
        self._losses = val
    # --------------------------------------------------------------------------
    @property
    def ties(self) -> int:
        return self._ties
    @ties.setter
    def ties(self, val: int) -> None:
        self._ties = val
    # --------------------------------------------------------------------------
    @property
    def wins(self) -> int:
        return self._wins
    @wins.setter
    def wins(self, val: int) -> None:
        self._wins = val
    # --------------------------------------------------------------------------
    def games_played(self) -> int:
        """
        
        """
        return self.wins + self.losses + self.ties
    # --------------------------------------------------------------------------
    def goal_difference(self) -> int:
        """
        
        """
        return self.goals_for - self.goals_against
    # --------------------------------------------------------------------------
    def points(self) -> int:
        """
        
        """
        return (self.wins * config.POINTS_PER_WIN
                + self.ties * config.POINTS_PER_TIE)
