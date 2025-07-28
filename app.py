
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Mój Chatbot</title>
</head>
<body>
    <h1>Chatbot</h1>
    <form action="/chat" method="post">
        <input type="text" name="message" placeholder="Napisz wiadomość" required>
        <button type="submit">Wyślij</button>
    </form>
    {% if response %}
        <p><strong>Odpowiedź:</strong> {{ response }}</p>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form.get("message")
    # Prosta symulacja odpowiedzi
    response = f"Echo: {message}"
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
