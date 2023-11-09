from flask import Flask, render_template,request,flash,redirect,url_for
import sqlite3
import os
app=Flask(__name__)

app.secret_key="123"
app.config['UPLOAD_FOLDER']="static/images"
con=sqlite3.connect("database.db")
con.execute("CREATE TABLE IF NOT EXISTS data(pid INTEGER PRIMARY KEY ,name TEXT,address TEXT)")
con.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        name=request.form['name']
        password=request.form['password']
        con=sqlite3.connect("database8.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from customer where name=? and mail=?",(name,password))
        data=cur.fetchone()
        return redirect(url_for("home"))


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            contact=request.form['contact']
            mail=request.form['mail']
            con=sqlite3.connect("database8.db")
            cur=con.cursor()
            cur.execute("insert into customer(name,address,contact,mail)values(?,?,?,?)",(name,address,contact,mail))
            con.commit()
            flash("Record Added  Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("index"))
            con.close()

    return render_template('register.html')

@app.route('/logout')
def logout():
    return redirect(url_for("index"))

@app.route("/addData",methods=["POST","GET"])
def addData():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            con=sqlite3.connect("database.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(name,address)values(?,?)",(name,address))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("item"))
            con.close()
@app.route("/item.html",methods=["POST","GET"])
def item():
 
    con=sqlite3.connect("database.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    return render_template("item.html",data=data)
@app.route('/update_record/<string:id>',methods=["POST","GET"])
def update_record(id):
    con=sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM data where pid=?",(id))
    data = cur.fetchone()
    con.close()

    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute("UPDATE data SET name=?,address=? where pid=?",(name,address,id))
            con.commit()
            flash("Update Successfully","success")
        except:
            flash("Error in Update Operation","danger")
        finally:
            return redirect(url_for("item"))
            con.close()
    return render_template('update_record.html',data=data)

@app.route('/delete_record/<string:id>')
def delete_record(id):
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("item"))
        con.close()

@app.route("/addData1",methods=["POST","GET"])
def addData1():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            con=sqlite3.connect("database2.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(name,address)values(?,?)",(name,address))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("catagory"))
            con.close()

@app.route("/catagory.html",methods=["POST","GET"])
def catagory():
    con=sqlite3.connect("database2.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    return render_template("catagory.html",data=data)

@app.route('/catagory_update/<string:id>',methods=["POST","GET"])
def catagory_update(id):
    con=sqlite3.connect("database2.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM data where pid=?",(id))
    data = cur.fetchone()
    con.close()

    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
           
            con = sqlite3.connect("database2.db")
            cur = con.cursor()
            cur.execute("UPDATE data SET name=?,address=? where pid=?",(name,address,id))
            con.commit()
            flash("Update Successfully","success")
        except:
            flash("Error in Update Operation","danger")
        finally:
            return redirect(url_for("catagory"))
            con.close()
    return render_template('catagory_update.html',data=data)

@app.route('/delete_record1/<string:id>')
def delete_record1(id):
    try:
        con = sqlite3.connect("database2.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("catagory"))
        con.close()
@app.route("/addData3",methods=["POST","GET"])
def addData3():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            con=sqlite3.connect("database3.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(name,address)values(?,?)",(name,address))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("warehouse"))
            con.close()

@app.route("/warehouse.html",methods=["POST","GET"])
def warehouse():
    con=sqlite3.connect("database3.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    return render_template("warehouse.html",data=data)
    
@app.route('/warehouse_update/<string:id>',methods=["POST","GET"])
def warehouse_update(id):
    con=sqlite3.connect("database3.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM data where pid=?",(id))
    data = cur.fetchone()
    con.close()

    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
           
            con = sqlite3.connect("database3.db")
            cur = con.cursor()
            cur.execute("UPDATE data SET name=?,address=? where pid=?",(name,address,id))
            con.commit()
            flash("Update Successfully","success")
        except:
            flash("Error in Update Operation","danger")
        finally:
            return redirect(url_for("warehouse"))
            con.close()
    return render_template('warehouse_update.html',data=data)

@app.route('/delete_record3/<string:id>')
def delete_record3(id):
    try:
        con = sqlite3.connect("database3.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("warehouse"))
        con.close()
@app.route("/addData4",methods=["POST","GET"])
def addData4():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            con=sqlite3.connect("database4.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(name,address)values(?,?)",(name,address))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("attributes"))
            con.close()

@app.route("/attributes.html",methods=["POST","GET"])
def attributes():
 
    con=sqlite3.connect("database4.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    return render_template("attributes.html",data=data)
@app.route('/attributes_update/<string:id>',methods=["POST","GET"])
def attributes_update(id):
    con=sqlite3.connect("database4.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM data where pid=?",(id))
    data = cur.fetchone()
    con.close()

    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
           
            con = sqlite3.connect("database4.db")
            cur = con.cursor()
            cur.execute("UPDATE data SET name=?,address=? where pid=?",(name,address,id))
            con.commit()
            flash("Update Successfully","success")
        except:
            flash("Error in Update Operation","danger")
        finally:
            return redirect(url_for("attributes"))
            con.close()
    return render_template('attributes_update.html',data=data)

@app.route('/delete_record4/<string:id>')
def delete_record4(id):
    try:
        con = sqlite3.connect("database4.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("attributes"))
        con.close()
@app.route("/addData5",methods=["POST","GET"])
def addData5():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            con=sqlite3.connect("database5.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(name,address)values(?,?)",(name,address))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("add_record"))
            con.close()

@app.route("/add_record.html",methods=["POST","GET"])
def add_record():
 
    con=sqlite3.connect("database5.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    return render_template("add_record.html",data=data)

@app.route('/addrecord_update/<string:id>',methods=["POST","GET"])
def addrecord_update(id):
    con=sqlite3.connect("database5.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM data where pid=?",(id))
    data = cur.fetchone()
    con.close()

    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
           
            con = sqlite3.connect("database5.db")
            cur = con.cursor()
            cur.execute("UPDATE data SET name=?,address=? where pid=?",(name,address,id))
            con.commit()
            flash("Update Successfully","success")
        except:
            flash("Error in Update Operation","danger")
        finally:
            return redirect(url_for("add_record"))
            con.close()
    return render_template('addrecord_update.html',data=data)

@app.route('/delete_record5/<string:id>')
def delete_record5(id):
    try:
        con = sqlite3.connect("database5.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("add_record"))
        con.close()
@app.route("/prouducts.html")
def prouducts():
    return render_template("prouducts.html")
@app.route("/order.html")
def order():
    return render_template("order.html")

@app.route("/addData6",methods=["POST","GET"])
def addData6    ():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            contact=request.form['contact']
            number=request.form['number']
            number1=request.form['number1']
            mail=request.form['mail']
            mail1=request.form['mail1']
            mail2=request.form['mail2']
            con=sqlite3.connect("database6.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(name,address,contact,number,number1,mail,mail1,mail2)values(?,?,?,?,?,?,?,?)",(name,address,contact,number,number1,mail,mail1,mail2))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("magorder"))
            con.close()
@app.route("/magorder.html")
def magorder():
    con=sqlite3.connect("database6.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    con.close()
    return render_template("magorder.html",data=data)

@app.route('/order_record/<string:id>',methods=["POST","GET"])
def order_record(id):
    con=sqlite3.connect("database6.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM data where pid=?",(id))
    data = cur.fetchone()
    con.close()

    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            contact=request.form['contact']
            number=request.form['number']
            number1=request.form['number1']
            mail=request.form['mail']
            mail1=request.form['mail1']
            mail2=request.form['mail2']
            con = sqlite3.connect("database7.db")
            cur = con.cursor()
            cur.execute("UPDATE data SET name=?,address=?,contact=?,number=?,number1=?,mail=?,mail1=?,mail2=? where pid=?",(name,address,contact,number,number1,mail,mail1,mail2,id))
            con.commit()
            flash("Update Successfully","success")
        except:
            flash("Error in Update Operation","danger")
        finally:
            return redirect(url_for("magorder"))
            con.close()
    return render_template('order_record.html',data=data)

@app.route('/delete_record6/<string:id>')
def delete_record6(id):
    try:
        con = sqlite3.connect("database6.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("magorder"))
        con.close()

@app.route("/users_order.html")
def users_order():
    return render_template("users_order.html")  
    
    

@app.route("/addData7",methods=["POST","GET"])
def addData7():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            contact=request.form['contact']
            mail=request.form['mail']
            mail1=request.form['mail1']

            con=sqlite3.connect("database9.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(name,address,contact,mail,mail1)values(?,?,?,?,?)",(name,address,contact,mail,mail1))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("member"))
            con.close()

@app.route("/member.html",methods=["POST","GET"])
def member():
    con=sqlite3.connect("database9.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM data")
    data=cur.fetchall()
    con.close()
    return render_template("member.html",data=data)

@app.route('/member_record/<string:id>',methods=["POST","GET"])
def member_record(id):
    con=sqlite3.connect("database9.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM data where pid=?",(id))
    data = cur.fetchone()
    con.close()

    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            contact=request.form['contact']
            mail=request.form['mail']
            mail1=request.form['mail1']
            con = sqlite3.connect("database9.db")
            cur = con.cursor()
            cur.execute("UPDATE data SET name=?,address=?,contact=?,mail=?,mail1=? where pid=?",(name,address,contact,mail,mail1,id))
            con.commit()
            flash("Update Successfully","success")
        except:
            flash("Error in Update Operation","danger")
        finally:
            return redirect(url_for("member"))
            con.close()
    return render_template('member_record.html',data=data)

@app.route('/delete_record7/<string:id>')
def delete_record7(id):
    try:
        con = sqlite3.connect("database9.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("member"))
        con.close()
        
if(__name__=='__main__'):
    app.run(debug=True)
