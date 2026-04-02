from position import Position
from piece import King, Queen, Bishop, Knight, Rook, Pawn, Piece


class Board:
    """Représente l'état de l'échiquier (8x8)"""

    def __init__(self):
        # Dictionnaire : clé = str(position), valeur = Piece (ou None si vide)
        # Structure : { "a1": <Rook blanc>, "b1": <Knight blanc>, ... }
        self.__pieces: dict = {}
        self.__initialize()

    def __initialize(self):
        """Place toutes les pièces à leur position initiale"""

        # ── Pièces blanches (color=0) ──
        back_row_white = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, PieceClass in enumerate(back_row_white):
            col = chr(ord('a') + i)
            pos = Position(col, 1)
            self.__pieces[str(pos)] = PieceClass(pos, 0)

        for i in range(8):
            col = chr(ord('a') + i)
            pos = Position(col, 2)
            self.__pieces[str(pos)] = Pawn(pos, 0)

        # ── Pièces noires (color=1) ──
        back_row_black = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, PieceClass in enumerate(back_row_black):
            col = chr(ord('a') + i)
            pos = Position(col, 8)
            self.__pieces[str(pos)] = PieceClass(pos, 1)

        for i in range(8):
            col = chr(ord('a') + i)
            pos = Position(col, 7)
            self.__pieces[str(pos)] = Pawn(pos, 1)

        # Cases vides (lignes 3 à 6)
        for row in range(3, 7):
            for i in range(8):
                col = chr(ord('a') + i)
                pos = Position(col, row)
                self.__pieces[str(pos)] = None

    def getPiece(self, position: Position):
        """Retourne la pièce à 'position', ou None si la case est vide"""
        return self.__pieces.get(str(position), None)

    def getPosition(self, piece: Piece):
        """Retourne la position d'une pièce, ou None si elle a été capturée"""
        for key, p in self.__pieces.items():
            if p is piece:
                return p.get_position()
        return None

    def movePiece(self, fromPos: Position, toPos: Position):
        """Déplace une pièce (sans vérification de validité)"""
        piece = self.__pieces.get(str(fromPos))
        if piece:
            piece.set_position(toPos)
            self.__pieces[str(toPos)] = piece
            self.__pieces[str(fromPos)] = None

    def display(self):
        """Affiche l'échiquier en mode texte dans le terminal"""
        print("  a  b  c  d  e  f  g  h")
        print(" +" + "──+" * 8)
        for row in range(8, 0, -1):
            line = f"{row}|"
            for i in range(8):
                col = chr(ord('a') + i)
                piece = self.__pieces.get(str(Position(col, row)))
                if piece is None:
                    # Case vide : affichage alterné pour simuler les couleurs
                    cell = "  "
                else:
                    color_prefix = "w" if piece.get_color() == 0 else "b"
                    cell = f"{color_prefix}{str(piece)}"
                line += f"{cell}|"
            print(line + f" {row}")
        print(" +" + "──+" * 8)
        print("  a  b  c  d  e  f  g  h")
