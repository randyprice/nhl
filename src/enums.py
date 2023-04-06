from enum import Enum, Flag

# ==============================================================================
class Conference(Enum):
    """
    
    """
    EASTERN = 0
    WESTERN = 1
    # --------------------------------------------------------------------------
    def from_string(s: str) -> "Conference":
        """
        
        """
        match s.lower():
            case "eastern": return Conference.EASTERN
            case "western": return Conference.WESTERN
            case _: raise Exception(f"cannot convert string {s} to Conference")
    # --------------------------------------------------------------------------
    def to_string(conference: "Conference") -> str:
        """
        
        """
        match conference:
            case Conference.EASTERN: return "eastern"
            case Conference.WESTERN: return "western"

# ==============================================================================
class Division(Enum):
    """
    
    """
    ATLANTIC = 0
    CENTRAL = 1
    METROPOLITAN = 2
    PACIFIC = 3
    # --------------------------------------------------------------------------
    def from_string(s: str) -> "Division":
        """
        
        """
        match s.lower():
            case "atlantic": return Division.ATLANTIC
            case "central": return Division.CENTRAL
            case "metropolitan": return Division.METROPOLITAN
            case "pacific": return Division.PACIFIC
            case _: raise Exception(f"cannot convert string {s} to Division")
    # --------------------------------------------------------------------------
    def to_string(division: "Division") -> str:
        """
        
        """
        match division:
            case Division.ATLANTIC: return "atlantic"
            case Division.CENTRAL: return "central"
            case Division.METROPOLITAN: return "metropolitan"
            case Division.PACIFIC: return "pacific"

# ==============================================================================
class Outcome(Enum):
    """
    
    """
    WIN = 0
    LOSS = 1
    TIE = 2

# ==============================================================================
class SubdivisionSchedule(Flag):
    """
    
    """
    A_HOSTS_C = True
    A_HOSTS_D = False

# ==============================================================================
class Subdivision(Enum):
    """
    
    """
    A = 0
    B = 1
    C = 2
    D = 3
