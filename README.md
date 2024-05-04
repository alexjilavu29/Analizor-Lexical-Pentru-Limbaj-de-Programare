# Pascal Language Toolkit

This repository contains two Python programs designed for handling Pascal code. The first program is a lexical analyzer which reads Pascal code and identifies various tokens and errors. The second program is a formatter that indents and formats Pascal source code according to conventional programming styles.

## Contents

- `analizor_lexical.py`: Lexical analyzer for Pascal programming language.
- `indentare_pascal.py`: Source code formatter for Pascal programming language.

## Lexical Analyzer

The lexical analyzer scans a Pascal source code file (`cod_sursa.txt`), identifies tokens (such as keywords, identifiers, and literals), and outputs the results to `rezultat.txt`. It also detects and reports lexical errors and maintains a string table for all tokens identified.

### Features

- Identifies various tokens like identifiers, keywords, constants (integer and real), assignment and addition operators, delimiters, spaces, comments (including unclosed comments), and lexical errors.
- Outputs a list of tokens and a string table to `rezultat.txt`.
- Error reporting for lexical mishaps.

### Usage

Run the script with a source file named `cod_sursa.txt` in the same directory:

python lexical_analyzer.py

## Formatter

The formatter reads Pascal code from a file (`cod_sursa_2.pas`), formats it by correctly indenting the blocks, and writes the formatted code to `rezultat_2.pas`.

### Features

- Supports indentation for various Pascal constructs including program blocks, variable declarations, control structures (`if`, `else`, `for`, `while`), and more.
- Removes redundant spaces and comments.
- Ensures structured and readable code output.

### Usage

Ensure that the source file `cod_sursa_2.pas` is in the directory and run the script:

```python formatter.py```

## Requirements

- Python 3.6 or higher.
- No external libraries are required for the lexical analyzer.
- The formatter uses the `re` module for regular expressions which is included in standard Python distributions.

## Contributing

Contributions to enhance the functionalities of the lexical analyzer and formatter are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.


