import re 

comment_char = "¨";
regular_grammar_re = r"<[^>]+>\s*::=\s*(?:[a-z]?<?[^>]+>?\s*\|?\s*)+ε?\s*";
token_re = r"[a-zA-Z0-9_.,?!@#$%^&*()\-+=:;\"'<>{}[\]\\/|`~]+";

def get_tokens_and_rg_from_file(input_file):
    regular_grammars = list();
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
            regular_grammars.append(line);
            continue;
        # tokens
        x = re.fullmatch(token_re, line);
        if x : 
            tokens.append(line);
            continue;
    return tokens, regular_grammars;
