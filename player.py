import random


class Player:
    """Représente un joueur humain"""

    def __init__(self, name: str, color: int):
        self.__name = name
        self.__color = color  # 0 = blanc, 1 = noir

    # --- Getters ---
    def get_name(self) -> str:
        return self.__name

    def get_color(self) -> int:
        return self.__color

    def askMove(self) -> str:
        """Demande au joueur de saisir son coup.
        Format attendu : 'Pb2 b4'  (identifiant+case_origine  case_destination)
        """
        move = input(f"{self.__name} ({'Blanc' if self.__color == 0 else 'Noir'}), votre coup : ")
        return move.strip()


class AIPlayer(Player):
    """Joueur IA – génère un coup aléatoire (version minimale)"""

    def __init__(self, color: int):
        super().__init__("AI", color)

    def askMove(self) -> str:
        """Génère un coup complètement aléatoire (version simplifiée séance 3)"""
        cols = "abcdefgh"
        # Choisit deux cases au hasard pour simuler un coup
        col1 = random.choice(cols)
        row1 = random.randint(1, 8)
        col2 = random.choice(cols)
        row2 = random.randint(1, 8)

        # Choisit un type de pièce au hasard
        piece_id = random.choice(['K', 'Q', 'B', 'N', 'R', 'P'])

        move = f"{piece_id}{col1}{row1} {col2}{row2}"
        print(f"AI joue : {move}")
        return move
