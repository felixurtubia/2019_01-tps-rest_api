from flask import Flask
import pika, os
from urllib.parse import urlparse
import json
import uuid

app = Flask(__name__)
# export FLASK_APP=api.py
# flask run


def get_data(channel, method, properties, body):
	
	if (body is None):
		body = {}
	a = body
	channel.stop_consuming()
	return a

def publicar(data, queue):
	url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://riikuyvl:WtYUU4rdx0-UOTPE0yrObjMZt4WXuAxh@crane.rmq.cloudamqp.com/riikuyvl')
	url = urlparse(url_str)
	params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],
	    credentials=pika.PlainCredentials(url.username, url.password))
	connection = pika.BlockingConnection(params)
	channel = connection.channel()
	channel.queue_declare(queue=queue)
	channel.basic_publish(
		exchange='', 
		routing_key=queue, 
		body=json.dumps(data)
		)
	connection.close()
	return

class RpcClient_q8(object):

	def __init__(self):
		url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://riikuyvl:WtYUU4rdx0-UOTPE0yrObjMZt4WXuAxh@crane.rmq.cloudamqp.com/riikuyvl')
		url = urlparse(url_str)
		params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],credentials=pika.PlainCredentials(url.username, url.password))
		self.connection = pika.BlockingConnection(params)
		self.channel = self.connection.channel()

		result = self.channel.queue_declare(queue=q8, exclusive=False)
		self.callback_queue = result.method.queue

		self.channel.basic_consume(
			queue=self.callback_queue,
			on_message_callback=self.on_response,
			auto_ack=True)

	def on_response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

	def call(self, data):
		self.response = None
		self.corr_id = str(uuid.uuid4())
		self.channel.basic_publish(
			exchange='',
			routing_key=q8,
			properties=pika.BasicProperties(
				reply_to=self.callback_queue,
				correlation_id=self.corr_id,
			),
			body=json.dumps(data)
			)
		while self.response is None:
			self.connection.process_data_events()
		return self.response


class RpcClient_q6(object):

	def __init__(self):
		url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://riikuyvl:WtYUU4rdx0-UOTPE0yrObjMZt4WXuAxh@crane.rmq.cloudamqp.com/riikuyvl')
		url = urlparse(url_str)
		params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],credentials=pika.PlainCredentials(url.username, url.password))
		self.connection = pika.BlockingConnection(params)
		self.channel = self.connection.channel()

		result = self.channel.queue_declare(queue=q6, exclusive=False)
		self.callback_queue = result.method.queue

		self.channel.basic_consume(
			queue=self.callback_queue,
			on_message_callback=self.on_response,
			auto_ack=True)

	def on_response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

	def call(self, data):
		self.response = None
		self.corr_id = str(uuid.uuid4())
		self.channel.basic_publish(
			exchange='',
			routing_key=q6,
			properties=pika.BasicProperties(
				reply_to=self.callback_queue,
				correlation_id=self.corr_id,
			),
			body=json.dumps(data)
			)
		while self.response is None:
			self.connection.process_data_events()
		return self.response		

def publicar_recibir(data, queue_out, queue_in):
	"""
	receives data in any data type and sends a json object
	returns response from queue_in in json object
	"""
	url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://riikuyvl:WtYUU4rdx0-UOTPE0yrObjMZt4WXuAxh@crane.rmq.cloudamqp.com/riikuyvl')
	url = urlparse(url_str)
	params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],
	    credentials=pika.PlainCredentials(url.username, url.password))
	connection = pika.BlockingConnection(params)
	channel = connection.channel()
	channel.queue_declare(queue=queue_out)
	channel.basic_publish(
		exchange='', 
		routing_key=queue_out, 
		body=json.dumps(data)
		)
	channel.queue_declare(queue=queue_in)
	method, properties, body = channel.basic_get(
		queue=queue_in,
		auto_ack=False
		)
	while(method.NAME == 'Basic.GetEmpty'):
		method, properties, body = channel.basic_get(
		queue=queue_in,
		auto_ack=True
		)
	
	if(body is None):
		body = {}
	connection.close()
	return body


q1='crear_mazo'
q1_r='crear_mazo_respuesta'
q2='crear_mazo_secundario'
q2_r= 'crear_mazo_secundario_respuesta'
q3='agregar_carta_mazo_secundario'
q3_r='agregar_carta_mazo_secundario_respuesta'
q4='editar_mazo_usuario'
q4_r='editar_mazo_usuario_respuesta'
q5='remover_mazo'
q5_r='remover_mazo_respuesta'
q6='leer_mazo_usuario'
q6_r='leer_mazo_usuario_respuesta'
q7='remover_carta_mazo_secundario'
q7_r='remover_carta_mazo_secundario_respuesta'
q8 = 'listar_mazo_usuario'
q8_r = 'listar_mazo_usuario_respuesta'




@app.route('/')
def hello_world():
	return "Hello, World!"

#Buscar un mazo de usuario (q6) -> se espera respuesta
@app.route('/user_deck/<id>')
def show_deck_info(id):
	# Parse CLODUAMQP_URL (fallback to localhost)
	data = {"id": id}
	respuesta = RpcClient_q6.call(data)
	return respuesta

#Listar los mazos de un usuario (q8)
@app.route('/user_deck/list/<id_user>')
def show_user_decks(id_user):
	data = {"id_user": id_user}
	respuesta = RpcClient_q8().call(data)
	return respuesta


#Crear un mazo de usuario (q1)
@app.route('/user_deck/create/<id_user>/<name>')
def create_user_deck(id_user, name):
	data = {"iduser":id_user, "name": name}
	publicar(data=data, queue= q1)
	return "Se ha creado exitosamente"

#Ediar un mazo de usuario (q4)
@app.route('/user_deck/update/<id_userdeck>/<name>')
def update_user_deck(id_userdeck, name):
	data = {"id_userdeck": id_userdeck, "name": name}
	publicar(data=data, queue=q4)
	return "Se ha modificado exitosamente"


#Remover un mazo de usuario (q5)
@app.route('/user_deck/remove/<id_userdeck>')
def remove_user_deck(id_userdeck):
	data = {"id": id_userdeck}
	publicar(data = data, queue=q5)
	return "Mazo eliminado exitosamente"

#Crear un mazo secundario (q2)
@app.route('/deck/create/<id_userdeck>/<cardsmin>/<cardsmax>/<cardscount>/<type>')
def create_deck(id_userdeck, cardsmin, cardsmax, cardscount, type):
	data = {"idUserDeck": id_userdeck, "cardsMin": cardsmin, "cardsMax": cardsmax, "cardsCount": cardscount, "type": type}
	publicar(data=data, queue=q2)
	return " {} deck creado exitosamente".format(type)


#Agregar carta a mazo secundario (q3) 
@app.route('/deck/add_card/<id_deck>/<id_web>')
def add_card_deck(id_deck, id_web):
	data = {"idweb":id_deck, "iddeck":id_web}
	publicar(data=data, queue=q3)
	return "Carta {} agregada exitosamente".format(id_web)


#Remover carta de mazo secundario (q7)
@app.route('/deck/remove_card/<id_deck>/<id_card>')
def remove_card_deck(id_deck, id_card):
	data = {"idmazo": id_deck, "idcarta": id_card}
	publicar(data=data, queue=q7)
	return "Carta {} eliminada exitosamente del mazo {}".format(id_card, id_deck)

#if __name__ == '__main__':
#	app.run(debug=False, host='0.0.0.0')