from bottle import *


@route("/")
@route("/<page>")
def index(page="Frettir"):
    titill="Template"
    if page == "Frettir":
        return template('index.tpl',title=titill)
    elif page == "pic":
        return template('pic.tpl',title=titill)
    else:
        @error(404)
        def error404(error):
            return 'Nothing here, sorry'


@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')


@route('/img/<filename:re:.*\.jpg>')
def send_image(filename):
    # static/img directory
    return static_file(filename, root='img', mimetype='image/jpg')


run(host="localhost", port=8080, reloader=True)
