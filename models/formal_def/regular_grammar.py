import re
from transition import Transition

epsilon = "ε";
final_state_flag = "fstate"
split_rule_productions_regex = r"::=";
capture_rule_symbol_regex = r"<(.*?)>";
capt_term_bf_nonterm_re = r"^(.*?)(?=<)"; # capture_terminals_before_non_terminal_regex 

class Regular_Grammar:
    def __init__(self, rules):
        self.non_terminals = ["S"]; # states symbols
        self.terminals = [];        # terminal symbols
        self.productions = [];      # list of Transitions:(state, terminal, nstate)
        self.start_symbol = "S";    # start state

        self.capture_rules_into_productions(rules);

    def capture_rules_into_productions(self, rules):
        for rule in rules:
            # remove all whitespaces from rule string 
            rule = rule.replace(" ", "");

            # capture rule and productions
            rule, productions = rule.split(split_rule_productions_regex);
            rule = rule.strip();
            productions = productions.split("|");

            # capture rule symbol and add to states list 
            rule_symbol = re.findall(capture_rule_symbol_regex, rule);
            rule_symbol = rule_symbol[0];

            if rule_symbol not in self.non_terminals:
                self.non_terminals.append(rule_symbol);

            for production in productions:
                non_terminal = re.findall(capture_rule_symbol_regex, production);

                if non_terminal:
                    # if there is a non terminal, 
                    # capture terminal normally: "a<A> | b<B>"
                    terminal = re.findall(capt_term_bf_nonterm_re, production);
                    terminal = terminal[0];
                    non_terminal = non_terminal[0];
                else:
                    # if not, 
                    # means the production is a terminal-only : " a | ε "
                    terminal = production;
                    if terminal == epsilon:
                        non_terminal = rule_symbol;
                    else:
                        non_terminal = production + "_"+ final_state_flag +"_" + str(len(self.non_terminals));

                # update symbols lists 
                if non_terminal not in self.non_terminals:
                    self.non_terminals.append(non_terminal);
                if terminal not in self.terminals:
                    self.terminals.append(terminal);

                # add to transitions to productions
                self.productions.append(Transition(rule_symbol, terminal, non_terminal));


    def __str__(self):
        out = f"non_terminals: {self.non_terminals}\n";
        out += f"terminals: {self.terminals}\n";
        out += f"productions: ";
        for production in self.productions:
            out += production.__str__() + ",";
        return out + "\n";
