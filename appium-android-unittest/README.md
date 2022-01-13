# appium for android + unittest

# 安装

## 依赖

```shell
pip install Appium-Python-Client Selenium unittest
```

## appium
```shell
npm config set registry https://registry.npm.taobao.org
npm install appium -g
npm install appium-doctor -g 
appium-doctor
```


# 启动appium-server
```
appium -p 4723 -bp 4724 --webdriveragent-port 8100
```

# 运行脚本

```shell
cd appium-android-unittest
```

```shell
python run.py
```


# 目录说明

* apk文件夹
* test_report
存放每次执行测试后，生成的测试报告。
* testcase
存放测试用例脚本（以test开头unittest单元测试脚本）

# appium capability 参数


# 参考

[unittest](https://docs.python.org/zh-cn/3/library/unittest.html)
[appium capability](http://appium.io/docs/cn/writing-running-appium/caps/)

