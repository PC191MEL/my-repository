from flask import Flask 

app = Flask (__name__)

@app.route('/')
def hello():
    return "<h1>hello world<h1>"

@app.route('/second')
def second(): 
   return "This is the second page</h2>"

@app.route('/third/subthird')
def third():
   return "This is the subpage of the third page"

@app.route('/fourth/<string:id>')
def fourth(id):
   return f'This is page id {id}'

if __name__ == '__main__':
  app.run(debug=False)


