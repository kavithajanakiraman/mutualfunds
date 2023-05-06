from flask import Flask,render_template,redirect,request,url_for
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")
def home():
    conn=sql.connect("mutual.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from customer")
    data=cur.fetchall()
    conn.row_factory=sql.Row
    cur1=conn.cursor()
    cur1.execute("select * from mutualfunds")
    data1=cur1.fetchall()
    return render_template("index.html",DATA=data,DATA1=data1)

@app.route("/addcust",methods=['GET','POST'])
def add_cust():
     if request.method=="POST":
          name=request.form.get("name")
          email=request.form.get("email")
          phoneno=request.form.get("phoneno")
          password=request.form.get("password")
          conn=sql.connect("mutual.db")
          cur=conn.cursor()
          cur.execute("insert into customer (name,email,phoneno,password) values (?,?,?,?)",(name,email,phoneno,password))
          conn.commit()
          return redirect(url_for('home'))
     return render_template("add_customer.html")

@app.route("/editcust<string:id>",methods=['GET','POST'])
def edit_cust(id):
     if request.method=="POST":
          name=request.form.get("name")
          email=request.form.get("email")
          phoneno=request.form.get("phoneno")
          password=request.form.get("password")
          conn=sql.connect("mutual.db")
          cur=conn.cursor()
          cur.execute("update customer set name=?, email=?,phoneno=?,password=? where id=?",(name,email,phoneno,password,id))
          conn.commit()
          return redirect(url_for('home'))
     conn=sql.connect("mutual.db")
     conn.row_factory=sql.Row
     cur=conn.cursor()
     cur.execute("select * from customer where id=?",(id,))
     data=cur.fetchone()
     return render_template("edit_customer.html",DATA=data)

@app.route("/deletecust<string:id>",methods=['GET'])
def delete_cust(id):
     conn=sql.connect("mutual.db")
     cur=conn.cursor()
     cur.execute("delete from customer where id=?",(id,))
     conn.commit()
     return redirect(url_for('home'))

@app.route("/addmutual",methods=['GET','POST'])
def add_mutual():
     if request.method=="POST":
          name=request.form.get("name")
          schemecode=request.form.get("schemecode")
          nav=request.form.get("nav")
          units=request.form.get("units")
          totalvalue=int(nav)*int(units)
          conn=sql.connect("mutual.db")
          cur=conn.cursor()
          cur.execute("insert into mutualfunds (name,schemecode,nav,units,totalvalue) values (?,?,?,?,?)",(name,schemecode,nav,units,totalvalue))
          conn.commit()
          return redirect(url_for('home'))
     return render_template("add_mutualfund.html")

@app.route("/editmutual<string:id>",methods=['GET','POST'])
def edit_mutual(id):
     if request.method=="POST":
          name=request.form.get("name")
          schemecode=request.form.get("schemecode")
          nav=request.form.get("nav")
          units=request.form.get("units")
          totalvalue=int(nav)*int(units)
          conn=sql.connect("mutual.db")
          cur=conn.cursor()
          cur.execute("update mutualfunds set name=?, schemecode=?,nav=?,units=?,totalvalue=? where id=?",(name,schemecode,nav,units,totalvalue,id))
          conn.commit()
          return redirect(url_for('home'))
     conn=sql.connect("mutual.db")
     conn.row_factory=sql.Row
     cur=conn.cursor()
     cur.execute("select * from mutualfunds where id=?",(id,))
     data=cur.fetchone()
     return render_template("edit_mutualfund.html",DATA1=data)

@app.route("/deletemutual<string:id>",methods=['GET'])
def delete_mutual(id):
     conn=sql.connect("mutual.db")
     cur=conn.cursor()
     cur.execute("delete from mutualfunds where id=?",(id,))
     conn.commit()
     return redirect(url_for('home'))



if __name__=="__main__":
     app.run(debug=True)