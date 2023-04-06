from exceptions import ConstPropertyAssignError

# ------------------------------------------------------------------------------
class OutcomeProbabilityFactor:
    def __init__(self, win: float, loss: float, weight: float):
        """
        
        """
        self._win = win
        self._loss = loss
        self._weight = weight
    # --------------------------------------------------------------------------
    @property
    def loss(self) -> float:
        return self._loss
    @loss.setter
    def loss(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def weight(self) -> float:
        return self._weight
    @weight.setter
    def weight(self, _) -> None:
        raise ConstPropertyAssignError
    # --------------------------------------------------------------------------
    @property
    def win(self) -> float:
        return self._win
    @win.setter
    def win(self, _) -> None:
        raise ConstPropertyAssignError
