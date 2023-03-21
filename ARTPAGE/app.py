from flask import Flask,url_for,render_template,redirect,request
app=Flask(__name__ , template_folder='template')

@app.route('/')
def adminpage():
    return render_template('adminpage.html')


@app.route('/home')
def home():
    return render_template('adminpage.html')

@app.route('/login', methods=['POST','GET'])
def login(e):
    return render_template('login.html')

@app.errorhandler(404)
@app.route('/acrylic')
def acrylic(e):
    return render_template('acrylic.html')


@app.route("/charcoal" )
def charcoal(e):
    return render_template('charcoal.html')


@app.route('/potrait')
def potrait(e):
    return render_template('potrait.html')
    
    
if __name__ == "__main__":
    app.run(debug=True)

