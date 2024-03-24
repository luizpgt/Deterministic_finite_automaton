# test table 
from models.state_transition_table import Table
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
    rg = Regular_Grammar("<S> ::= a<A> | b<A>\n<A>::=c<S>|d<S>|ε");
    rg.add_to_table(t);
    print(rg)
    print(t);
