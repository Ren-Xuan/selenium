from selenium import webdriver
import time
import http.client
import os
import urllib.request
import locale
locale.setlocale(locale.LC_ALL,'en')
def req(url,sleepTime):
    while True:
        try:
            result=str(urllib.request.urlopen(url).read().decode("utf8", "ignore"))
            return result
        except:
            time.sleep(sleepTime)
            continue

def get_webservertime(host):
    conn=http.client.HTTPConnection(host)
    conn.request("GET", "/")
    r=conn.getresponse()
    ts=  r.getheader('date') 
    #将GMT时间转换成北京时间
    ltime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    print(ltime)
    ttime=time.localtime(time.mktime(ltime)+8*60*60)
    print(ttime)
    dat="date %u-%02u-%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
    tm="time %02u:%02u:%02u"%(ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
    print (dat,tm)
    os.system(dat)
    os.system(tm)
#设置系统时间
get_webservertime('www.baidu.com')
#开始
wd =webdriver.Chrome()
wd.set_window_size(1280,1000)
wd.implicitly_wait(10)#隐式等待
wd.get('https://act.daoju.qq.com/act/a20200207duobao/index.htm')

nowTime=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
print(nowTime)
print('等待60秒扫码登陆')
time.sleep(120)
############################提前几分钟获取手机号，循环每次睡眠十秒，以分钟跳出循环
while True:
    print(time.strftime('ready for accpting phone:%H:%M',time.localtime(time.time())))
    if time.strftime('%H-%M',time.localtime(time.time())) == "23-59":
        break
    time.sleep(10)
tokenUrl="http://api.xinma1.com:10000/login?uName=\
1584160851&pWord=qq1584160851&Developer=Developer\
=x4XsHeMB4hYfoYl67d%2fHOA%3d%3d"
#token=urllib.request.urlopen("http://api.xinma1.com:10000/login?uName=\
#1584160851&pWord=qq1584160851&Developer=Developer\
#=x4XsHeMB4hYfoYl67d%2fHOA%3d%3d").read().decode("utf8", "ignore").split("&")[0]
token=req(tokenUrl,1).split("&")[0]
print("接号"+token)

iPhoneNumberUrl=str("http://api.xinma1.com:10000/getPhone?ItemId=46957&token="+token)
iPhoneNumber=str(req(iPhoneNumberUrl,1).split(";")[0])
print(iPhoneNumber)
with open('fail.txt', 'w+') as ff:
    ff.write(str(token)+"="+iPhoneNumber)
js='''D.mo.amsSubmit2(285729, 644781, {
	    sNeedSubmitPopDiv: false, 
            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
             success: function (res) {
                alert(res.sMsg);
            },failure:function(res){
                D.mo.amsSubmit2(285729, 644781, {
	                sNeedSubmitPopDiv: false, 
                    sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                     success: function (res) {
                        alert(res.sMsg);
                    },failure:function(res){
                           D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                              alert(res.sMsg);
                            },failure:function(res){
                           D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                           D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                                D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                                D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                                D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                                D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                            D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                            D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                            D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                            D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                            D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                            D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                            D.mo.amsSubmit2(285729, 644781, {
	                        sNeedSubmitPopDiv: false, 
                            sData: {'iPhoneNumber':'''+iPhoneNumber+''','getId':5},
                             success: function (res) {
                            alert(res.sMsg);
                            },failure:function(res){
                                console.log(res.sMsg);
	                        }
                        });
                                console.log(res.sMsg);
	                        }
                        });
                                console.log(res.sMsg);
	                        }
                        });
                                console.log(res.sMsg);
	                        }
                        });
                                console.log(res.sMsg);
	                        }
                        });console.log(res.sMsg);
	                        }
                        });console.log(res.sMsg);
	                        }
                        });console.log(res.sMsg);
	                        }
                        });console.log(res.sMsg);
                                }
                        });console.log(res.sMsg);
	                        }
                        });console.log(res.sMsg);
	                        }
                        });console.log(res.sMsg);
	                        }
                        });console.log(res.sMsg);
                                }
                        });console.log(res.sMsg);
                                }
                        });console.log(res.sMsg);
                                }
                        });console.log(res.sMsg);
                        }
    });'''
print("等待到十二点整")
while True:
    print(time.strftime('%H-%M-%S',time.localtime(time.time())))
    if time.strftime('%H-%M-%S',time.localtime(time.time())) == "23-59-59":
        break
time.sleep(0.9)
print('23:59:59:900ms发短信')
wd.execute_script(js)
#接码
phoneCode="1234"
while True:
    try:
        print(time.strftime('ready for gettting code:%H:%M',time.localtime(time.time())))
        time.sleep(0.5)
        messageUrl=str("http://api.xinma1.com:10000/getMessage?token="+token+"&ItemId=46957&Phone="+iPhoneNumber)
        message=str(req(messageUrl,1))
        print(message)
        if not message.__contains__("False"):
            try:
                phoneCode=str(message.split("是")[1].split("，")[0])
                break
            except:
                continue
    except:
        continue
while True:
    print(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
    print("接到码"+phoneCode)
    ############################睡眠一定时间不能频繁获取
    submit='''D.mo.amsSubmit(285729, 641649, {
		sData: {
                    'dmid': 5,'phoneCode':'''+phoneCode+''','iPhoneNumber':'''+iPhoneNumber+'''
			},
		success: function (res) {
		Hx.updateJf(1500);
		if(D.mo.isH5){
		closeDialog();
		}
		alert(res.sMsg);
		},failure:function(res){
			console.log(res.sMsg);
		}
	});'''
    cnt =0
    while cnt<100:
        wd.execute_script(submit)
        time.sleep(0.05)
        cnt=cnt+1
    break
    #凌晨零点十秒以后基本上没了
    if time.strftime('%S',time.localtime(time.time())) > '15' and \
        time.strftime('%S',time.localtime(time.time())) < '40' :
        print('progress ended..... ')
        break
    time.sleep(0.5)
print('end......')

