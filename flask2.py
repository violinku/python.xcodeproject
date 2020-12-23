from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('rack_1.html')
    # render_template('dongkuk.html')
        
        
if __name__ == '__main__':
    app.run()
