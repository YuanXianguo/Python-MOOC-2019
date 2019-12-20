for i in range(3):
    user = input()
    psw = input()
    if user.title() == 'Kate' and psw == '666666':
        print("登录成功！")
        break
else:
    print("3次用户名或者密码均有误！退出程序。")
