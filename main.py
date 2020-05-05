import threading, os, http.server

MESSAGE_FOR_GEEK = "你好，我是这个程序的开发者，不管你是谁，你看起来都反编译了这个程序，这无关紧要。我想你一定是一个开发者吧，百度的想法简直是司马昭之心，为了保护我们开发者的正当利益，请务必传播本软件，谢谢。MS187敬上"
if not os.path.exists("bdlogin.html"):
    os.mkdir("api")
    file1 = open("api/init", "w")
    file1.write(
        """{"srecord":{"autoQuery":true},"loginurl":{"url":"http:\/\/pandownload.com\/bdlogin.html"},"wke":"http:\/\/dl.pandownload.club\/dl\/node-190312.dll","pcscfg":{"appid":250528,"ua":"","ct":0},"flag":1,"ad":{"url":"https:\/\/pandownload.com\/donate.html","image":"http:\/\/pandownload.com\/images\/donate.png","attribute":"width=\"88\" height=\"100\" padding=\"0,0,5,0\"","rand":100},"bdc":["aF5yaHQQfQt3E3lxdHdjVmF4f3hae3JsfFxIbGxbW152FHF0anpdW3R5UHR1H1hxdwdoTGRMcXR1THsRbF92XXJbdmpveF93Yl9TE3dod3tYaXYIc1oRXGZKbVR1aGkGcV57dmleen1wEAYEdnV9BXF3BQFxd3sCaGh2BHB0BgdpW3F2c3pbAXF3ewJoaAYEcHQGBHZ1fQVxdwUBcXd7AmhoBgRwdAYEdnV9BXF3BQFxd3sCaGgGBHB0BgR2dX0FcXcFAXF3ewJoaAYEcHQGBHZ1fQVxdwUBcXd7AmhoBgRwdAYEdnV9BXF3BQFxd3sCaGgGBHB0BgRpB21SYXYFFH0UDmpben5afkgCdmsFAH9ydxMIflxqEnUHWxVpdgUTcwdsTH0UcBBpdndddV1+XWh2altzWlpLaVxbWH1cXEh1XWMXfAZ5FnR0fV99aXlcagZrWHUHaRZ9EXVJcnRTXH1MYhB9BlFddVoNDw=="],"timestamp":1586998638,"code":0,"message":"success"}""""")
    file2 = open("api/latest", "w")
    file2.write(
        """{"version":"404","url":"https:\/\/dl1.cnponer.com\/files\/PanDownload_v2.2.2.zip","web":"https:\/\/www.lanzous.com\/i8ua9na","detail":"\u591a\u8c22\u4f5c\u8005\uff0c\u8fd9\u51e0\u5e74\u6765\u7684\u66f4\u65b0\n\u963f\u91cc\u560e\u591a\uff01\uff01\uff01\n\u6700\u65b0\u7248\u672c\u4e3a:2.2.2\n\u66f4\u65b0\u65f6\u95f4: 2020-01-24\n\u66f4\u65b0\u5185\u5bb9:\n1. \u754c\u9762\u4f18\u5316\n2. bug\u4fee\u590d","md5":"13d3da755509afe3be8f7fc191a50cbd","code":0,"message":"success"}""")
    os.mkdir("api/script")
    file3 = open("api/script/list", "w")
    file3.write(
        """{"scripts":[{"name":"search_pandown.lua","remove":true},{"name":"search_ncckl.lua","remove":true},{"name":"search_quzhuanpan.lua","remove":true},{"name":"anime_01.lua","remove":true},{"name":"anime_02.lua","remove":true},{"name":"anime_dilidili.lua","remove":true},{"name":"anime","remove":true},{"name":"s","id":2,"url":"http:\/\/pandownload.com\/static\/scripts\/s008","md5":"8dfd9a6c08d06bec27ae358f315cca8f"},{"name":"download_pcs.lua","id":1000,"url":"http:\/\/pandownload.com\/static\/scripts\/download_pcs.lua","md5":"38770cd3e9bcd62f7212941b51ca1378"},{"name":"default","id":0,"url":"http:\/\/pandownload.com\/static\/scripts\/default_0.6.7_3fee3733","md5":"a1124f076924209d0322078000cdc882","key":"568729a30cee34aec0e6fc7a6e303272"}],"code":0,"message":"success"}""")
    file4 = open("bdlogin.html", "w")
    file4.write(
        """<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="referrer" content="never">
    <title>Login</title>
    <style>
        #messagebox {
            position: fixed;
            width: 100%;
            max-width: 530px;
            background: #fff;
            padding: 30px;
            margin: auto;
            left: 0;
            right: 0;
            border-radius: 4px;
        }

        #messagebox h1 {
            text-align: center;
        }

        #messagebox p {
            margin: 10px 0;
        }

        .ok-btn {
            color: #fff;
            background-color: #5cb85c;
            border-color: #4cae4c;
            display: inline-block;
            padding: 6px 12px;
            margin-bottom: 0;
            font-size: 14px;
            font-weight: 400;
            line-height: 1.42857143;
            text-align: center;
            white-space: nowrap;
            vertical-align: middle;
            cursor: pointer;
            border: 1px solid transparent;
            border-radius: 4px;
            display: block;
            margin: auto;
            max-width: 150px;
        }

        .ok-btn:hover {
            background: #6ecc6e;
        }

        .not-visible {
            visibility: hidden;
        }
    </style>
</head>

<body>
    <div id="messagebox" style="display: none;">
        <h1>
            提示
        </h1>
        <p>
            您当前使用的是<b>IE内核</b><br>
            如果通过<b>用户名密码登录</b>可能会出现<b>当前浏览器版本过低无法登录</b>的问题<br>
            解决方法：<br>
            1. 下载Webkit内核（下载地址在窗口底部）<br>
            2. 使用扫码登录或第三方账号登录
        </p>
        <div class="ok-btn"
            onclick="window.location.href='https://passport.baidu.com/v2/?login&u=https%3A%2F%2Fpan.baidu.com%2Fdisk%2Fhome';">
            <p>
                确定
            </p>
        </div>
    </div>
    <script>
        function detectIE() {
            var ua = window.navigator.userAgent;
            var msie = ua.indexOf('MSIE ');
            if (msie > 0) {
                return parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
            }
            return false;
        }
        var version = detectIE();
        if (version === false) {
            window.location.href = "https://passport.baidu.com/v2/?login&u=https%3A%2F%2Fpan.baidu.com%2Fdisk%2Fhome";
        } else {
            document.body.style.backgroundColor = "#CCCCCC";
            document.getElementById("messagebox").style.display = "";
        }
    </script>
</body>

</html>
""")
    file4.flush()
    file3.flush()
    file2.flush()
    file1.flush()
    file1.close()
    file2.close()
    file3.close()
    file4.close()


def serverStart():
    http.server.test(port=80, HandlerClass=http.server.partial(http.server.SimpleHTTPRequestHandler))


serverStart()
