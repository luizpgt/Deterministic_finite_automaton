from scanner import read_file
from input_types import get_line_type
from controllers.input.regular_grammar import read_regular_grammar, print_symbols

from models.state_transition_table import Table
# from models.token import Token
# from state_transition_table import STTable

# test table 

TRANSITION_TABLE = [];

if __name__ == "__main__":
    with open("./input_file.txt") as f:
        fcontent = f.read();

    rules = [];
    for line in fcontent.splitlines():
        line_type = get_line_type(line);
        if line_type == "none": 
            print("\"none\" line_types usualy means unexpected behaviour");
            exit();
        if line_type == "regular grammar":
            rules.append(line);

    print("rules: ", rules);
    symbols = read_regular_grammar(rules);
    print_symbols(symbols);


    # test table 
    print("test table");
    t = Table();
    t.add_row();
    t.add_row();
    t.add_col();
    t.add_col();

    print(t);
