from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def home():
    return render_template('tool.html', image_list=[])

if __name__ == '__main__':
    app.run()