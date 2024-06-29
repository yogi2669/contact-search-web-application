from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

contacts = {
    'charudeep': { 'phone': '7569530667', 'email': 'charu@gmail.com' },
    'surya': { 'phone': '9876543210', 'email': 'surya@gmail.com' },
    'ram': { 'phone': '9618151774', 'email': 'ram@gmail.com' },
    'vasanth': { 'phone': '9381596264', 'email': 'vasanth@gmail.com' },
    'vamsi': { 'phone': '6305661136', 'email': 'vamsi@gmail.com' },
    'adithya': { 'phone': '8688916103', 'email': 'adithya@gmail.com' },
    'ram charan': { 'phone': '777-777-7777', 'email': 'ram charan@example.com' },
    'dileep': { 'phone': '7569530667', 'email': 'dileep@gmail.com' },
    'archit': { 'phone': '9876543210', 'email': 'archit@gmail.com' },
    'ankit': { 'phone': '9618151774', 'email': 'ankit@gmail.com' },
    'ganesh': { 'phone': '9381596264', 'email': 'ganesh@gmail.com' },
    'ritiesh': { 'phone': '6305661136', 'email': 'ritiesh@gmail.com' },
    'santosh': { 'phone': '8688916103', 'email': 'santosh@gmail.com' },
    'devi prasad': { 'phone': '9441102669', 'email': 'ram charan@example.com' },
    'preethi': { 'phone': '9959673577', 'email': 'kachabadam@gmail.com' },
    'hema': { 'phone': '9182873464', 'email': 'hema@gmail.com' },

}

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/api/contacts')
def get_contacts():
    return jsonify(list(contacts.keys()))

@app.route('/api/search', methods=['GET'])
def search_contacts():
    query = request.args.get('query', '')

    matching_contacts = {name: contacts[name] for name in contacts if query.lower() in name.lower()}

    return jsonify(matching_contacts)

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

       
        contacts[name] = {'phone': phone, 'email': email }
        
        return redirect(url_for('index'))

    return render_template('add_contact.html')

if __name__ == '__main__':
    app.run(debug=True)

