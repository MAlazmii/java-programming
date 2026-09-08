# Java programming exercises

Coursework on linked structures, exceptions, and classical ciphers. Exercises are independent: the two `Caesar` classes must be compiled into separate output directories.

| Folder | Contents | Status |
| --- | --- | --- |
| `exercises/caesar-cipher` | Caesar rotation and frequency-based decoding | Compiles; sample rotation covered |
| `exercises/substitution-ciphers` | Caesar, Vigenère and monoalphabetic substitution | Compiles; Caesar/Vigenère regressions covered |
| `exercises/exceptional-press` | Books, vending machine and printing press | Compiles; historical behavioral limitations below |
| `exercises/math-library` | Floating-point arithmetic demonstration | Compiles and runs |
| `exercises/cabinet-and-graph` | Cabinet heuristics and graph neighborhoods | Incomplete original course scaffold |

## Run

Requires JDK 8 or newer and Python 3. From this repository:

```sh
python3 tests/test_exercises.py
mkdir -p build/substitution
javac -d build/substitution exercises/substitution-ciphers/*.java
java -cp build/substitution Caesar decrypt 3 'Def ABC!'
java -cp build/substitution Vigenere encrypt LEMON ATTACKATDAWN
```

Expected output: `Abc XYZ!` and `LXFOPVEFRNHR`.

## Corrections and limits

The substitution exercise now routes Caesar CLI decryption to `decrypt`, normalizes shifts modulo 26, and repeats Vigenère keys. Vigenère accepts nonempty ASCII letter keys (case insensitive); its default key is `A`. Existing positional key advancement is retained, including positions occupied by punctuation.

`cabinet-and-graph` requires the missing `COMP108A2Node` and `COMP108A2Output` classes. Neither is present in the available original history. It is excluded from compilation rather than supplied with guessed course contracts. Credits to Prudence Wong remain in the files.

The press exercise is preserved as a historical implementation: `print` resolves book IDs against the working directory instead of the constructor directory, and `request` does not correctly fulfill a request when it first replenishes an empty shelf. No course book fixtures were supplied. Monoalphabetic substitution also retains historical behavior (shared static mappings, limited input validation and whitespace handling); the regression suite does not certify it.

Original imported sources can be recovered from the first commit. See [provenance](PROVENANCE.md) and [file mapping](PROVENANCE.json) for source repositories, commit IDs, hashes and author references. No replacement license has been applied.
