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

```python lexical_analyzer.py```

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


# Roumanian Translation Below
--- 



# Toolkit pentru Limbajul de Programare Pascal

Acest repository conține două programe Python concepute pentru manipularea codului Pascal. Primul program este un analizor lexical care citește codul Pascal și identifică diferiți tokeni și erori. Al doilea program este un formator care indentează și formatează codul sursă Pascal conform stilurilor convenționale de programare.

## Conținut

- `lexical_analyzer.py`: Analizor lexical pentru limbajul de programare Pascal.
- `formatter.py`: Formator de cod sursă pentru limbajul de programare Pascal.

## Analizor Lexical

Analizorul lexical scanează un fișier de cod sursă Pascal (`cod_sursa.txt`), identifică tokenii (cum ar fi cuvinte cheie, identificatori și literali) și afișează rezultatele în `rezultat.txt`. De asemenea, detectează și raportează erorile lexicale și menține un tabel de șiruri pentru toți tokenii identificați.

### Caracteristici

- Identifică diferiți tokeni, cum ar fi identificatori, cuvinte cheie, constante (întregi și reale), operatori de asignare și adunare, delimitatori, spații, comentarii (inclusiv comentarii nedeschise), și erori lexicale.
- Oferă o listă de tokeni și un tabel de șiruri în `rezultat.txt`.
- Raportarea erorilor lexicale.

### Utilizare

Rulează scriptul cu un fișier sursă numit `cod_sursa.txt` în același director:

```python lexical_analyzer.py```

## Formator

Formatorul citește codul Pascal dintr-un fișier (`cod_sursa_2.pas`), îl formatează corect indendând blocurile și scrie codul formatat în `rezultat_2.pas`.

### Caracteristici

- Suportă indentarea pentru diverse construcții Pascal, inclusiv blocuri de program, declarații de variabile, structuri de control (`if`, `else`, `for`, `while`) și altele.
- Elimină spațiile și comentariile redundante.
- Asigură un output de cod structurat și lizibil.

### Utilizare

Asigură-te că fișierul sursă `cod_sursa_2.pas` se află în director și rulează scriptul:

```python formatter.py```

## Cerințe

- Python versiunea 3.6 sau mai recentă.
- Nu sunt necesare biblioteci externe pentru analizorul lexical.
- Formatorul utilizează modulul `re` pentru expresii regulate, care este inclus în distribuțiile standard Python.

## Contribuții

Contribuțiile pentru îmbunătățirea funcționalităților analizorului lexical și formatorului sunt binevenite. Te încurajez să clonezi repository-ul, să faci modificările dorite și să trimiți un pull request.

