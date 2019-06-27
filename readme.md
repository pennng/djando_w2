本次将分享MTV模式的实践 - 除法运算

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
写函数 In models.py
```python
def get_current_time():

    now = datetime.now().timestamp()

    return now

```

如有需要，迭代测试与模型

## 3. 创建前端模板
