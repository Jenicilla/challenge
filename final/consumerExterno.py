import requests

response = requests.get('https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios')
print(response.status_code)

user_name =  response.json()
for datos in user_name:
    myobj =  {'id': int(datos['id']),'fec_alta': datos['fec_alta'],'user_name': datos['user_name'],'codigo_zip': datos['codigo_zip'],'credit_card_num': datos['credit_card_num'],'credit_card_ccv': datos['credit_card_ccv'],'cuenta_numero': datos['cuenta_numero'],'direccion': datos['direccion'],'geo_latitud': datos['geo_latitud'],'geo_longitud': datos['geo_longitud'],'color_favorito': datos['color_favorito'],'foto_dni': datos['foto_dni'],'ip': datos['ip'],'auto': datos['auto'],'auto_modelo': datos['auto_modelo'],'auto_tipo': datos['auto_tipo'],'auto_color': datos['auto_color'],'cantidad_compras_realizadas': datos['cantidad_compras_realizadas'],'avatar': datos['avatar'],'fec_birthday': datos['fec_birthday']}
    print(myobj)
    response2 = requests.post('http://127.0.0.1:5000/tasks', json = myobj)