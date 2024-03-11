class STTable:
    # constructor
    def __init__(self, states, entry_symbols, transition_functions):
        self.states = states;
        self.entry_symbols = entry_symbols;
        self.transition_functions = transition_functions;

    def __str__(self):
        return f"states: {self.states}\nentry_symbols: {self.entry_symbols}\ntransition_functions: {self.transition_functions}\n";
