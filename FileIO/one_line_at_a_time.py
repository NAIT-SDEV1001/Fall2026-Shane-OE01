from pathlib import Path

#read one line at a time and append to a list
def read_one_line(file_path):
    books = []
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            line = file.readline()
            while line !="":#While the line read is not empty, keep reading
                book = line.strip()
                if book:
                    books.append(book)
                line = file.readline()
        return books
#have function return a clean list of books
    except FileNotFoundError:
        return None

def main():
    file_path = Path(__file__).parent/'books.txt'
    books = read_one_line(file_path)

    for book in books:
        print(book)

if __name__ == '__main__':
    main()