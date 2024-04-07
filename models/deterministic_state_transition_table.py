class Deterministic_State_Transition_Table:
    def __init__(self, state_transition_table):
        self.state_transition_table = state_transition_table;

        self.table = [ [[0]] + self.state_transition_table.finite_automata.alphabet ];
        self.cols = len(self.table[0]);
        self.rows = 1;

 
        self.states = [[0]];
        self.accept_states = [([0], "ERROR")]; # contains tuples: (state, accept_token/grammar)
        self.error_state = 0;
        self.determinize();

        self.add_error_state();


    def add_error_state(self):
        for state_line in self.table[1:]:
            for transition in state_line[1:]:
                if len(transition) < 1: transition.append(self.error_state);


    def verify_and_add_accept_state(self, det_state):
        nondet_accept_states = self.state_transition_table.finite_automata.accept_states;
        accept_state = ([], '');

        for nondet_state in det_state:
            for nondet_accept_state in nondet_accept_states:
                if nondet_state == nondet_accept_state[0]:
                    if accept_state[1] and ("_variable_" in nondet_accept_state[1]):
                        # filtra caso onde mesmo estado final reconhece 
                        # gramática e token ao mesmo tempo
                        continue;
                    accept_state = (det_state, nondet_accept_state[1]);

        if accept_state[0] and accept_state[1]: 
            self.accept_states.append(accept_state);

    def state_index(self, state):
        for i in range(0, len(self.states), 1):
            if (state == self.states[i]):
                return i;
        return 0;


    def add_empty_state_row(self, state):
        if state in self.states: return;
        self.table.append( [state] + ((self.cols - 1) * [[]]));
        self.states.append(state);
        self.rows += 1;


    def add_transition_to_pos(self, row, col, value):
        for value_ in value: 
            if value_ not in self.table[row][col]:
                self.table[row][col] = self.table[row][col] + [value_];

    def add_state(self, transition_node):

        # non-deterministic STATE TRANSITION TABLE info:
        nondet_table = self.state_transition_table.table;
        alphabet = self.state_transition_table.finite_automata.alphabet;

        # append STATEs
        self.add_empty_state_row(transition_node);

        # transition_node looks like : [2,9] || [1] -> ALL non zero-length states
        for state in transition_node:
            state_index_ = self.state_index(transition_node);
            for col in range(1, self.cols, 1):
                # for each transition on nondet_table
                nondet_transition = nondet_table[state][col];
                if (nondet_transition != [0]):
                    self.add_transition_to_pos(state_index_, col, nondet_transition);

    def append_initial_rule(self):
        nondet_table = self.state_transition_table.table;

        self.add_empty_state_row([ nondet_table[1][0] ]);

        for col in range(1, len(nondet_table[1]), 1):
            transition = nondet_table[1][col];
            if transition != [self.error_state]:
                self.add_transition_to_pos(1, col, transition);


    def determinize(self):
        # non-deterministic STATE TRANSITION TABLE (info-utils):
        alphabet = self.state_transition_table.finite_automata.alphabet;
        states = self.state_transition_table.finite_automata.states;
        nondet_table = self.state_transition_table.table;

        ## add initial state row
        self.append_initial_rule();

        # for each transitions on det_table
        row = 1;
        while (row < self.rows):
            for col in range(1, self.cols, 1):
                transition_node = self.table[row][col];

                # checks if transition is already a state
                append_condition = (transition_node not in self.states);
                append_condition *= transition_node != [self.error_state];
                append_condition *= len(transition_node);

                if (append_condition):
                    # adds to states and add state row
                    self.add_state(transition_node);
                    self.verify_and_add_accept_state(transition_node);
            row += 1;


    def __str__(self):
        out = "";
        out += "states: " + str(self.states) + "\n";
        for row in self.table:
            out += str(row) + "\n";
        return out;
