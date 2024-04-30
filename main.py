# ANALIZOR LEXICAL - LIMBAJUL DE PROGRAMARE PASCAL
# Jilavu Alexandru

# Definire clasa Token
class Token:
    def __init__(self, tip, valoare):
        self.tip = tip
        self.valoare = valoare

    def __str__(self):
        return f"Tip: {self.tip}, Valoare: {self.valoare}"

# Definire clasa LexicalAnalyzer
class LexicalAnalyzer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.current_index = 0
        self.string_table = {}
        # Cuvintele cheie din Pascal
        self.keyword_table = {"begin", "end", "var", "integer", "for", "if", "else"}

        # Definire stari
        self.states = {
            'initial': {},
            'identificator': {'is_final': True},
            'constanta intreaga': {'is_final': True},
            'constanta flotanta': {'is_final': True},
            'cuvant cheie': {'is_final': True},
            'eroare': {'is_final': True},
            'operator de asignare': {'is_final': True},
            'doua puncte': {'is_final': True},
            'delimitator': {'is_final': True},
            'spatiu': {'is_final': True}
        }
        # Starea curentă
        self.current_state = 'initial'

        # Definire tranzitii dintr-o stare in alta
        self.transitions = {
            'initial': [
                (self.is_alpha, 'identificator'),
                (str.isdigit, 'constanta intreaga'),
                (lambda char: char == ':', 'doua puncte'),
                (lambda char: char in ';.', 'delimitator'),
                (str.isspace, 'spatiu')
            ],
            'identificator': [(self.is_alnum, 'identificator')],
            'constanta intreaga': [(str.isdigit, 'constanta intreaga')],
            'doua puncte': [(lambda char: char == '=', 'operator de asignare')],
            'operator de asignare': [],
            'delimitator': [],
            'spatiu': [(str.isspace, 'spatiu')]
        }

    @staticmethod
    def is_alpha(char):
        return char.isalpha()

    @staticmethod
    def is_alnum(char):
        return char.isalnum()

    # Adaugare string in tabela de stringuri
    def add_string_to_table(self, s):
        if s not in self.string_table:
            self.string_table[s] = len(self.string_table)
        # Returneaza stringul din tabela de stringuri
        return s

    # Definire metoda gettoken
    def gettoken(self):

        # Indexul de start al tokenului
        token_start = self.current_index

        # Cuvantul final va fi stocat in aceasta variabila
        value = ''

        # Starea finala detectata si indexul final detectat
        last_final_state = None
        last_final_index = None

        # Cat timp nu am ajuns la finalul codului sursa
        while self.current_index < len(self.source_code):
            # Caracterul curent
            char = self.source_code[self.current_index]
            self.current_index += 1
            # Tranzitiile posibile din starea curenta
            possible_transitions = self.transitions.get(self.current_state, [])

            transitioned = False
            # Verificam daca caracterul curent satisface conditia pentru o tranzitie
            for condition, next_state in possible_transitions:
                if condition(char):
                    self.current_state = next_state
                    if 'is_final' in self.states[self.current_state]:
                        last_final_state = self.current_state
                        last_final_index = self.current_index
                    value += char
                    transitioned = True
                    break

            # Daca nu s-a facut nicio tranzitie, verificam daca am ajuns intr-o stare finala
            if not transitioned:
                if last_final_state is not None:
                    # Check if the token is a keyword
                    if last_final_state == 'identificator' and value in self.keyword_table:
                        last_final_state = 'cuvant cheie'

                    self.current_index = last_final_index
                    self.current_state = 'initial'
                    # Daca am gasit un cuvant cheie, returnam un token cu ultimul tip final si valoarea gasita
                    if self.states[last_final_state].get('is_final'):
                        return Token(last_final_state, self.add_string_to_table(value[:last_final_index - token_start]))
                else:
                    return Token('eroare', f"La poziția {token_start}")

        # Se reseteaza starea curenta la starea initiala
        self.current_state = 'initial'
        # Daca am gasit un cuvant cheie, returnam un token cu ultimul tip final si valoarea gasita
        if last_final_state and self.states[last_final_state].get('is_final'):
            return Token(last_final_state, self.add_string_to_table(value))
        return None


def main():
    # Citim valoarea variabilei source dintr-un fisier .txt
    with open('cod_sursa.txt', 'r') as file:
        source = file.read()

    analyzer = LexicalAnalyzer(source)
    tokens = []

    while True:
        token = analyzer.gettoken()
        if token is None or token.tip == 'eroare':
            break
        tokens.append(token)

    for token in tokens:
        if token.tip != 'spatiu':
            with open('rezultat.txt', 'a') as file:
                file.write(f"{token}\n")
            print(token)
    with open('rezultat.txt', 'a') as file:
        file.write(f"Tabela de stringuri: {analyzer.string_table}\n\n\n")
    print(analyzer.string_table)

if __name__ == "__main__":
    main()
