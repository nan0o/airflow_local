import requests
def extract_dolar_price(url, **context):
    message = ""
    json_response = requests.get(url).json()
    for index, type in enumerate(('Oficial','Blue')):
        buyer = json_response[index]['casa']['compra'][:-1]
        seller = json_response[index]['casa']['venta'][:-1]
        print(f"{type} | {buyer} | {seller}")
        message = message + f"{type} | {buyer} | {seller}\n"
    return message