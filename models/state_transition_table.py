class State_Transition_Table:
    def __init__(self, finite_automata):
        self.table = [[0]]; # multidimensional list
        self.finite_automata = finite_automata;
        self.error_state = 0;

        self.represent_finite_automata();
        self.add_error_state();
    
    
    def add_error_state(self):
        for state_line in self.table[1:]:
            for transition in state_line[1:]:
                if len(transition) < 1: transition.append(self.error_state);


    def represent_finite_automata(self):
        # add terminals 
        self.table[0].extend(self.finite_automata.alphabet);

        # add state rows
        cols_ = len(self.table[0]);
        for state in self.finite_automata.states:
            self.table.append([state] + ((cols_-1)* [[]]));

        # add transitions 
        self.add_transitions_to_table();


    def add_transitions_to_table(self):
        for transition in self.finite_automata.transition_functions:
            col_ = self.get_symbol_position(transition.input_symbol);
            row_ = transition.prev_state;
            val_ = self.table[row_][col_] + [transition.next_state];
            self.table[row_][col_] = val_;


    def get_symbol_position(self, symbol):
        symbols_list = self.table[0];
        for i in range(1, len(symbols_list), 1):
            if symbols_list[i] == symbol:
                return i;
        return 0;
            
    def __str__(self):
        out = "";
        accept_states = [];
        for state in self.finite_automata.accept_states:
            accept_states.append(state[0]);
        for row in self.table:
            if row[0] == self.finite_automata.start_state: out += "->";
            elif row[0] in accept_states: out += "* ";
            else : out += "  ";
            out += str(row) + "\n";
        return out;
