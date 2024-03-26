from transition import Transition
from finite_automata import Finite_Automata
from regular_grammar import Regular_Grammar
from token import Token
from state_transition_table import State_Transition_Table

# regular_grammar = Regular_Grammar(input_lines);
# token = Token(input_line);

# finite_automata = Finite_Automata();
# finite_automata.add_token(token);
# finite_automata.add_regular_grammar(regular_grammar);

token_1 = Token("atomic");
token_2 = Token("bomb");
token_3 = Token("boom");


finite_automata = Finite_Automata();
finite_automata.add_token(token_1);
finite_automata.add_token(token_2);
finite_automata.add_token(token_3);

print(finite_automata);

state_transition_table = State_Transition_Table(finite_automata);
print(state_transition_table);
