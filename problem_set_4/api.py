import requests

def main():
    print('Search the Art Institute of Chicago!')
    artist = input('Artist: ')
    try:
        response = requests.get(
            'https://api.artic.edu/api/v1/artworks/search',
            {'q': artist}
            )
        response.raise_for_status() # check if the response worked as intended. If not...
    except requests.HTTPError:
        print('I could not complete the request!')
        return # exit the program
    # convert response to a json object
    content = response.json()
    for artwork in content['data']: # there is a key called 'data'
        print(f'* {artwork['title']} ')


main()