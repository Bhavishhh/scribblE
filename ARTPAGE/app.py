from flask import Flask,url_for,render_template,redirect,request
app=Flask(__name__ , template_folder='template')

@app.route('/')
def adminpage():
    return render_template('adminpage.html')


@app.route('/home')
def home():
    return render_template('adminpage.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/acrylic')
def acrylic():
    return render_template('acrylic.html')


@app.route("/charcoal" )
def charcoal():
    return render_template('charcoal.html')


@app.route('/potrait')
def potrait():
    return render_template('potrait.html')
    
if __name__ == "__main__":
    app.run(debug=True)

