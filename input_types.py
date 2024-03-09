import re 

regular_grammar_re = r"<[^>]+>\s*::=\s*(?:[a-z]<[^>]+>\s*\|?\s*)+ε?\s*";
token_re = r"[a-zA-Z0-9_.,?!@#$%^&*()\-+=:;\"'<>{}[\]\\/|`~]+";

def get_line_type(line):
    if not len(line): return "empty line";

    x = re.search(regular_grammar_re, line);
    if x : return "regular grammar";

    x = re.search(token_re, line);
    if x : return "token";

    return "none";
