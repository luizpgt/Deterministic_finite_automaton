import re 

regular_grammar_re_old = r"<[^>]+>\s*::=\s*(?:[a-z]<[^>]+>\s*\|?\s*)+ε?\s*";
regular_grammar_re = r"<[^>]+>\s*::=\s*(?:[a-z]?<?[^>]+>?\s*\|?\s*)+ε?\s*";

class Regular_Grammar:
    def __init__(self, r_grammar):
        self.r_grammar = r_grammar;
        self.rules = Regular_Grammar.read_rules_r_grammar(r_grammar);
        self.INITIAL_STATE_SYMBOL = 'S';
        self.FINAL_STATE_SYMBOL = 'ε' 

    @staticmethod
    def read_rules_r_grammar(r_grammar):
        rules = [];

        for line in r_grammar.splitlines():
            if re.fullmatch(regular_grammar_re, line):
                rules.append(Regular_Grammar.extract_transitions_r_grammar(line));
        return rules;


    @staticmethod
    def extract_transitions_r_grammar(line):
        # aux lists 
        transitions = []; 
        non_terminals = []; 
        terminals = [];

        # extract transitions from line 
        terminals = re.findall(r'(\w)(?=<)', line);
        terminals += (re.findall(r'\|\s*(\w)(?!<)', line));
        non_terminals = re.findall(r'<([A-Z])>', line);
                
        # save rule symbol (left side symbol)
        transitions.append(Regular_Grammar.Transition('', non_terminals.pop(0)));

        # save pair (terminal, non_terminal)
        for i in range(0, len(terminals), 1):
            if i < len(non_terminals):
                transitions.append(
                    Regular_Grammar.Transition(terminals[i], non_terminals[i]));
            else:
                transitions.append(Regular_Grammar.Transition(terminals[i], ''));
        return transitions;


    def add_to_table(self, table):
        def set_xor_get_state(symbol):
            # find or create state on table + return row
            nonlocal states; nonlocal table;
            for pair in states:
                symbol_, state = pair;
                if symbol_ == symbol:
                    return state;
            pair = (symbol, table.rows);
            states.append(pair);
            table.add_state_row();
            return (table.rows - 1);

        def set_xor_get_terminal(terminal):
            # find or create terminal on table + return col 
            nonlocal table;
            for i in range(0, len(table.SYMBOLS), 1):
                if table.SYMBOLS[i] == terminal:
                    return i;
            table.add_symbol_col(terminal);
            return (table.cols - 1);

        # this def will add all prods to the table

        # list of tuple pairs (non_terminal, table_state)
        states = [];

        # add the initial state for the initial rule
        pair = (self.INITIAL_STATE_SYMBOL, table.INI_ST);
        states.append(pair);

        # add all productions for each rule 
        for rule in self.rules:
            # get rule
            rule_symbol = (rule[0]).non_terminal;
            rule_state = set_xor_get_state(rule_symbol);

            # for each prod in rule
            for transition in rule[1:]:
                # check if terminal is epsilon (does not adds to terminal row)
                if transition.terminal == self.FINAL_STATE_SYMBOL:
                    table.mark_specific_final_state(rule_state);
                    continue;

                if transition.terminal and transition.non_terminal:
                    term_col = table.has_symbol_pos(transition.terminal);
                    state_row = set_xor_get_state(transition.non_terminal);
                    if not term_col:
                        # adds terminal to the table
                        term_col = table.cols;
                        table.add_symbol_col(transition.terminal);
                        node_value = state_row ;
                    else:
                        # indeterminism case 
                        node_value = [];
                        old_node_value = table.get_node_value(rule_state, term_col);
                        # if node has no transition
                        if old_node_value == 0:
                            node_value = state_row;
                        else:
                            # if it already have other transitions
                            if type(old_node_value) == int:
                                node_value.append(old_node_value);
                                node_value.append(state_row);
                            else:
                                node_value = old_node_value + [state_row];
                    table.add_transition_node(rule_state, node_value, term_col);


    def __str__(self):
        out = "";
        for rule in self.rules:
            for transition in rule:
                out += f"({transition.terminal}, {transition.non_terminal}), ";
            out += "\n";
        return out;


    class Transition:
        def __init__(self, terminal, non_terminal):
            self.terminal = terminal;
            self.non_terminal = non_terminal;

        def __str__(self):
            return f"({self.terminal},{self.non_terminal})";

