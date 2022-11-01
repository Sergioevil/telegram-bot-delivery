import requests

def get_item_text(articul:str):
    # use sima-land api 
    r = requests.get(f"https://www.sima-land.ru/api/v3/item/?sid={articul}&expand=cart_item")
    content = r.json()
    if len(content['items']) == 0:
        return False

    return {'text': f"[{content['items'][0]['name']}]({content['items'][0]['photoUrl']})\nЦена: {content['items'][0]['price']}₽",
    'price' : int(content['items'][0]['price'])
    }
    
def check_address(address):
    # use openstreetmap api
    r = requests.get(f"https://openstreetmap.ru/api/search?q={address}")
    content = r.json()
    to_out = []
    for i in content.get('matches', ''):
        adrr = i.get('display_name').split(', ')[-3:]
        to_out.append(', '.join(adrr).replace('город', 'г.'))
    return to_out
    

