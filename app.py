from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='assets')

# Serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')

# Serve about.html
@app.route('/about')
def about():
    return render_template('about.html')

# Serve chatbot.html
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Serve contact.html
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Serve facebooklogin.html
@app.route('/facebooklogin')
def facebook_login():
    return render_template('facebooklogin.html')

# Serve portfolio.html
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Serve ui-ux.html
@app.route('/ui-ux')
def ui_ux():
    return render_template('ui-ux.html')

# Serve webdev.html
@app.route('/webdev')
def webdev():
    return render_template('webdev.html')

# Serve webdev.html
@app.route('/flask')
def flask():
    return 'Running FLask'

if __name__ == '__main__':
    app.run(debug = True)