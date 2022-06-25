

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False) # threaded=True mode allows concurrent requests, opening a new thread for each new request; but might block gunicorn

  
  
  
  
