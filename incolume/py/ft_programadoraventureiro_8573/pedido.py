import requests
import json
from urllib.parse import quote

def new_token():
    url = "http://192.168.254.1:8091/oauth/token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    params = {
        "client_id": "IntegracaoBimer.js",
        "client_secret": "30ab7b08360b0850521b7f714d067ded",
        "grant_type": "password",
        "username": "EVERTONCOSTA",
        "nonce": "123456789",
        "password": "f2c0d35e8965bf9d5201769880749ff5",
    } 

    # body = quote("client_id=IntegracaoBimer.js&client_secret=2a67641e9dbcd751c913b5349effdc5d&grant_type=password&username=APIBIMER&nonce=123456789&password=f98b471b1946655749a8c18cfa14172d")

    response = requests.post(url, headers=headers, data=params)

    if response.status_code != 200:
        print(f"Erro na solicitação do Token: {response.status_code}")

    data = json.loads(response.text)
    # print(data)
    access_token = data['access_token']
    
    return access_token

def consultar_operacao_id_api(id_operacao):
    url = f"http://192.168.254.1:8091/api/operacoes/{id_operacao}"
    
    token = new_token()

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Erro na solicitação do IdOperacao API: {response.status_code}")


    data = json.loads(response.text)
    # print(json.dumps(data['ListaObjetos'][0]['Nome'], indent=4))

    if data['Erros'] == []:
        return data['ListaObjetos'][0]['Nome']
    else:
        # open_dialogo('e')
        print(data['Erros'])
        return ''

def consulta_fornecedor_api(codigoCRM):
    url = f"http://192.168.254.1:8091/api/pessoas/codigo/{codigoCRM}"
    
    token = new_token()

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Erro na solicitação do Fornecedor API: {response}")

    data = json.loads(response.text) 
    print(json.dumps(data['ListaObjetos'][0]['Identificador'], indent=4)) # Retorna o id do fornecedor
    # print(data)

    return data


# def novo_pedido_de_compra_api():
#     url = "http://192.168.254.1:8091/api/compras/pedidos/consultar/status?codigoEmpresa=04&identificadorFornecedor=00A000000P&status=A&dataInicialEmissao=2024-06-21&dataFinalEmissao=2024-06-21"    
#     token = new_token()

#     headers = {
#     'Content-Type': 'application/json',
#     'Accept': 'application/json',
#     'Authorization': f'Bearer {token}'
#     }

#     response = requests.get(url, headers=headers)

    

#     if response.status_code != 200:
#         print(f"Erro na solicitação do PedidoDeVenda API: {response}")
        

#     data = json.loads(response.text) 
#     print(json.dumps(data, indent=4))
#     # print(data)

#     return data

# novo_pedido_de_compra_api()
consulta_fornecedor_api('000012')