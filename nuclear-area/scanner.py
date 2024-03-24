def read_file(filename):
    with open(filename) as f:
        return f.read();

if __name__ == "__main__":
    print("This file is not meant to be run separately");
