from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/cafes')
def get_cafes():
    conn = sqlite3.connect('cafes.db')
    c = conn.cursor()
    cafes = []
    for row in c.execute('SELECT * FROM cafes'):
        cafes.append({
            'id': row[0],
            'name': row[1],
            'location': row[2],
            'rating': row[3]
        })
    conn.close()
    return jsonify({'cafes': cafes})

@app.route('/cafes', methods=['POST'])
def add_cafe():
    conn = sqlite3.connect('cafes.db')
    c = conn.cursor()
    c.execute('INSERT INTO cafes (name, location, rating) VALUES (?, ?, ?)',
              (request.form['name'], request.form['location'], request.form['rating']))
    conn.commit()
    conn.close()
    return 'Cafe added'

@app.route('/cafes/<int:id>', methods=['DELETE'])
def delete_cafe(id):
    conn = sqlite3.connect('cafes.db')
    c = conn.cursor()
    c.execute('DELETE FROM cafes WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return 'Cafe deleted'

if __name__ == '__main__':
    app.run(debug=True)
