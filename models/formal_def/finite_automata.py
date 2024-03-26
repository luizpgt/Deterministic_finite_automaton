from transition import Transition 

class Finite_Automata:
    def __init__(self):
        self.start_state = 1;             # initial state
        self.states = [self.start_state]; # states list 
        self.alphabet = [];               # input symbols list
        self.transition_functions = [];   # list of transitions 
        self.accept_states = [];          # final states list 

    def add_alphabet_symbol(self, input_symbol):
        if input_symbol not in self.alphabet:
            self.alphabet.append(input_symbol);
    
    def create_new_state(self):
        new_state = self.states[-1] + 1;
        self.states.append(new_state);
        return new_state;

    def add_transition_function(self, transition):
        self.transition_functions.append(transition);

    def add_to_accept_states(self, state):
        self.accept_states.append(state);

    # TOKEN
    def add_token(self, token):
        for i in range(0, token.len, 1):
            input_symbol = token.word[i];
            if i == 0:
                prev_state = self.start_state;
            self.add_alphabet_symbol(input_symbol);
            next_state = self.create_new_state();
            transition = Transition(prev_state, input_symbol, next_state);
            self.add_transition_function(transition);
            if i == token.len - 1:
                self.add_to_accept_states(next_state);
            prev_state = next_state;

    # REGULAR GRAMMAR
    def add_regular_grammar(self, regular_grammar):
        pass;


    def __str__(self):
        out = f"start_state: {self.start_state}\n";
        out+= f"states: {self.states}\n";
        out+= f"alphabet: {self.alphabet}\n";
        out+= f"transition_functions: ";
        for tr in self.transition_functions: 
            out += "(" + tr.__str__() + "), ";
        out+= f"\naccept_states: {self.accept_states}\n";
        return out;
