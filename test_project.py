import json
import subprocess
import sys
import unittest
from pathlib import Path
from app import solve

ROOT = Path(__file__).resolve().parent

class ProjectTests(unittest.TestCase):
    def test_sample_result(self):
        result = solve(json.loads((ROOT / 'sample.json').read_text()))
        self.assertEqual(result["candidates"], ["bat"])

    def test_cli(self):
        output = subprocess.check_output([sys.executable, str(ROOT / 'app.py'), str(ROOT / 'sample.json')])
        expected = solve(json.loads((ROOT / 'sample.json').read_text()))
        self.assertEqual(json.loads(output), json.loads(json.dumps(expected)))
