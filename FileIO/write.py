from pathlib import Path

def write_book(file_path, book):
        #exists is optional. 
        if file_path.exists():    
            with open(file_path,'a',encoding='utf-8') as file:
                file.write(f"{book}\n")
        #if the file does not exist it will be created

def main():
    file_path = Path(__file__).parent/'books.txt'
    write_book(file_path,"The Hobbit")

if __name__== '__main__':
    main()