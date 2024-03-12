matrix = []
rows = 0;
cols = 0;

def fill_matrix(row_len):
    for i in range(0, row_len, 1):
        pass;

def zeroeslist(n):
    return [0] * n;

def printmatrix():
    print(f"{rows}x{cols}");
    for row in matrix:
        print(row);

def print_last_row():
    i = 1;
    for row in matrix:
        if i == rows:
            print(row);
            return;
        i += 1;

def print_last_col():
    i = 1;
    last_col = [];
    print("⎴");
    for row in matrix:
        print(row[-1]);
    print("⎵");

def add_row():
    global rows;
    matrix.append([rows] + zeroeslist(cols - 1));
    rows += 1;

def add_col():
    global cols;
    for row in matrix:
        row.append(0);
    matrix[0][-1] = cols;
    cols += 1;


printmatrix();
matrix.append([0]);
rows += 1;
cols += 1;

printmatrix();
matrix[0] = matrix[0] + [cols];
cols += 1;

printmatrix();
add_row();
add_row();
add_row();

printmatrix();

add_col();
add_col();
add_col();
add_col();
add_row();

matrix[rows-1][cols-1] = [1,2];
print("last element: ", matrix[-1][-1]);

printmatrix();

print("atomic");
print_last_row();
print_last_col();
