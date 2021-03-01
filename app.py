from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():#ส่งข้อมูลแบบดิกชันนารี
   data = {'name':'กรรณธรรม', 'age':'45', 'location':'bangyai'}
   return render_template("index.html", DATA=data)

@app.route('/about')
def about():# ส่งข้อมูลแบบ list และใช้ for looop เช็คค่าออกมาแสดง
   products = ["มอเตอร์","แบตเตอรี่","สายพาน","ชุดตกแต่ง",'ล้อแม็ก', 'เครื่องเสียงรถยนต์']
   return render_template("about.html", myproduct = products) 


@app.route('/admin')
def profile():# เพิ่มค่าพารามิเตอร์และส่งค่า user,pass ไปตรวจสอบ
    name = 'JHON'
    age = '18'
    username = 'hs4qwc'
    Pass = '55555'
    return render_template("admin.html", neme=name, age=age, username=username, Pass=Pass)

@app.route('/layout')
def LAYOUT():
    TEMP = '38'
    HUDI = '85'
    return render_template("layout.html", temp=TEMP, hudi=HUDI)

@app.route('/user/<name>/<age>')#การส่งค่า
def USER(name, age):
    return '<h1>ชื่อ: {} อายุ: {} </h1>'.format(name[1], age)

if __name__ == "__main__":
    app.run(debug=True)



