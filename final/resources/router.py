from flask import request, jsonify, Blueprint
from datetime import datetime
from database import tasks


endpoints = Blueprint('routes-tasks', __name__)


@endpoints.route('/tasks', methods=['POST'])
def add_task():
    fec_alta = request.json['fec_alta']
    user_name = request.json['user_name']
    codigo_zip = request.json['codigo_zip']
    credit_card_num = request.json['credit_card_num']
    credit_card_ccv = request.json['credit_card_ccv']
    cuenta_numero = request.json['cuenta_numero']
    direccion = request.json['direccion']
    geo_latitud = request.json['geo_latitud']
    geo_longitud = request.json['geo_longitud']
    color_favorito = request.json['color_favorito']
    foto_dni = request.json['foto_dni']
    ip = request.json['ip']
    auto = request.json['auto']
    auto_modelo = request.json['auto_modelo']
    auto_tipo = request.json['auto_tipo']
    auto_color = request.json['auto_color']
    cantidad_compras_realizadas = request.json['cantidad_compras_realizadas']
    avatar = request.json['avatar']
    fec_birthday = request.json['fec_birthday']
    id = request.json['id']

    data = (fec_alta,user_name,codigo_zip,credit_card_num,credit_card_ccv,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday,id)
    task_id = tasks.insert_task(data)

    if task_id:
        task = tasks.select_task_by_id(task_id)
        return jsonify(task), 201
    return jsonify({'message': 'Internal Error'}), 400


@endpoints.route('/tasks', methods=['GET'])
def get_tasks():
    data = tasks.select_all_tasks()

    if data:
        return jsonify({'tasks': data}), 200
    elif data == False:
        return jsonify({'message': 'Internal Error'}), 400
    else:
        return jsonify({'tasks': {}}), 200


@endpoints.route('/tasks/one', methods=['GET'])
def get_tasks_id():
    id_arg = request.args.get('id')
    data = tasks.select_task_by_id(id_arg)

    if data:
        return jsonify({'tasks': data}), 200
    elif data == False:
        return jsonify({'message': 'Internal Error'}), 400
    else:
        return jsonify({'tasks': {}}), 200


#@endpoints.route('/tasks', methods=['PUT'])
#def update_task():
#    title = request.json['title']
#    completed = request.json['completed']
#    id_arg = request.args.get('id')

#    if tasks.update_task(id_arg, (title, completed)):
#        task = tasks.select_task_by_id(id_arg)
#        return jsonify(task), 200
#    return jsonify({'message': 'Internal Error'}), 400


#@endpoints.route('/tasks', methods=['DELETE'])
#def delete_task():
#    id_arg = request.args.get('id')

#    if tasks.delete_task(id_arg):
#        return jsonify({'message': 'Task Deleted'}), 200
#    return jsonify({'message': 'Internal Error'}), 400
