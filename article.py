from flask import Flask, request, redirect, render_template, url_for, flash
from datetime import datetime
from flask import flash


app = Flask(__name__)
app.secret_key = '1a2b3c4d5e'

comments = []  


@app.route('/', methods=['GET', 'POST'])
def article():
    if request.method == 'POST':
        name = request.form.get('name')
        comment_text = request.form.get('comment')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        comments.append({
            'name': name,
            'text': comment_text,
            'timestamp': timestamp
        })
        return redirect(url_for('article'))
    return render_template("article.html", comments=comments)

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET'])
def contact():
    
    return render_template("contact.html")

@app.route('/submit_contact',  methods=['GET','POST'])
def submit_contact():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        appointment = request.form.get('appointment')
        message = request.form.get('message')

        flash('Your message has been received. Thank you for reaching out!')
    
        return redirect(url_for('submit_contact'))
    return render_template('submit_contact.html')

if __name__ == "__main__":
    app.run(debug=True)
