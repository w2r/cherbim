# cherbim


### 此教程仅适用于安卓系统

#### 操作步骤：

##### 1. 下载tasker 破解版

自己百度搜索下载 ，便捷食用链接：https://drive.google.com/file/d/1VqJcsUactP-x6l3nKXoQPhQFCUlOnFnv/view?usp=sharing

##### 2. 申请tg机器人

第一步：Telegram上关注botfather，申请一个bot(机器人)。关注之后发送`/newbot`创建新bot，起个好听的名字，之后会让你再起个username，最后你会得到bot api，然后记得关注这个机器人

第二步：关注`userinfobot`获得自己的id

第三步：测试是否收到短信，把前面获得的api和id替换到下方链接中，格式一定要和链接中格式一样的                                                                                         

```
https://api.telegram.org/bot703106170:AAE2RJ57xjVsX6mRVqJiqZk_wilfC7fCgtg/sendMessage?chat_id=561661782&text=你好
```

第四部：浏览器输入以上网址，这时tg机器人会收到“你好”内容，若不出现内容，大概率是api和id不对

##### 3. 配置tasker

第一步：新建配置文件，事件，筛选器，搜索短信，选择接收短信（记得给短信权限）

第二步：点击新建的配置文件，新建任务，命名，点+号，筛选器搜索JavaScriptlet，代码部分如下：

```
var SMS=global('SMSRB');
var url="https://api.telegram.org/bot703106170:AAE2RJ57xjVsX6mRVqJiqZk_wilfC7fCgtg/sendMessage?chat_id=561661782&text="+SMS;
var method = "GET" ;// or"POST"/"PUT"/"DELETE"
var xhttp = new XMLHttpRequest();
xhttp.open( method, url, false );
xhttp.send(); //if method was"POST", put info in the () here
if( xhttp.status == 200 ) { //successfulhttp request
var response = xhttp.responseText; }
```

URL部分要改成你自己测试成功的链接，然后其他部分不用改动

**大功告成！**


