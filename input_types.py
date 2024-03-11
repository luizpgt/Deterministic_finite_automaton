import re 

regular_grammar_re = r"<[^>]+>\s*::=\s*(?:[a-z]<[^>]+>\s*\|?\s*)+ε?\s*";
token_re = r"[a-zA-Z0-9_.,?!@#$%^&*()\-+=:;\"'<>{}[\]\\/|`~]+";

def get_line_type(line):
    if not len(line): return "empty line";

    x = re.fullmatch(regular_grammar_re, line);
    if x : return "regular grammar";

    x = re.fullmatch(token_re, line);
    if x : return "token";

    return "none";

if __name__ == "__main__":
    print("This file is not meant to be run separately");
