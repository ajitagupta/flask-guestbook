from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
messages = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        if name and message:
            messages.append({'name': name, 'message': message})
        return redirect(url_for('guestbook'))
    return render_template('guestbook.html', messages=messages)

@app.route('/reset')
def reset():
    messages.clear()
    return redirect(url_for('guestbook'))

if __name__ == '__main__':
    app.run(debug=True)
