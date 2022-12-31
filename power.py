import time
import webbrowser
systime = time.localtime()#取得當前時間
result = time.strftime("%Y-%m-%d %H:%M:%S %p", systime)#轉換為看得懂的格式
run = True #控制運行
url = "https://youtu.be/Jrg9KxGNeJY"#要開啟的網址
while (run):
    if (result == "2022-12-31 21:48:00 PM"):
        webbrowser.open(url,new=0,autoraise=True)#在默認瀏覽器開啟url
        run = False
        break;