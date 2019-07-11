## WK3-MQTT
### 1. 安装
```bash
pip install paho-mqtt
```

### 2. 关注一个主题
```python
import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("tem")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.payload)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("35.246.79.248", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
```

### 3. 发送数据
```python
i = client.publish("topic", 'your msg')
```

## WK2-Django MTV模式的实践 - 时间显示  
### 1. 克隆远程代码
上次结束时的代码
```bash
git clone https://github.com/pennng/djando_w2

```

### 2. "M" Test Driven Development (TDD) 后端开发
撰写测试用例, 允许2秒误差 In tests.py  
```python
from django.test import TestCase
from . import models
from datetime import datetime

class MyTests(TestCase):
    def test_time(self):
        now = datetime.now().timestamp()
        self.assertLess(abs(now - models.get_current_time()), 2)
```
运行测试
```bash
python manage.py test polls
```
写函数 In models.py
```python
def get_current_time():

    now = datetime.now().timestamp()

    return now

```
再次运行测试时成果。如有需要，迭代测试与模型

### 3. "T" 创建前端模板
在polls目录下创建文件夹 /templates
新建模版文件 time.html
```html
<html>
<head>
    <title>Time</title>
</head>
<body>
    <h1>Current time: {{time}}</h1>
</body>
</html>
```
在/mysite/setting.py文件里配置模版目录，TEMPLATES "DIRS"里添加
添加
```python
            BASE_DIR + "/polls/templates"
```

### 4. "V" 创建视图
在views.py
```python
from django.shortcuts import render
from . import models

def time(request):
    context = {
        "time": models.get_current_time()
    }
    return render(request, 'time.html', context)
```

在urls.py, urlpattens添加
```python
    path('time', views.time, name = 'time')
```

### 运行查看效果
```bash
python manage.py runserver
```