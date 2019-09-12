
import pytest
import sys
import time
import json

sys.path.append('..')
import api as api


def test_create_and_read_deck():
	print("Prueba de integracion crear y retornar")
	nombre = "Mazo de prueba de integracion " + str(round(time.time()*1000))
	nombre_retornado = ""
	api.create_user_deck(1, nombre)
	mazos = json.loads(api.show_user_decks(1))
	print(mazos)
	for mazo in mazos:
		if nombre == mazo[2]:
			nombre_retornado = mazo[2]
	assert nombre == nombre_retornado

def test_create_secondary_deck():
	print("Prueba de integracion crear y retornar un mazo secundario")
	mazo_prueba = json.loads(api.show_deck_info(1))
	n_mazos_secundarios = len(mazo_prueba["mazos_secundarios"])
	api.create_deck(1, 0, 15, 0, "main")
	time.sleep(5)
	mazo_prueba = json.loads(api.show_deck_info(1))
	n_mazos_secundarios_respuesta = len(mazo_prueba["mazos_secundarios"])


	assert n_mazos_secundarios == (n_mazos_secundarios_respuesta  - 1)

def delete_create_add_card_and_read_deck():
	assert True
