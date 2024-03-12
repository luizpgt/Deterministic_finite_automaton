class Token:
    def __init__(self, word):
        self.word = word;

    def __str__(self):
        return f"token: \"{self.word}\"";

    def add_to_table(self, table):
        if len(self.word) < 1: return 

        # add first char 
        this_char_col = table.has_symbol_pos(self.word[0]);
        if not this_char_col:
            this_char_col = table.cols;
            table.add_symbol_col(self.word[0]);
        table.add_transition_node(table.INI_ST, table.rows, this_char_col);
        table.add_state_row();

        # add mean chars 
        for symbol in self.word[1:]:
            this_char_col = table.has_symbol_pos(symbol);
            if not this_char_col:
                this_char_col = table.cols;
                table.add_symbol_col(symbol);
            table.add_transition_node(table.rows - 1 , table.rows, this_char_col);
            table.add_state_row();

        # add last char
        table.mark_final_state();
