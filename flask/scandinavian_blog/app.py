#print(__name__)
from flask import Flask, render_template

app = Flask(__name__) #create flask app

@app.route('/') #create a route - a url
# when a certain Url is requested,
# what should be returned?
# when the url / is accesed, return hello world
def hello_world():
    return render_template('home.html')

@app.route('/sweden')
def sweden():
    # You can render a separate template for Sweden here if needed
    return render_template('sweden_template.html')

@app.route('/denmark')
def denmark():
    # You can render a separate template for Denmark here if needed
    return render_template('denmark_template.html')

@app.route('/norway')
def norway():
    # You can render a separate template for Iceland here if needed
    return render_template('norway_template.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)