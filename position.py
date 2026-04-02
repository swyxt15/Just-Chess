class Position:
    """Représente une case de l'échiquier (ex: 'e1', 'a8')"""

    def __init__(self, column: str, row: int):
        self.__column = column  # lettre de 'a' à 'h'
        self.__row = row        # chiffre de 1 à 8

    # --- Getters ---
    def get_column(self) -> str:
        return self.__column

    def get_row(self) -> int:
        return self.__row

    # --- Setters ---
    def set_column(self, column: str):
        self.__column = column

    def set_row(self, row: int):
        self.__row = row

    def __str__(self) -> str:
        return f"{self.__column}{self.__row}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Position):
            return False
        return self.__column == other.__column and self.__row == other.__row
