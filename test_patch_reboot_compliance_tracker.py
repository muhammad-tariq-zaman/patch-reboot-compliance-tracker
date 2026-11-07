import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import track

def row(h, p, r):
    return {"host": h, "patched": p, "rebooted": r}

class TestRebootCompliance(unittest.TestCase):
    def test_compliant(self):
        self.assertEqual(track([row("H1", "yes", "yes")])[0][1], "COMPLIANT")
    def test_patched_no_reboot(self):
        self.assertEqual(track([row("H1", "yes", "no")])[0][1], "PATCHED, NO REBOOT")
    def test_not_patched(self):
        self.assertEqual(track([row("H1", "no", "no")])[0][1], "NOT PATCHED")
    def test_action_first(self):
        r = track([row("A", "yes", "yes"), row("B", "yes", "no")])
        self.assertEqual(r[0][0], "B")
