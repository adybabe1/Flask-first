from flask import Flask, render_template, url_for
app = Flask(__name__) # this gets the name of the file as the app name

@app.route("/") # this tells flask what URL to serve up
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')
  
@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page', text='This is the second page')
  
#put the code in bypass manual environment variable setting
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")