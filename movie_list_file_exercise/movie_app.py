from pathlib import Path

def read_movies(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            entries = file.readlines()
        return [entry.strip() for entry in entries if entry.strip()]
    except FileNotFoundError:        
        return None

def write_movie(file_path, entry):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'{entry}\n')
    

def main():
    file_path = Path(__file__).parent / 'movies.txt'
    
    while True:
        print('\nMovie Menu')
        print('R - Read movies')
        print('W - Add a movie')
        print('Q - Quit')
        choice = input('Choose an option: ').strip().lower() 

        if choice == 'r':
            movies = read_movies(file_path)
            if movies is None:
                print('The movie file does not exist.')
                continue
            if not movies:
                print('The movie list empty')
            else:
                print('\nMovie List:')
                for movie in movies:
                    print(movie)
        elif choice == 'w':
            title = input('Enter a movie title: ').strip()
            if not title:
                print('Please enter a movie title')
            else:
                write_movie(file_path, title)
                print('Movie saved!') 
        elif choice == 'q':
            print('GoodBye!')
            break
        else:
            print('Please choose R,W or Q')

if __name__ == '__main__':
    main()