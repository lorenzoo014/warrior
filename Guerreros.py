import enum
# Using enum class create enumerations
class Guerreros(enum.Enum):
    MARCIANO = 1
    TERRICOLA = 2
class GuerrerosTypeError(Exception):
    """Raised when the guerreros type is wrong"""
    pass