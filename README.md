# 2019_01-tps-rest_api

API REST para conexión con servicios de mazos y de cartas.
Permite el manejo y búsqueda de Cartas Yu-GI-Oh!

Rutas:
1. Crear mazo de usuario
  https://tps-restfulapi.herokuapp.com/user_deck/create/<id_user>/<deck_name>
2. Crear mazo secundario (main Deck, side Deck y extra Deck)
  https://tps-restfulapi.herokuapp.com/deck/create/<id_userdeck>/<min cards>/<max cards>/<card Count>/<[main/side/extra]>
3. Agregar carta a mazo secundario
  https://tps-restfulapi.herokuapp.com/deck/add_card/<id_deck>/<id_web>
4. Editar mazo dew usuario
  https://tps-restfulapi.herokuapp.com/user_deck/update/<id_userdeck>/<name>
5. Remover un mazo de usuarios y sus secundarios
  https://tps-restfulapi.herokuapp.com/user_deck/remove/<id_userdeck>
6. Obtener información de un mazo 
  https://tps-restfulapi.herokuapp.com/user_deck/<id_deck>
7. Listar todos los mazos de un usuaio
  https://tps-restfulapi.herokuapp.com/user_deck/list/<id_user>
8. Buscar información detallada de carta
  https://tps-restfulapi.herokuapp.com/card/detail/<[card_name/card_id]>
9. Busqueda general de cartas
  https://tps-restfulapi.herokuapp.com/card/search/<card_name>
10. Buscar información básica de carta (nombre e imagen para display)
  https://tps-restfulapi.herokuapp.com/card/basic_info/<[card_name/card_id]>
