class Table:
    def __init__(self):
        self.matrix = [[0]];
        self.rows   = 1;
        self.cols   = 1;

    def add_row(self):
        self.matrix.append([self.rows] + zero_fill(self.cols - 1));
        self.rows += 1;

    def add_col(self): 
        for row in self.matrix:
            row.append(0);
        self.matrix[0][-1] = self.cols; # adiciona o "cabeçalho" da coluna 
        self.cols += 1;

    def __str__(self):
        out = f"({self.rows}, {self.cols}) =>";
        for row in self.matrix:
            out += '\n';
            out += str(row);
        return out;

def zero_fill(n):
    return [0] * n;
