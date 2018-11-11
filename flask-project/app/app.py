from flask import Flask
import flask_cors

app=Flask(__name__)
flask_cors.CORS(app, supports_credentials=True)
app.config.from_object('app.conf')