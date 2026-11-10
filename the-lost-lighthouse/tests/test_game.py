import unittest

from game import (
    new_game,
    move_player,
    collect_item,
    light_lighthouse,
    is_win,
    is_loss
)


class TestMysteryIsland(unittest.TestCase):

    def setUp(self):
        self.player = new_game("Ada")

    def test_new_game(self):
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
        self.assertEqual(self.player["inventory"], [])

    def test_invalid_move(self):
        original_energy = self.player["energy"]

        result = move_player(self.player, "Lighthouse")

        self.assertFalse(result)
        self.assertEqual(self.player["energy"], original_energy)

    def test_legal_move(self):
        result = move_player(self.player, "Jungle")

        self.assertTrue(result)
        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)

    def test_collect_rope(self):
        self.assertTrue(collect_item(self.player))
        self.assertIn("rope", self.player["inventory"])

    def test_cannot_collect_twice(self):
        collect_item(self.player)

        self.assertFalse(collect_item(self.player))
        self.assertEqual(self.player["inventory"].count("rope"), 1)

    def test_bridge_requires_rope(self):
        self.player["location"] = "Cave"

        result = move_player(self.player, "Old Bridge")

        self.assertFalse(result)
        self.assertEqual(self.player["location"], "Cave")

    def test_lighthouse_requires_lantern(self):
        self.player["location"] = "Lighthouse"

        self.assertFalse(light_lighthouse(self.player))
        self.assertFalse(is_win(self.player))

    def test_successful_win(self):
        self.player["location"] = "Lighthouse"
        self.player["inventory"].append("lantern")

        self.assertTrue(light_lighthouse(self.player))
        self.assertTrue(is_win(self.player))

    def test_energy_loss(self):
        self.player["energy"] = 1

        move_player(self.player, "Jungle")

        self.assertTrue(is_loss(self.player))
        self.assertEqual(self.player["energy"], 0)

    def test_replay_creates_fresh_state(self):
        self.player["inventory"].append("rope")
        self.player["energy"] = 2

        fresh_player = new_game("Ada")

        self.assertEqual(fresh_player["energy"], 5)
        self.assertEqual(fresh_player["inventory"], [])
        self.assertEqual(fresh_player["location"], "Beach")


if __name__ == "__main__":
    unittest.main()
