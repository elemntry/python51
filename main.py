from flask import Flask

app = Flask(__name__)


def calculate(a, b):
    return a + b


@app.route("/")
def index():
    # return f"This is a payment pag! Please pay {calculate(5,5)} USD"
    return "This is a payment pag! Please pay %s USD" % (calculate(5, 5))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
