import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from position import Position
from piece import King, Queen, Bishop, Knight, Rook, Pawn
from board import Board
from player import Player, AIPlayer


# ══════════════════════════════════════════════
#  Tests de la classe Position
# ══════════════════════════════════════════════
class TestPosition(unittest.TestCase):

    def test_str_representation(self):
        """__str__ doit retourner colonne+ligne ex: 'e1'"""
        pos = Position('e', 1)
        self.assertEqual(str(pos), 'e1')

    def test_getters(self):
        pos = Position('a', 8)
        self.assertEqual(pos.get_column(), 'a')
        self.assertEqual(pos.get_row(), 8)

    def test_equality(self):
        pos1 = Position('d', 4)
        pos2 = Position('d', 4)
        self.assertEqual(pos1, pos2)

    def test_inequality(self):
        pos1 = Position('a', 1)
        pos2 = Position('h', 8)
        self.assertNotEqual(pos1, pos2)


# ══════════════════════════════════════════════
#  Tests des pièces
# ══════════════════════════════════════════════
class TestPieces(unittest.TestCase):

    def test_king_str(self):
        k = King(Position('e', 1), 0)
        self.assertEqual(str(k), 'K')

    def test_queen_str(self):
        q = Queen(Position('d', 1), 0)
        self.assertEqual(str(q), 'Q')

    def test_bishop_str(self):
        b = Bishop(Position('c', 1), 0)
        self.assertEqual(str(b), 'B')

    def test_knight_str(self):
        n = Knight(Position('b', 1), 0)
        self.assertEqual(str(n), 'N')

    def test_rook_str(self):
        r = Rook(Position('a', 1), 0)
        self.assertEqual(str(r), 'R')

    def test_pawn_str(self):
        p = Pawn(Position('a', 2), 0)
        self.assertEqual(str(p), 'P')

    def test_piece_color_white(self):
        k = King(Position('e', 1), 0)
        self.assertEqual(k.get_color(), 0)

    def test_piece_color_black(self):
        k = King(Position('e', 8), 1)
        self.assertEqual(k.get_color(), 1)

    def test_isValidMove_returns_bool(self):
        """isValidMove doit retourner un booléen (True en version simplifiée)"""
        board = Board()
        p = Pawn(Position('e', 2), 0)
        result = p.isValidMove(Position('e', 4), board)
        self.assertIsInstance(result, bool)


# ══════════════════════════════════════════════
#  Tests du plateau
# ══════════════════════════════════════════════
class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_white_rook_a1(self):
        piece = self.board.getPiece(Position('a', 1))
        self.assertIsNotNone(piece)
        self.assertEqual(str(piece), 'R')
        self.assertEqual(piece.get_color(), 0)

    def test_black_king_e8(self):
        piece = self.board.getPiece(Position('e', 8))
        self.assertIsNotNone(piece)
        self.assertEqual(str(piece), 'K')
        self.assertEqual(piece.get_color(), 1)

    def test_empty_square(self):
        """Les cases du milieu doivent être vides au départ"""
        piece = self.board.getPiece(Position('e', 4))
        self.assertIsNone(piece)

    def test_white_pawns_row2(self):
        """Toute la ligne 2 doit contenir des pions blancs"""
        for col in "abcdefgh":
            piece = self.board.getPiece(Position(col, 2))
            self.assertIsNotNone(piece)
            self.assertEqual(str(piece), 'P')
            self.assertEqual(piece.get_color(), 0)

    def test_getPosition(self):
        """getPosition doit retourner la position de la pièce"""
        piece = self.board.getPiece(Position('e', 1))
        pos = self.board.getPosition(piece)
        self.assertEqual(str(pos), 'e1')


# ══════════════════════════════════════════════
#  Tests du joueur
# ══════════════════════════════════════════════
class TestPlayer(unittest.TestCase):

    def test_player_name(self):
        p = Player("Alice", 0)
        self.assertEqual(p.get_name(), "Alice")

    def test_player_color(self):
        p = Player("Bob", 1)
        self.assertEqual(p.get_color(), 1)

    def test_ai_player_askMove_format(self):
        """AIPlayer.askMove() doit retourner une chaîne non vide"""
        ai = AIPlayer(0)
        move = ai.askMove()
        self.assertIsInstance(move, str)
        self.assertGreater(len(move), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
