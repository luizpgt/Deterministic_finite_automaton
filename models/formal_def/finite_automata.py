from models.transition import Transition

class Finite_Automata:
    def __init__(self):
        self.start_state = 1; # initial state
        self.states = [start_state]; # states list 
        self.alphabet = []; # input symbols list
        self.transition_functions = []; # list of transitions 
        self.accept_states = []; # final states list 

    def add_alphabet_symbol(self, input_symbol):
        self.alphabet.append(input_symbol);

    def add_transition_function(self, transition):
        self.transition_functions.append(transition);

    def add_to_accept_states(self, state):
        self.accept_states.append(state);

    def __str__(self):
        pass;

