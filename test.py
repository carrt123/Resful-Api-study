from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "carrt"
user_dict = {
    1 : {"name": "张三", "age":17},
    2  : {"name": "李四", "age": 18}
}
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get("pwd")
    if user == "123456" and pwd=="123":
        # return redirect('/')
        session['xxx'] = "123456"
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/')
def index():
    username = session.get('xxx')
    if not username:
        return redirect(url_for('login'))
    return render_template('index.html', user_dict = user_dict)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    uid = request.args.get('uid')
    uid = int(uid)

    if request.method == "GET":
        info = user_dict[uid]

        return render_template('edit.html', info=info)

    name = request.form.get('name')
    age = request.form.get('age')

    print(name, age, uid)
    user_dict[uid]['name'] = name
    user_dict[uid]['age'] = age
    return redirect(url_for('index'))

@app.route('/delete/<uid>')
def delete(uid):
    del user_dict[int(uid)]
    return redirect("/")


print("第五次提交")
if __name__ == '__main__':
    app.run(debug=True, port=8000)




