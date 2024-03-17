from scanner import read_file
from input_types import get_line_type
from controllers.input.regular_grammar import read_regular_grammar, print_symbols

from models.state_transition_table import Table
# from models.token import Token
# from state_transition_table import STTable

# test table 
TRANSITION_TABLE = [];
# test token
from models.token import Token
# test regular grammar 
from models.regular_grammar import Regular_Grammar

if __name__ == "__main__":
    with open("./input_file.txt") as f:
        fcontent = f.read();

    # test table 
    print("test table :::");
    t = Table();

    # test token
    # to = Token("atomic");
    # to.add_to_table(t);
    # print(to);
    # tok = Token("bomb");
    # tok.add_to_table(t);
    # print(tok);
    # toke = Token("project");
    # toke.add_to_table(t);
    # print(toke);

    # test regular_grammar 
    rg = Regular_Grammar("<S> ::= a<A> | b<A>|e\n<A>::=c<S>|d<S>|ε");
    rg.add_to_table(t);
    print(rg)
    print(t);
