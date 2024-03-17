class Table:
    def __init__(self):
        self.matrix = [[0], [1]];
        self.rows   = 2;
        self.cols   = 1;
        self.INI_ST = 1; # initial state (q0) will ever be 1st row
        self.END_ST = []; # final states will be on that list 
        self.SYMBOLS= []; # all entry symbols are here

    def add_state_row(self):
        self.matrix.append([self.rows] + zero_fill(self.cols - 1));
        self.rows += 1;

    def add_symbol_col(self, symbol): 
        for row in self.matrix:
            row.append(0);
        self.matrix[0][-1] = symbol; # adiciona o "cabeçalho" da coluna 
        self.SYMBOLS.append([symbol, self.cols]);
        self.cols += 1;

    def add_transition_node(self, state_p, state_n, col):
        self.matrix[state_p][col] = state_n;

    def mark_final_state(self):
        self.END_ST.append(self.rows - 1);
    def mark_specific_final_state(self, state):
        self.END_ST.append(state);

    def has_symbol_pos(self, symbol):
        for i in range(0, len(self.SYMBOLS)):
            if self.SYMBOLS[i][0] == symbol:
                return self.SYMBOLS[i][1];
        return 0;

    def __str__(self):
        out = f"({self.rows}, {self.cols}) =>";
        for row in self.matrix:
            out += '\n';
            if (row[0] == self.INI_ST) and (row[0] in self.END_ST):
                out += "->*" + str(row);
            elif row[0] in self.END_ST:
                out += " * " + str(row);
            elif row[0] == self.INI_ST:
                out += "-> " + str(row);
            else:
                out += "   " + str(row);
        out += f"\nfinal states: {self.END_ST}";
        out += f"\nentry symbols: ";
        for pair in self.SYMBOLS:
            out += pair[0] + ", ";
        out += "\n";
        return out;


def zero_fill(n):
    return [0] * n;
