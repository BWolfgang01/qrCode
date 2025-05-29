from flask import Flask, request, send_file, render_template_string
from qrCode import qr
app = Flask(__name__)
HTML_TEMPLATE = '''
    <html>
        <body>
            <form method="get">
                <input type="text" name="value" placeholder="Enter text for QR code" />
                <input type="submit" value="Generate" />
            </form>
            {% if value %}
                <h2>Result for: "{{ value }}"</h2>
                <img src="/qr?value={{ value }}">
            {% endif %}
        </body>
    </html>
'''
@app.route('/')
def home():
    value = request.args.get('value', '')
    return render_template_string(HTML_TEMPLATE, value=value)

@app.route('/qr')
def generate_qr():
    value = request.args.get('value', '')
    if not value:
        return "No value provided", 400
    img_io = qr(value)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
