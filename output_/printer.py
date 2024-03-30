from models.state_transition_table import State_Transition_Table
from models.deterministic_state_transition_table import Deterministic_State_Transition_Table

def markdown_print_table(table):
    out = "";

    if isinstance(table, Deterministic_State_Transition_Table):
        rows_ = table.rows;
        cols_ = table.cols;
        accept_states = table.accept_states;

    if isinstance(table, State_Transition_Table):
        rows_ = len(table.finite_automata.states) + 1;
        cols_ = len(table.table[0]);
        accept_states = table.finite_automata.accept_states;

    table = table.table;

    for row in range(0, rows_, 1):
        out += " | ";
        # append col to accept_states
        for accept_state in accept_states:
            if table[row][0] == accept_state[0]:
                out += accept_state[1];
        out += " | ";
        for col in range(0, cols_, 1):
            out += str(table[row][col])  + " |";
        out += "\n";
        if row == 0:
            for col in range(0, cols_ + 1, 1): # cols_ + (1)accept_state col
                out += "|-";
            out += "|\n";

    return out;
