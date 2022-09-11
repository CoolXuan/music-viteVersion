from user import User
import re
from flask import Flask, session
from common.utility import gen_email_code, send_email
# 创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = "1"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
'''
返回前端格式
{
  rescode:1
  data:
  message:
}


'''
# 测试网页链接使用
@app.route('/', methods=['GET'])
def logintest():
    return 'login-success'

@app.route('/mysql', methods=['GET'])
def mysqltest():
    user=User()
    if user.get_data("1976756410@qq.com"):
        return 'mysql-success'

@app.route('/<email>', methods=['GET'])
def emailtest(email):
        code = gen_email_code()
        send_email(email, code)
        return 'email-success'

@app.route('/ecode/<url>', methods=['POST'])
def ecode(url):
    email = url
    user = User()
    # 验证用户是否已经注册
    if len(user.get_data(email)) > 0:
        return 'user-repeated'

    if not re.match('.+@.+\..+', email):
        return 'email-invalid'

    code = gen_email_code()
    send_email(email, code)
    try:
        session['ecode'] = code  # 将邮箱验证码保存在Session中
        print(session['ecode'])
        return 'send-pass'
    except:
        return 'send-fail'


@app.route('/user/<url>', methods=['POST'])
def register(url):
    user = User()
    email = url.split('&')[0].strip()
    password = url.split('&')[1].strip()
    ecode = url.split('&')[2].strip()
    print(email, password, ecode.lower(), session.get('ecode').lower())
    # 校验邮箱验证码是否正确
    if ecode.lower() != session.get('ecode').lower():
        return 'ecode-error'
    else:
        print('a')
        user_name = user.insert_data(email, password)
        print(user_name)
        if user_name != '':
            return user_name
        # # 实现注册功能
        # password = password
        # result = user.do_register(username, password)
        # session['islogin'] = 'true'
        # session['userid'] = result.userid
        # session['username'] = username
        # session['nickname'] = result.nickname
        # session['role'] = result.role
        # # 更新积分详情表
        return 'reg-pass'


@app.route('/login/<url>', methods=['POST'])
def login(url):
    print(url)
    user = User()
    userdata = []
    email = url.split('&')[0].strip()
    password = url.split('&')[1].strip()
    userdata = list(user.get_data(email)[0])
    print(userdata)
    if userdata != []:
        print('已获取用户信息！')
        if email == str(userdata[1]) and str(password) == str(userdata[3]):
            idname = str(userdata[2])
            print(idname)
            return idname
        else:
            return 'login_error'
    else:
        return 'login_error'
# ecode = url.split('&')[2].strip()
# print(email, password, ecode.lower(), session.get('ecode').lower())
# # 校验邮箱验证码是否正确
# if ecode.lower() != session.get('ecode').lower():
#     return 'ecode-error'

# # 验证用户是否已经注册
# if len(book.get_data(email)) > 0:
#     print('user-repeated')
#     return 'user-repeated'
# else:
#     print('a')
# # 实现注册功能
# password = password
# result = user.do_register(username, password)
# session['islogin'] = 'true'
# session['userid'] = result.userid
# session['username'] = username
# session['nickname'] = result.nickname
# session['role'] = result.role
# # 更新积分详情表

# user = Users()
# username = request.form.get('username').strip()
# password = request.form.get('password').strip()
# vcode = request.form.get('vcode').lower().strip()

# # 校验图形验证码是否正确
# if vcode != session.get('vcode') and vcode != '0000':
#     return 'vcode-error'

# else:
#     # 实现登录功能
#     password = hashlib.md5(password.encode()).hexdigest()
#     result = user.find_by_username(username)
#     if len(result) == 1 and result[0].password==password:
#         session['islogin'] = 'true'
#         session['userid'] = result[0].userid
#         session['username'] = username
#         session['nickname'] = result[0].nickname
#         session['role'] = result[0].role
#         # 更新积分详情表
#         Credit().insert_detail(type='正常登录',target='0',credit=1)
#         user.update_credit(1)
#         # 将Cookie写入浏览器
#         response = make_response('login-pass')
#         response.set_cookie('username', username, max_age=30*24*3600)
#         response.set_cookie('password', password, max_age=30*24*3600)
#         return response
#     else:
#         return 'login-fail'
# @app.route('/logout')
# def logout():
#     # 清空Session，页面跳转
#     session.clear()

#     response = make_response('注销并进行重定向', 302)
#     response.headers['Location'] = url_for('index.home')
#     response.delete_cookie('username')
#     response.set_cookie('password', '', max_age=0)
#     return response

if __name__ == '__main__': 
    app.run()
