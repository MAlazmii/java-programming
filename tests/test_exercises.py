"""Compile each independent exercise and exercise its public commands."""
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class CipherTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.out = pathlib.Path(cls.temp.name)
        for exercise in ['substitution-ciphers', 'caesar-cipher', 'exceptional-press', 'math-library']:
            destination = cls.out / exercise
            destination.mkdir()
            subprocess.run(['javac', '-d', str(destination), *map(str, (ROOT/'exercises'/exercise).glob('*.java'))], check=True)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def command(self, name, *args):
        return subprocess.run(['java', '-cp', str(self.out/'substitution-ciphers'), name, *args], text=True, capture_output=True)

    def test_original_caesar_rotation(self):
        result = subprocess.run(['java', '-cp', str(self.out/'caesar-cipher'), 'Caesar', '3', 'Abc XYZ!'], capture_output=True, text=True, check=True)
        self.assertEqual(result.stdout.strip(), 'Def ABC!')

    def test_math_demo(self):
        result = subprocess.run(['java', '-cp', str(self.out/'math-library'), 'MathLibraryExample'], capture_output=True, text=True, check=True)
        self.assertIn('sqrt(-4) = NaN', result.stdout)
        self.assertIn('4/0.0 = Infinity', result.stdout)

    def test_caesar_decrypt_cli(self):
        result = self.command('Caesar', 'decrypt', '3', 'Def ABC!')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), 'Abc XYZ!')

    def test_caesar_negative_and_large_shift(self):
        for shift in ['-1', '51']:
            self.assertEqual(self.command('Caesar', 'encrypt', shift, 'Abc XYZ!').stdout.strip(), 'Zab WXY!')

    def test_vigenere_repeats_short_key(self):
        self.assertEqual(self.command('Vigenere', 'encrypt', 'LEMON', 'ATTACKATDAWN').stdout.strip(), 'LXFOPVEFRNHR')
        self.assertEqual(self.command('Vigenere', 'decrypt', 'LEMON', 'LXFOPVEFRNHR').stdout.strip(), 'ATTACKATDAWN')

    def test_vigenere_invalid_key(self):
        for key in ['', '123']:
            result = self.command('Vigenere', 'encrypt', key, 'HELLO')
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('key must contain', result.stderr)

if __name__ == '__main__':
    unittest.main()
