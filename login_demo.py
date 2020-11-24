import os
from random import randrange

from flask import Flask, render_template, request, url_for, redirect, make_response, session, jsonify
import sqlite3

from pyecharts.charts import Line
from pyecharts import options as opts

DBName = r'D:\flask_app\login_demo\static\DB.db'
os.chdir(r'D:\flask_app\login_demo')

app = Flask(__name__)
app.secret_key = 'flask123456'

@app.route('/')
def root():
    cookie = request.cookies.get('email')
    print('cookie')
    print(cookie)
    if 'email' in session:
        print('session')
        print(session['email'])
        email = session['email']
        try:
            os.mkdir(r'static\user\{}'.format(email))
        except FileExistsError as e:
            print(e)

        '''
        目录遍历
        '''

        # walk = os.walk(r'static')
        # root_list = []
        # root_list_len = []
        # root_list_len_range = []
        # root_list_split = []
        #
        # for root, dirs, files in walk:
        #     print(root)
        #
        #     root_list.append(root)
        #     # print(files)
        #
        # for i in root_list:
        #     root_list_len.append(len(str(i).split('\\')))
        #     root_list_split.append(str(i).split('\\'))
        #
        # for i in root_list_len:
        #     root_list_len_range.append(list(range(i - 1)))
        #
        # root_list_num = list(range(len(root_list)))
        # print(root_list)
        # print(root_list_len)
        # print(root_list_len_range)
        # print(root_list_num)


        return render_template('index.html')
    else:
        return redirect(url_for('signin'))


@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/signin/action', methods=['POST','GET'])
def signin_action():
    conn = sqlite3.connect(DBName)
    if request.method == 'POST':
        print('in post')
        email = request.form['email']
        password = request.form['password']

        '''
        连接sqlite，验证
        '''

        c = conn.cursor()
        cursor = c.execute("SELECT EMAIL, PASSWORD FROM PW")
        for row in cursor:
            emailDB = row[0]
            passwordDB = row[1]
            if email == emailDB:
                if password == passwordDB:


                    resp = make_response(redirect(url_for('root')))
                    '''
                        设置cookie,默认有效期是临时cookie,浏览器关闭就失效
                        可以通过 max_age 设置有效期， 单位是秒
                    '''''
                    resp.set_cookie("email", email, max_age=3600)
                    session['email'] = email
                    return resp

        return render_template('signin.html', flag=False)
    else:
        print('in else')
        return redirect(url_for('home',name='None'))


@app.route('/<name>/home')
def home(name):

    cookie_1 = request.cookies.get("email")
    print('cookie:'+str(cookie_1))
    return "<a href='/'>root</a>"


def check_cookie():
    cookie_email = request.cookies.get('email')
    if cookie_email != None:
        return True
    else:
        return False


"""echarts Demo"""
def line_base() -> Line:
    global idx
    idx = 9
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name='',
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='动态数据'),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line

@app.route('/lineChart')
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()


idx = 9
@app.route('/lineDynamicData')
def update_line_data():
    global idx
    idx += 1
    return jsonify({"name": idx, "value": randrange(50, 80)})

@app.route('/getRootFile')
def getRootFile():


    print(str(request.args.get('data')))
    walk = os.walk(r'static')
    for root, dirs, files in walk:
        rootName = root
        dirsList = dirs
        filesList = files
        break
    return jsonify({"rootName": rootName, "dirsList": dirsList, "filesList": filesList})

@app.route('/getFileList')
def getFileList():
    s = str(request.args.get('data'))
    print(s)
    walk = os.walk(r'static')
    for root, dirs, files in walk:
        if root == s:
            print(root)
            print(dirs,files)
    return jsonify({"success":"success get"})

if __name__ == '__main__':
    app.run(debug = True)
