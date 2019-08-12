from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  return jsonify({
    "message": "test!!2"
  })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
