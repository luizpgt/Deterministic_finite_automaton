import re 

INITIAL_STATE_SYMBOL = 'S';
regular_grammar_re = r"<[^>]+>\s*::=\s*(?:[a-z]<[^>]+>\s*\|?\s*)+ε?\s*";


class symbol_pair:
    def __init__(self, terminal, nonterminal):
        self.terminal = terminal;
        self.nonterminal = nonterminal;

    def __str__(self):
        return f"({self.terminal},{self.nonterminal})";


def read_regular_grammar(rules):
    symbols = [];
    for rule in rules:
        x = re.split(regular_grammar_re, rule);
        symbols.append(extract_symbols(rule));
    return symbols;


def extract_symbols(rule):
    # lists
    terminals = []; nonterminals = []; symbols = [];

    # extract symbols from rule
    terminals = re.findall(r'(\w)(?=<)', rule);
    nonterminals = re.findall(r'<([A-Z])>', rule);

    # save the rule symbol (left side symbol)
    rule_symbol = nonterminals.pop(0);
    symbols.append(symbol_pair('', rule_symbol));

    # save pair (terminal, nonterminal)
    for terminal, nonterminal, in zip(terminals, nonterminals):
        symbols.append(symbol_pair(terminal, nonterminal));

    return symbols;


def print_symbols(symbols):
    for line in symbols:
        print("rule : ", end="");
        for symbolpair in line:
            print(symbolpair, end=", ");
        print()


if __name__ == "__main__":
    with open("./../../input_file.txt") as f:
        fcontent = f.read();
    
    rules = [];
    for line in fcontent.splitlines():
        if re.fullmatch(regular_grammar_re, line):
                rules.append(line);
    print("rules: ", rules);
    symbols = read_regular_grammar(rules);
    print_symbols(symbols);
