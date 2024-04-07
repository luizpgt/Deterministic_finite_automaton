from models.transition import Transition
from models.finite_automata import Finite_Automata
from models.state_transition_table import State_Transition_Table
from models.token import Token
from models.deterministic_state_transition_table import Deterministic_State_Transition_Table
from input_.scanner import get_tokens_and_rg_from_file
from output_.printer import markdown_print_table


def read_inputs(filename):
    tokens, regular_grammar = get_tokens_and_rg_from_file(filename);
    return tokens, regular_grammar;


def generate_finite_automata(filename):
    # read inputs
    tokens, regular_grammars = read_inputs(filename);

    # create FINITE AUTOMATA 
    finite_automata = Finite_Automata();

    # add tokens to FINITE AUTOMATA
    for token in tokens:
        finite_automata.add_token(Token(token));

    # add regular grammars to FINITE AUTOMATA
    finite_automata.add_regular_grammars(regular_grammars);

    return finite_automata;


def generate_state_transition_table(filename):
    # generate FINITE AUTOMATA
    finite_automata = generate_finite_automata(filename);

    # create STATE TRANSITION TABLE
    state_transition_table = State_Transition_Table(finite_automata);

    return state_transition_table;

    
def generate_deterministic_state_transition_table(filename): 
    # generate STATE TRANSITION TABLE
    state_transition_table = generate_state_transition_table(filename);

    # create DETERMINISTIC STATE TRANSITION TABLE
    deterministic_state_transition_table = Deterministic_State_Transition_Table(state_transition_table);

    return deterministic_state_transition_table;


def markdown_print(table):
    print(markdown_print_table(table));


# ε
if __name__ == "__main__":
    input_filename = "input_file.txt";

    deterministic_state_transition_table = generate_deterministic_state_transition_table(input_filename);
    markdown_print(deterministic_state_transition_table.state_transition_table);
    markdown_print(deterministic_state_transition_table);
    exit();

    state_transition_table = generate_state_transition_table(input_filename);
    markdown_print(state_transition_table);
    exit();
