import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    
    return 'Hello World! I have been seen {} times.\n'.format(3)

if __name__ == "__main__":
    app.run(debug=True ,host='0.0.0.0', port=5001)
    
