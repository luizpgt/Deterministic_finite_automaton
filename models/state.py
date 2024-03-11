INITIAL_STATE_SYMBOL = 'S';

class State:
    def __init__(self, state, initial, final):
        self.state = state;
        self.state_id = state_id;
        self.initial = initial;
        self.final = final;
    def __str__(self):
        return f"state: {self.state}\ninitial: {self.initial}\nfinal: {self.final}";
