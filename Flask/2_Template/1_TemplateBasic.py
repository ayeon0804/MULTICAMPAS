from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('1_TemplateBasic.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)