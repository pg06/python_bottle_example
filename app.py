# encoding: utf-8
from bottle import route, run, template, static_file, error, request


# coloque seu ip local para acessar de outros navegadores (inclusive celulares)
# ou deixe 'localhost' para teste só nessa maquina
my_host = 'localhost'
my_port = 5000


@route('/static/<static_type>/<filename>')
def server_static(static_type, filename):
    """

        Descrição: Configurar arquivos estaticos do App
    """
    return static_file(filename, root='./static/' + static_type + '/')


@error(404)
def error404(error):
    """
    
        Descrição: Configurar Pagina de ERROR 404
    """
    return 'ERROR 404 - Endereço não encontrado'


@route('/')
def index():
    """

        Descrição: Pagina principal
    """
    my_routes = ['', 'test']
    for i, my_route in enumerate(my_routes):
        href = "http://" + my_host + ":" + str(my_port) + "/" + my_route
        my_routes[i] = href

    return template('template/index.html',
        my_routes=my_routes)



@route('/test')
def test():
    """

        Descrição: Pagina teste
    """
    if not request.cookies.get('last_url'):
        request.cookies['last_url'] = request.url
    request.cookies['url'] = request.url
    charts = {}
    charts['info'] = [{
        "name": 'Tokyo',
        'data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
    }, {
        'name': 'New York',
        'data': [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
    }, {
        'name': 'Berlin',
        'data': [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
    }, {
        'name': 'London',
        'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
    }]
    charts['categories'] = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
        'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dec']
    return template('template/test.html',
        back_link= request.cookies.get('last_url'),
        charts= charts)


# rodar o aplicativo
run(host=my_host, port=my_port)
