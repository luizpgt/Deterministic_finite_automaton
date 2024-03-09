from scanner import read_file
from input_types import get_line_type

if __name__ == "__main__":
    file_content = read_file("input_file.txt");
    
    for line_content in file_content.splitlines():
        line_type = get_line_type(line_content);        
        print(line_type , " : " , line_content);
