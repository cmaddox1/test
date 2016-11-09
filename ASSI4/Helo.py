from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('Assi4.html')
def handle_data():
        projectpath = request.form.assignment_4.py


    

if __name__ == "__main__":
    app.run(debug=True)    



