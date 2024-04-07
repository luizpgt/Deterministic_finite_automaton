import re 

comment_char = "¨";
regular_grammar_re = r"<[^>]+>\s*::=\s*(?:[a-z]?<?[^>]+>?\s*\|?\s*)+ε?\s*";
token_re = r"[a-zA-Z0-9_.,?!@#$%^&*()\-+=:;\"'<>{}[\]\\/|`~]+";

def split_grammars(all_regular_grammars):
    regular_grammar = [];
    regular_grammars = [];

    for rule in all_regular_grammars:
        trimmed_rule = rule.replace(" ", "");

        if ("<S>" in trimmed_rule) :
            if len(regular_grammar): regular_grammars.append(regular_grammar);
            regular_grammar = [];

        regular_grammar.append(rule);

    regular_grammars.append(regular_grammar);

    return regular_grammars;

def get_tokens_and_rg_from_file(input_file):
    all_regular_grammars = list();
    tokens = list();

    with open(input_file) as file:
        lines = file.readlines();

    for line in lines: 
        # remove extra whitespaces + \n
        line = line.strip();
        # filter empty lines
        if not len(line): 
            continue;
        # filter comment lines
        if len(line) and (line[0] == comment_char): 
            continue;

        # rules of regular grammars
        x = re.fullmatch(regular_grammar_re, line);
        if x : 
            all_regular_grammars.append(line);
            continue;

        # tokens
        x = re.fullmatch(token_re, line);
        if x : 
            tokens.append(line);
            continue;

    regular_grammars = split_grammars(all_regular_grammars);
    return tokens, regular_grammars;
