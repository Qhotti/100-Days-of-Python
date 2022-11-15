from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    user=request.form['username']
    password=request.form['password']
    return render_template('thing.html', username=user,password=password)

if __name__ == '__main__':
    app.run(debug=True)