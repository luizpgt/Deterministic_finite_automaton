
from transition import Transition
from finite_automata import Finite_Automata
from state_transition_table import State_Transition_Table
from token import Token
from regular_grammar import Regular_Grammar

# ε

# create FINITE AUTOMATA 
finite_automata = Finite_Automata();

# add tokens to FINITE AUTOMATA
token_1 = Token("se");
token_2 = Token("entao");
token_3 = Token("senao");
# print(token_1);
# print(token_2);
# print(token_3);

finite_automata.add_token(token_1);
finite_automata.add_token(token_2);
finite_automata.add_token(token_3);

# add regular grammar to FINITE AUTOMATA
input_lines = list();
input_lines.append("<S> ::= a<A> | e<A> | i<A> | o<A> | u<A>");
input_lines.append("<A> ::= a<A> | e<A> | i<A> | o<A> | u<A> | ε");

regular_grammar = Regular_Grammar(input_lines);
# print(regular_grammar);
finite_automata.add_regular_grammar(regular_grammar);

# create STATE TRANSITION TABLE
state_transition_table = State_Transition_Table(finite_automata);
print(state_transition_table);
