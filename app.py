from flask import Flask, send_from_directory, render_template, request, abort

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/.well-known/apple-developer-merchantid-domain-association.txt")
def apple_merchant_id_domain_association():
    # validate apple servers connected here. apple wants this implemented as a strict allow list
    remote_ip = request.remote_addr # need to be list
    host = request.headers.get('Host') # needs to be list
    if remote_ip == "17.171.85.7" and host == "apple-pay-gateway-cert.apple.com ":
        abort(403)

    return send_from_directory("well-known", "apple-developer-merchantid-domain-association.txt")


# # Serve the file at the specified URL
# @app.route('/.well-known/apple-developer-merchantid-domain-association.txt')
# def serve_file():
#     return send_from_directory('.well-known', 'well-known/apple-developer-merchantid-domain-association.txt')
# Run the app
if __name__ == '__main__':
    app.run(host="72.193.225.119", debug=True)
