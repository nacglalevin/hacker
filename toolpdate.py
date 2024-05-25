from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from selenium.webdriver.chrome.options import Options

#定义执行次数
times = 0
#发邮件函数
def send_mail(tx,tittle,rev,rev_name,sen_name):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器,本人使用的是qq smtp 服务
    mail_user="xxxx@qq.com"    #用户名
    mail_pass="xxxxx"   #口令 
    sender = 'xxxxx@qq.com'#发送人的qq邮箱
    receivers = [rev]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText(tx)
    message['From'] = Header(sen_name, 'utf-8') #括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
    message['To'] = Header(rev_name, 'utf-8') #括号里的对应收件人邮箱昵称、收件人邮箱账号
    subject = tittle
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 587)  # 发件人邮箱中的SMTP服务器，端口是465
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        return "success"
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
        return "error"

#比较两个文件是否相同函数，相同返回yes,不同返回no
def judge():
    num=0
    with open("a1.txt",encoding='utf-8') as file01:
        for line in file01:
            num=num+1
            # print(num)
    # 计算一共有几行
    with open("a1.txt",'r',encoding='utf-8') as x ,open("a2.txt",'r',encoding='utf-8') as y:
        line1=x.readlines()
        line2=y.readlines()
    for i in range(num):
        if line1[i]==line2[i]:
            print("yes")
            return "yes"
        else:
            var=str(i+1)
            print("no")
            return "no"

#无头浏览器参数配置
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")
#创建浏览器对象
web = Chrome(options=opt)
#web = Chrome()  有头浏览器
#打开一个网址
web.get("xxxxx/")
#找到输入框，输入账号密码
web.find_element_by_xpath('//*[@id="UserName"]').send_keys("xxxxx")
web.find_element_by_xpath('//*[@id="PassWord"]').send_keys("xxxxx",Keys.ENTER)
# 登录按钮
login = web.find_element_by_xpath('//*[@id="btLogin"]')
login.click()
time.sleep(1)
while(1):
    #如果执行次数超过180（3个小时，即发送一条邮件，表示程序正常工作）
    if(times > 180):
        times = times % 180
        send_mail('tx','tittle','rev','rev_name','sen_name')
    #找到iframe1 进入iframe1
    iframe1 = web.find_element_by_xpath('//*[@id="MenuFrame"]')
    web.switch_to.frame(iframe1) 
    #进入课务管理
    kwgl = web.find_element_by_xpath('//*[@id="menu"]/div[2]/div[1]/div[2]/a')
    kwgl.click()
    time.sleep(1)
    #进入成绩页面
    cj = web.find_element_by_xpath('//*[@id="tree1_6_span"]')
    cj.click()
    #转到默认页面
    web.switch_to.default_content()
    #转到课程frame
    iframe2 = web.find_element_by_xpath('//*[@id="PageFrame"]')
    web.switch_to.frame(iframe2)
    time.sleep(1)
    #提取课程信息
    tx = web.find_element_by_xpath('//*[@id="ctl00_contentParent_dgData"]/tbody').text
    print(tx)
    #写入txt文本中
    with open("a1.txt","w",encoding='utf-8') as f:
        f.write(tx)  # 自带文件关闭功能，不需要再写f.close()
    #判断是否相同
    flag = judge()
    if(flag=="no"):
        #调用发送邮件的函数
        send_mail(tx,"tittle",'xxxx@qq.com','rev_name','sen_name')
        #更新文本内容
        with open("a2.txt","w",encoding='utf-8') as f:
            f.write(tx)  # 自带文件关闭功能，不需要再写f.close()        
    #转到默认页面
    web.switch_to.default_content()
    #刷新页面
    web.refresh()
    #程序睡眠一分钟,以免增加服务器造成不必要的负担
    time.sleep(60)
    #记录爬取次数
    times = times + 1
    print(times)