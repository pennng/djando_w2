本次将分享MTV模式的实践 - 时间显示

## 1. 克隆远程代码
上次结束时的代码
```bash
git clone https://github.com/pennng/djando_w2

```

## 2. Test Driven Development (TDD) 后端开发
撰写测试用例, 允许五秒误差 In tests.py  
```python
from django.test import TestCase
from . import models
from datetime import datetime

class MyTests(TestCase):

    def test_time(self):
        now = datetime.now().timestamp()
        self.assertLess(abs(now - models.get_current_time()), 5)
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

## 3. 创建前端模板
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

## 4. 创建视图
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

## 运行查看效果
```bash
python manage.py runserver
```