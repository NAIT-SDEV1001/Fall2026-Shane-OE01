import csv #to use dictreader/dictwriter
from pathlib import Path
from pprint import pprint

def read_artists(file_path):
    all_artists = []
    try:
        with open(file_path,'r',encoding ='utf-8') as file:
            reader = csv.DictReader(file)
            for artist in reader:#for each row on the file
                all_artists.append(artist)
    except FileNotFoundError:
        print(f'Error! the file {file_path} does not exist')
    return all_artists

#return all the artists in a list who have a monthly_listeners > value
def filter_by_minimum_listeners(file_path, minimum):
    artists = read_artists(file_path)    
    return [artist for artist in artists if int(artist['monthly_listeners']) > minimum]

def write_artists_to_file(file_path,artists):
    #list of what will be the fields for the header row on the file
    #fieldnames = ['band_name','biggest_hit'.........]
    # look at the first element in the artists list to get the keys and turn them into a list for the fieldnames on the file
    fieldnames = list(artists[0].keys())
    #newline = '' means only the dictwriter should perform a new line operation after each entry, not open() as well (resulting in extra spaces)
    with open(file_path,'w',newline = '',encoding ='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        for artist in artists:
            writer.writerow(artist)

#read the file
#add a new key/value pair called listeners_per_member
#write the new list (with the new field) to a new file

def add_listeners_per_member(file_path):
    artists = read_artists(file_path)
    for artist in artists:
        listeners = int(artist['monthly_listeners'])
        members = int(artist['members'])
        #add a new key/value pair to each dictionary in the list
        artist['listeners_per_member'] = round(listeners/members)
    return artists
    

def main():
    file_path = Path(__file__).parent/'data'/'music_artists.csv'    
    popular_artists = filter_by_minimum_listeners(file_path,15900000)
    
    file_path_write = Path(__file__).parent/'data'/'popular_music_artists.csv'    
    write_artists_to_file(file_path_write,popular_artists)

    file_path_new_key = Path(__file__).parent/'data'/'popular_music_artists_with_listeners_per_member.csv'    
    listeners_per_members = add_listeners_per_member(file_path)
    pprint(listeners_per_members)

    write_artists_to_file(file_path_new_key,listeners_per_members)

if __name__ == '__main__':
    main()