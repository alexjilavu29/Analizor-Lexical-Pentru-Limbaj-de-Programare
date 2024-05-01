# Scrieti un program pentru formatarea (scrierea indentata, frumoasa)
#     programelor Pascal, folosind gramatici atributate.
#    Programul Pascal initial si cel formatat sunt stocate in fisiere.

# Precizari:
# Programul poate indenta urmatoarele constructii:
# - inceputul unui program (begin)
# - inceputul unui bloc de instructiuni (begin)
# - sfarsitul unui bloc de instructiuni (end)
# - declararea variabilelor (var)
# - declararea tipurilor (type)
# - instructiunea de repetitie (repeat...until)
# - instructiunea de selectie (case)
# - instructiunea de conditie (if)
# - instructiunea de conditie alternativa (else)
# - instructiunea de iteratie (while...do)
# - instructiunea de iteratie (for...do)
# - instructiunea de terminare a programului (end.)

# Programul poate detecta urmatoarele functionalitati:
# - function
# - procedure
# - program

# Observatie
# La instructiunea if se poate folosi else doar in structura begin...end.

import re

def read_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_code(file_path, formatted_code):
    with open(file_path, 'w') as file:
        file.write(formatted_code)

def format_pascal_code(code):
    # Eliminarea comentariilor și a spațiilor redundante
    code = re.sub(r'{[^}]*}', '', code) # orice secventa de caractere care incepe cu { si se termina cu }
    code = re.sub(r'\s+', ' ', code).strip() # orice secventa de caractere care contine unul sau mai multe spatii

    # Reguli pentru indentare
    indent_level = 0
    formatted_code = ''

    tokens = re.split(r'(;|\bdo\b|\bthen\b|\belse\b|\bbegin\b|\btype\b|\brepeat\b|\bof\b|\bvar\b|\bend\b)',code)

    tokens = [token for token in tokens if token.strip()]


    last_token = tokens[0].strip()
    print(tokens)
    var_or_type = False
    in_case = False
    in_if = False
    in_if_else = False

    if last_token == 'var' or last_token == 'type' or last_token == 'begin' or last_token == 'repeat' or last_token == 'case':
        formatted_code += ' ' * indent_level + last_token
        indent_level += 4
        if last_token == 'var' or last_token == 'type':
            var_or_type = True
        elif last_token == 'of':
            in_case = True
        elif last_token == 'then':
            in_if = True
    else:
        formatted_code += ' ' * indent_level + last_token

    print(formatted_code)
    tokens = tokens[1:]

    for token in tokens:
        token = token.strip()
        words = token.split(" ")
        print(token)
        if (token in {'begin','var','type','repeat','program','case'} or words[0] in {'function','procedure','program'}) and var_or_type:
            indent_level -= 4
            var_or_type = False


        if token == 'begin':
            if last_token == 'else' or last_token == 'then' or last_token == 'do':
                indent_level -= 4
            formatted_code += ' ' * indent_level + token + '\n'
            indent_level += 4

        elif token in ';.':
            formatted_code += token + '\n'

        elif token == 'end':
            indent_level -= 4
            formatted_code += ' ' * indent_level + token
            if in_if_else:
                in_if_else = False

        elif token == 'var' or token == 'type':
            formatted_code += ' ' * indent_level + token + '\n'
            indent_level += 4
            var_or_type = True

        elif token == 'repeat':
            formatted_code += ' ' * indent_level + token + '\n'
            indent_level += 4

        elif words[0] == 'until':
            indent_level -= 4
            formatted_code += ' ' * indent_level + token

        elif token == 'of':
            formatted_code += ' ' + token + '\n'
            indent_level += 4
            in_case = True

        elif token == 'then':
            formatted_code += ' ' + token + '\n'
            indent_level += 4
            in_if = True

        elif token == 'else':
            if in_case:
                in_case = False
            if in_if:
                in_if = False
                formatted_code+= '\n'
                in_if_else = True
            indent_level -= 4
            formatted_code += ' ' * indent_level + token + '\n'
            indent_level += 4

        elif token == 'do':
            formatted_code += ' ' + token + '\n'
            indent_level += 4

        else:
            formatted_code += ' ' * indent_level + token

        last_token = token

    return formatted_code.strip()

# Utilizare
input_file_path = 'cod_sursa_2.pas'  # Fișierul cu codul sursă Pascal
output_file_path = 'rezultat_2.pas'  # Fișierul unde va fi scris codul formatat

code = read_code(input_file_path)
formatted_code = format_pascal_code(code)
write_code(output_file_path, formatted_code)

print("Codul a fost formatat și salvat în", output_file_path)


