from flask import Flask, send_from_directory
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/.well-known/apple-developer-merchantid-domain-association.txt")
def apple_merchant_id_domain_association():
    return send_from_directory("well-known", "apple-developer-merchantid-domain-association.txt")


# # Serve the file at the specified URL
# @app.route('/.well-known/apple-developer-merchantid-domain-association.txt')
# def serve_file():
#     return send_from_directory('.well-known', 'well-known/apple-developer-merchantid-domain-association.txt')
# Run the app
if __name__ == '__main__':
    app.run(host="72.193.225.119", debug=True)
