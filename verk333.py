from bottle import *


@route("/")
@route("/<page>")
def index(page="frettir"):
    titill="Template"
    if page == "frettir":
        return template('index.tpl',title=titill)
    elif page == "pic":
        return template('pic.tpl',title=titill)
    elif page =="reikn":
        return template('Reikn.tpl',title=titill)
    else:
        @error(404)
        def error404(error):
            return 'Nothing here, sorry'
@route('/Reikn')
def LidurA():
    return template('gaman.tpl', title = 'mah balls')
        
@route('/Reikn/<kt>')
def Reikn(kt):
    return template('ken.tpl',title = "Kennitala", kt=kt)

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

@route('/img/<filename>')
def send_image(filename):
    # static/img directory
    return static_file(filename, root='./static_file')


run(host="localhost", port=8080)
