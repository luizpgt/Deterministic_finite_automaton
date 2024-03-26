class Token:
    def __init__(self, word):
        self.word = word;
        self.len  = len(word);

    def __str__(self):
        return f"token: {self.word}";
