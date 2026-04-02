from board import Board
from player import Player, AIPlayer
from position import Position


class Chess:
    """Gère la partie d'échecs entre deux joueurs"""

    def __init__(self):
        self.__board = Board()
        self.__players: list = []       # liste de 2 Player
        self.__currentPlayer = None     # Player qui a la main

    # ──────────────────────────────────────────
    #  Initialisation
    # ──────────────────────────────────────────

    def initPlayers(self):
        """Demande les noms des joueurs et crée les instances Player ou AIPlayer"""
        self.__players = []
        for color, color_name in [(0, "Blanc"), (1, "Noir")]:
            name = input(f"Nom du joueur {color_name} (tapez 'AI' pour l'ordinateur) : ").strip()
            if name.upper() == "AI":
                self.__players.append(AIPlayer(color))
            else:
                self.__players.append(Player(name, color))
        # Les blancs commencent
        self.__currentPlayer = self.__players[0]

    # ──────────────────────────────────────────
    #  Affichage
    # ──────────────────────────────────────────

    def displayBoard(self):
        self.__board.display()

    # ──────────────────────────────────────────
    #  Validation & mise à jour
    # ──────────────────────────────────────────

    def isValidMove(self, move: str) -> bool:
        """Analyse la chaîne 'move' et appelle piece.isValidMove(...)
        Format attendu : 'Pe2 e4'  ->  pièce P en e2, destination e4
        VERSION SIMPLIFIÉE : retourne True si le format est correct
        """
        try:
            parts = move.strip().split()
            if len(parts) != 2:
                return False

            piece_str = parts[0]     # ex: 'Pe2'
            dest_str  = parts[1]     # ex: 'e4'

            if len(piece_str) != 3 or len(dest_str) != 2:
                return False

            # Extraction
            piece_id  = piece_str[0]          # 'P'
            src_col   = piece_str[1]           # 'e'
            src_row   = int(piece_str[2])      # 2
            dest_col  = dest_str[0]            # 'e'
            dest_row  = int(dest_str[1])       # 4

            srcPos  = Position(src_col, src_row)
            destPos = Position(dest_col, dest_row)

            # Vérifie qu'une pièce existe à la source
            piece = self.__board.getPiece(srcPos)
            if piece is None:
                print("Aucune pièce à cet emplacement.")
                return False

            # Vérifie que c'est la bonne pièce et la bonne couleur
            if str(piece) != piece_id:
                print(f"La pièce en {srcPos} n'est pas un(e) {piece_id}.")
                return False

            if piece.get_color() != self.__currentPlayer.get_color():
                print("Ce n'est pas votre pièce.")
                return False

            # Délègue à la méthode de la pièce (toujours True pour l'instant)
            return piece.isValidMove(destPos, self.__board)

        except (ValueError, IndexError):
            print("Format invalide. Exemple : 'Pe2 e4'")
            return False

    def updateBoard(self, move: str):
        """Met à jour l'échiquier à partir de la chaîne 'move'"""
        parts     = move.strip().split()
        piece_str = parts[0]
        dest_str  = parts[1]

        srcPos  = Position(piece_str[1], int(piece_str[2]))
        destPos = Position(dest_str[0],  int(dest_str[1]))

        self.__board.movePiece(srcPos, destPos)

    def isCheckMate(self) -> bool:
        """VERSION SIMPLIFIÉE : retourne toujours False (à compléter séance 5)"""
        return False

    def switchPlayer(self):
        """Bascule vers l'autre joueur"""
        if self.__currentPlayer is self.__players[0]:
            self.__currentPlayer = self.__players[1]
        else:
            self.__currentPlayer = self.__players[0]

    # ──────────────────────────────────────────
    #  Boucle principale
    # ──────────────────────────────────────────

    def play(self):
        """Déroule la partie complète"""
        self.initPlayers()

        while not self.isCheckMate():
            self.displayBoard()

            move = ""
            while not self.isValidMove(move):
                move = self.__currentPlayer.askMove()

            self.updateBoard(move)
            self.switchPlayer()
