from models.transition import Transition 

epsilon = "ε";
rg_final_state_flag = "fstate";
var_accept_state_prefix = "_variable_";

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

    def add_to_accept_states(self, state, accept_value):
        self.accept_states.append( (state, str(accept_value)) );

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
                self.add_to_accept_states(next_state, token.word);
            prev_state = next_state;

    # REGULAR GRAMMAR
    def add_regular_grammar(self, regular_grammar):
        states_dict = {"S": 1};

        # note: a production is a Transition object
        for production in regular_grammar.productions:
            # capture meaningful symbols on the production
            rg_prev_state_symbol = production.prev_state;
            rg_terminal = production.input_symbol;
            rg_next_state_symbol = production.next_state;


            # capture prev_state 
            if rg_prev_state_symbol in states_dict:
                # if key exists on states_dict
                prev_state = states_dict[rg_prev_state_symbol];
            else:
                # else: adds to states_dict
                prev_state = self.create_new_state();
                states_dict[rg_prev_state_symbol] = prev_state;

            # apply epsilon rule
            if (rg_prev_state_symbol == rg_next_state_symbol) and (rg_terminal == epsilon):
                self.add_to_accept_states(states_dict[rg_prev_state_symbol], str(var_accept_state_prefix + production.prev_state) );
                continue;

            # capture terminal
            self.add_alphabet_symbol(rg_terminal);

            # capture next_state
            if rg_next_state_symbol in states_dict:
                next_state = states_dict[rg_next_state_symbol];
            else: 
                next_state = self.create_new_state();
                states_dict[rg_next_state_symbol] = next_state;

            # apply single terminal with no non_terminal rule
            if rg_final_state_flag in rg_next_state_symbol:
                self.add_to_accept_states(states_dict[rg_next_state_symbol], str("grammar_" + production.prev_state) );

            transition = Transition(prev_state, rg_terminal, next_state);
            self.add_transition_function(transition);


    def __str__(self):
        out = f"start_state: {self.start_state}\n";
        out+= f"states: {self.states}\n";
        out+= f"alphabet: {self.alphabet}\n";
        out+= f"transition_functions: ";
        for tr in self.transition_functions: 
            out += "(" + tr.__str__() + "), ";
        out+= f"\naccept_states: {self.accept_states}\n";
        return out;
