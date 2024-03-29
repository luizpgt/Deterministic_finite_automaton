from models.transition import Transition
from models.finite_automata import Finite_Automata
from models.state_transition_table import State_Transition_Table
from models.token import Token
from models.regular_grammar import Regular_Grammar
#from models.deterministic_state_transition_table import Deterministic_State_Transition_Table
from input_.scanner import get_tokens_and_rg_from_file

# ε

input_filename = "input_file.txt";

# read inputs
tokens, regular_grammar = get_tokens_and_rg_from_file(input_filename);

# create FINITE AUTOMATA 
finite_automata = Finite_Automata();

# add tokens to FINITE AUTOMATA
for token in tokens:
    finite_automata.add_token(Token(token));

# add regular grammar to FINITE AUTOMATA
finite_automata.add_regular_grammar(Regular_Grammar(regular_grammar));

# create STATE TRANSITION TABLE
state_transition_table = State_Transition_Table(finite_automata);
print(state_transition_table);

print("accept_states: ", end="");
print(finite_automata.accept_states);
exit();

# create DETERMINISTIC STATE TRANSITION TABLE
# deterministic_state_transition_table = Deterministic_State_Transition_Table(state_transition_table);
# print(deterministic_state_transition_table);
