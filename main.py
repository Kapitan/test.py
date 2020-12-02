from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Стася!'

@app.route('/qwe/')
def rrt():
    x = input("enter here")
    return x
if __name__ == '__main__':
    app.run()
