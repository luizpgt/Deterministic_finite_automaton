class Transition:
    def __init__(self, prev_state, input_symbol, next_state):
        self.prev_state = prev_state;
        self.input_symbol = input_symbol;
        self.next_state = next_state;

    def __str__(self):
        return f"{self.prev_state} × {self.input_symbol} → {self.next_state}";
