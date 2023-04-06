# ==============================================================================
class ConstPropertyAssignError(Exception):
    """Raised on attempt to assign to a constant property."""
    # --------------------------------------------------------------------------
    def __init__(self):
        """Constructor."""
        super().__init__("cannot assign to a constant property")