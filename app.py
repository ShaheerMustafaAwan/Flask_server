from flask import Flask, request, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        timestamp = datetime.now().isoformat()

        log_file = os.path.join(log_dir, 'user_logs.txt')

        with open(log_file, 'a') as f:
            f.write(f"\n[{timestamp}] Name: {name}, Message: '{message}' from Flask server.")

        return render_template('thankyou.html', name=name, message=message)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)