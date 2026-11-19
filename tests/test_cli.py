import io
import unittest
from contextlib import redirect_stdout

from soot.cli import main


class TestCLI(unittest.TestCase):
    def test_prints_coming_soon(self):
        output = io.StringIO()
        with redirect_stdout(output):
            main()

        self.assertEqual(output.getvalue(), "Coming soon!\n")


if __name__ == "__main__":
    unittest.main()
