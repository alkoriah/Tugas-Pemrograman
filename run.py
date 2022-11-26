from flask import Flask
import mysql.connector

#initial app web
web = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    database="ti_5b"
)

@web.route('/')
def Home():
    return render_template('home.html')

@web.route('/mahasiswa')
def ListMahasiswa():
    cursor = db.cursor
    cursor.execute("SELECT * FROM tb_ti5b")
    result = cursor.fetchall()

    return render_template('list_mhs.html', data=result)

@web.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form
        nama = data['nama']
        nim = data['nim']
        alamat = data['alamat']

        cursor = db.cursor()
        query = f"INSERT INTO tb_ti5b (nama, nim, alamat) VALUES('{nama}', '{nim}', '{alamat}')"
        cursor.execute(query)
        db.commit()

        return redirect('/mahasiswa', code=302, Response=None)

    return render_template('form.html')


@web.route('/hapus/<id>')
def HapusMhs(id):
    cursor = db.cursor()
    query = f"DELETE FROM tb_ti5b WHERE id='{id}'"
    cursor.execute(query)
    db.commit()

    return redirect('/mahasiswa', code=302, Response=None)
    
if __name__=='__main__':
    web.run()