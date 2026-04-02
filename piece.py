from abc import ABC, abstractmethod
from position import Position


class Piece(ABC):
    """Classe abstraite représentant une pièce d'échecs"""

    def __init__(self, position: Position, color: int):
        # color : 0 = blanc, 1 = noir
        self.__position = position
        self.__color = color

    # --- Getters ---
    def get_position(self) -> Position:
        return self.__position

    def get_color(self) -> int:
        return self.__color

    # --- Setters ---
    def set_position(self, position: Position):
        self.__position = position

    # --- Méthodes abstraites ---
    @abstractmethod
    def isValidMove(self, newPosition: Position, board) -> bool:
        """Retourne True si le déplacement est valide selon les règles de la pièce"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


# ──────────────────────────────────────────────
#  Les 6 types de pièces
# ──────────────────────────────────────────────

class King(Piece):
    """Roi – se déplace d'une case dans toutes les directions"""

    def isValidMove(self, newPosition: Position, board) -> bool:
        # VERSION SIMPLIFIÉE : toujours valide (à compléter séance 5)
        return True

    def __str__(self) -> str:
        return 'K'


class Queen(Piece):
    """Reine – se déplace en ligne droite ou en diagonale, distance libre"""

    def isValidMove(self, newPosition: Position, board) -> bool:
        return True

    def __str__(self) -> str:
        return 'Q'


class Bishop(Piece):
    """Fou – se déplace uniquement en diagonale, distance libre"""

    def isValidMove(self, newPosition: Position, board) -> bool:
        return True

    def __str__(self) -> str:
        return 'B'


class Knight(Piece):
    """Cavalier – se déplace en L (2+1 cases)"""

    def isValidMove(self, newPosition: Position, board) -> bool:
        return True

    def __str__(self) -> str:
        return 'N'


class Rook(Piece):
    """Tour – se déplace en ligne droite (ligne ou colonne), distance libre"""

    def isValidMove(self, newPosition: Position, board) -> bool:
        return True

    def __str__(self) -> str:
        return 'R'


class Pawn(Piece):
    """Pion – avance d'une case (ou deux au premier coup), prend en diagonale"""

    def isValidMove(self, newPosition: Position, board) -> bool:
        return True

    def __str__(self) -> str:
        return 'P'
