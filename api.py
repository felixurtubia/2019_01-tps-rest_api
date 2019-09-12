from flask import Flask, render_template
import pika, os
from urllib.parse import urlparse
import json
import uuid

app = Flask(__name__)
# export FLASK_APP=api.py
# flask run

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

q11 = 'ver_informacion_basica'
q11_r = 'ver_informacion_basica_respuesta'
q12 = 'ver_informacion_detallada'
q12_r = 'ver_informacion_detallada_respuesta'
q13 = 'busqueda_parcial'
q13_r = 'busqueda_parcial_respuesta'
q14 = 'busqueda_especifica' 
q14_r = 'busqueda_especifica_respuesta'

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

def publicar_string(data, queue):
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
		body=data
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

		result = self.channel.queue_declare('', exclusive=True)
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

		result = self.channel.queue_declare('', exclusive=True)
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

class RpcClient_q11(object):
	def __init__(self):
		url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://riikuyvl:WtYUU4rdx0-UOTPE0yrObjMZt4WXuAxh@crane.rmq.cloudamqp.com/riikuyvl')
		url = urlparse(url_str)
		params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],credentials=pika.PlainCredentials(url.username, url.password))
		self.connection = pika.BlockingConnection(params)
		self.channel = self.connection.channel()

		result = self.channel.queue_declare('', exclusive=True)
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
			routing_key=q11,
			properties=pika.BasicProperties(
				reply_to=self.callback_queue,
				correlation_id=self.corr_id,
			),
			body=data
			)
		while self.response is None:
			self.connection.process_data_events()
		return self.response

class RpcClient_q12(object):
	def __init__(self):
		url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://riikuyvl:WtYUU4rdx0-UOTPE0yrObjMZt4WXuAxh@crane.rmq.cloudamqp.com/riikuyvl')
		url = urlparse(url_str)
		params = pika.ConnectionParameters(blocked_connection_timeout=20,socket_timeout=20,host=url.hostname, virtual_host=url.path[1:],credentials=pika.PlainCredentials(url.username, url.password))
		self.connection = pika.BlockingConnection(params)
		self.channel = self.connection.channel()

		result = self.channel.queue_declare('', exclusive=True)
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
			routing_key=q12,
			properties=pika.BasicProperties(
				reply_to=self.callback_queue,
				correlation_id=self.corr_id,
			),
			body=data
			)
		while self.response is None:
			self.connection.process_data_events()
		return self.response

class RpcClient_q13(object):
	def __init__(self):
		url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://riikuyvl:WtYUU4rdx0-UOTPE0yrObjMZt4WXuAxh@crane.rmq.cloudamqp.com/riikuyvl')
		url = urlparse(url_str)
		params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],credentials=pika.PlainCredentials(url.username, url.password))
		self.connection = pika.BlockingConnection(params)
		self.channel = self.connection.channel()

		result = self.channel.queue_declare('', exclusive=True)
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
			routing_key=q13,
			properties=pika.BasicProperties(
				reply_to=self.callback_queue,
				correlation_id=self.corr_id,
			),
			body=json.dumps(data)
			)
		while self.response is None:
			self.connection.process_data_events()
		return self.response


@app.route('/')
def hello_world():
	response = render_template('index.html')
	response.headers['Content-Security-Policy'] = "default-src 'self'"
	response.headers['X-XSS-Protection'] = '1; mode=block'
	return response

#Buscar un mazo de usuario (q6) -> se espera respuesta
@app.route('/user_deck/<id>')
def show_deck_info(id):
	# Parse CLODUAMQP_URL (fallback to localhost)
	data = {"id": id}
	respuesta = RpcClient_q6().call(data)
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


#Ver informacion detallada de una carta en específico, por su nombre (q12)
@app.route('/card/detail/<id>')
def view_detailed_info(id):
	#data = {"name": name}
	#publicar_string(data=id, queue=q12)
	#return "Se ha enviado mensaje de carta :D"
	respuesta = RpcClient_q12().call(id)
	return respuesta

# q11 = 'ver_informacion_basica'
# Ver información básica de una carta en específico(q11)
@app.route('/card/basic_info/<id>')
def view_basic_info(id):
	respuesta = RpcClient_q11().call(id)
	return respuesta

#q13 Búsqueda parcial de cartas, debería entregar una lista de cartas (q13)
@app.route('/card/search/<field>')
def search_card(field):
	respuesta = RpcClient_q13().call(field)
	return respuesta

if __name__ == '__main__':
	app.config.update(
	    SESSION_COOKIE_HTTPONLY=True,
		)
	app.run(host='0.0.0.0')

