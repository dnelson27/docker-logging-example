from flask import Flask
import markupsafe
import server

app = Flask(__name__)
@app.route("/howto")
def howto():
    return {
        "statusCode": 200,
        "result": "Use the /put or /get API to put or get data!"
    }

@app.route("/put/<string:data_id>/<string:data>")
def api_put(data_id, data):
    data_id = markupsafe.escape(data_id)
    data = markupsafe.escape(data)
    return {
        "statusCode": 200,
        "result": server.put_data(data_id, data)
    }

@app.route("/get/<string:data_id>")
def api_get(data_id):
    data_id = markupsafe.escape(data_id)
    return {
        "statusCode": 200,
        "result": server.get_data(data_id)
    }
