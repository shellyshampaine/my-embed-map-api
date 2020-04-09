from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'fuck'
    coords1 = str(request.args.get('coords1'))
    coords2 = str(request.args.get('coords2'))
    req = '<iframe width="600" height="800" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/directions?origin=' + coords1 + '&destination=' + coords2 + '&mode=walking&key=AIzaSyDwCpjPILFW4SHton4y3ThUU9KNip1xOJM" allowfullscreen></iframe>'
    return req
if __name__ == "__main__":
    app.run(debug=True)
