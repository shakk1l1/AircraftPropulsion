"""Regression tests for the interactive course helper, using no external packages."""

import contextlib
import io
from pathlib import Path
import runpy
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import ListOfEquation


class CommandLineTests(unittest.TestCase):
    def setUp(self):
        initial_values = {name: None for name in ListOfEquation.variables_values}
        initial_values["r"] = 287
        self.state = patch.dict(ListOfEquation.variables_values, initial_values, clear=True)
        self.state.start()
        self.addCleanup(self.state.stop)

    def run_commands(self, commands):
        output = io.StringIO()
        with patch("builtins.input", side_effect=commands) as mocked_input:
            with contextlib.redirect_stdout(output):
                runpy.run_path(str(ROOT / "main.py"), run_name="__main__")
        return output.getvalue(), [call.args[0] for call in mocked_input.call_args_list]

    def test_iteration_reuses_predefined_pressure_ratio(self):
        output, prompts = self.run_commands([
            "define", "pressureRatio", "10",
            "define", "isentropic efficiency Compressor", "0.85",
            "define", "Tt1", "288.15",
            "Tt2 Iteration", "1.4", "1004.5", "quit",
        ])
        self.assertNotIn("Pressure Ratio: ", prompts)
        self.assertIn("Final Tt2:", output)
        self.assertAlmostEqual(ListOfEquation.variables_values["gamma"], 1.4)
        self.assertGreater(ListOfEquation.variables_values["Tt2"], 288.15)

    def test_iteration_requests_missing_values_and_finishes(self):
        output, prompts = self.run_commands([
            "Tt2 Iteration", "10", "0.85", "288.15", "1.4", "1004.5", "quit",
        ])
        self.assertEqual(prompts.count("Pressure Ratio: "), 1)
        self.assertIn("Final Cp:", output)
        self.assertEqual(ListOfEquation.variables_values["pressureRatio"], 10)
        self.assertAlmostEqual(ListOfEquation.variables_values["Cp"], 1004.5)

    def test_define_uses_corrected_variable_name(self):
        _, prompts = self.run_commands([
            "define", "not_a_variable", "Tt1", "288.15", "quit",
        ])
        self.assertIn("Enter again: ", prompts)
        self.assertEqual(ListOfEquation.variables_values["Tt1"], 288.15)
        self.assertNotIn("not_a_variable", ListOfEquation.variables_values)


if __name__ == "__main__":
    unittest.main()
