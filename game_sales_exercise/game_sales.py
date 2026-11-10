import csv
from pathlib import Path

def read_sales(file_path):
    sales = []    
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for sale in reader:
                sales.append(sale)
    except FileNotFoundError:
        print(f'Error: The file {file_path} does not exist')
        return None
    return sales

def get_popular_games(sales):
    popular_games = []
    for sale in sales:
        price = float(sale['Price'])
        quantity = int(sale['Quantity'])
        revenue = price * quantity
        if revenue >= 100:
            popular_games.append({
                'Game': sale['Game'],
                'Category': sale['Category'],
                'Revenue': f"{revenue:.2f}"               
                })
    return popular_games

def write_report(file_path,games):
    #fieldnames = list(games[0].keys())#only safe if the list has at least one element (one dictionary)
    
    fieldnames = ["Game", "Category", "Revenue"]
    with open(file_path,'w',newline = '', encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        for game in games:
            writer.writerow(game)

def main():
    input_file_path = Path(__file__).parent/'data'/'game_sales.csv'
    output_file_path = Path(__file__).parent/'data'/'popular_games.csv'
    
    sales = read_sales(input_file_path)
    if sales is None:
        return    
    popular_games = get_popular_games(sales)
    
    write_report(output_file_path,popular_games)
    print(f'Sales records read: {len(sales)}')
    if popular_games:
        print('\nGames earning at least $100:')
        for game in popular_games:
            print(f'{game['Game']}:${game['Revenue']}')
    else:
        print(f'\nNo games earned at least $100')
    print(f'\nReport saved to {output_file_path.name} ')    


if __name__ == '__main__':
    main()
