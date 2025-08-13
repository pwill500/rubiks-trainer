# algorithms

class OLL:
    # first three
    LINE = ["F", "R", "U", "R'", "U'", "F'"]
    L_SHAPE = ["f", "R", "U", "R'", "U'", "f'"]
    DOT = ["F", "R", "U", "R'", "U'", "F'", "f", "R", "U", "R'", "U'", "f'"]

    # next seven
    SUNE = ["R", "U", "R'", "U", "R", "U2", "R'"]
    ANTISUNE = ["L'", "U'", "L", "U'", "L'", "U2", "L"]
    H = ["F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"]
    PI = ["R", "U2", "R2", "U'", "R2", "U'", "R2", "U2", "R"]
    L = ["x", "R'", "U", "R", "D'", "R'", "U'", "R", "D"]   # where 'x' means rotate to face bottom
    T = ["x", "L", "U", "R'", "U'", "L'", "U", "R", "U'"]   # where 'x' means rotate to face bottom
    U = ["R2", "D", "R'", "U2", "R", "D'", "R'", "U2", "R'"]

    @classmethod    # this is done for button-making purposes; I can reference all cases at once
    def all_cases(cls):
        return {    # creates a dict with {key : value} being {name : moves}
            "Line": cls.LINE,
            "L shape": cls.L_SHAPE,
            "Dot": cls.DOT,
            "Sune": cls.SUNE,
            "Antisune": cls.ANTISUNE,
            "H": cls.H, 
            "Pi": cls.PI, 
            "L": cls.L, 
            "T": cls.T, 
            "U": cls.U
        }

class PLL:
    # corner perm
    DIAGONAL = ["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R", "F'"]
    HEADLIGHTS = ["R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'"]

    # Edge permutation cases (2-look)
    CCW = ["R", "U'", "R", "U", "R", "U", "R", "U'", "R'", "U'", "R2"]
    CW = ["R2", "U", "R", "U", "R'", "U'", "R'", "U'", "R'", "U", "R'"]
    OPPOSITE = ["M2", "U'", "M2", "U2", "M2", "U'", "M2"]
    ADJACENT = ["M'", "U'", "M2", "U'", "M2", "U'", "M'", "U2", "M2"]     # where M' goes upwards

    @classmethod
    def all_cases(cls):
        return {
            "Diagonal": cls.DIAGONAL,
            "Headlights": cls.HEADLIGHTS,
            "CCW": cls.CCW,
            "CW": cls.CW,
            "Opposite": cls.OPP,
            "Adjacent": cls.ADJ
        }
    
class TWO:
    # first layer
    FIRST = ["R'", "D", "R", "L", "D'", "L'", "R'", "D", "R"]
    CHECKER = ["F2", "R2", "F'2"]

    # yellow
    Y1 = ["L", "U", "L'", "U", "L", "U2", "L'"]
    Y2 = ["R'", "U'", "R", "U'", "R'", "U2", "R"]
    Y3 = ["R2", "U2", "R", "U2", "R2"]
    Y4 = ["R", "U2", "R2", "U'", "R2", "U'", "R2", "U2", "R"]
    Y5 = ["F", "R", "U", "R'", "U'", "F'"]
    Y6 = ["R", "U", "R'", "U'", "R'", "F", "R", "F'"]
    Y7 = ["F", "R", "U'", "R'", "U'", "R", "U", "R", "F'"]

    # last layer
    LAST = ["L'", "U", "R'", "D2", "R", "U'", "R'", "D2", "R2"]

    @classmethod    # this is done for button-making purposes; I can reference all cases at once
    def all_cases(cls):
        return {    # creates a dict with {key : value} being {name : moves}
            "First": cls.FIRST,
            "Checker": cls.CHECKER,
            "Y1": cls.Y1,
            "Y2": cls.Y2,
            "Y3": cls.Y3,
            "Y4": cls.Y4, 
            "Y5": cls.Y5, 
            "Y6": cls.Y6, 
            "Y7": cls.Y7, 
            "Last": cls.LAST
        }