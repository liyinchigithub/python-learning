# appium for android + unittest

# 安装

## 依赖

```shell
pip install requirement.txt
```

## appium
```shell
npm config set registry https://registry.npm.taobao.org
npm install selenium
```



# 运行脚本

```shell
cd selenium-pytest
```

## 运行指定标志的用例
```shell
pytest -m baidu
```

## 运行所有用例
```shell
pytest
```

```shell
pytest -v -m "指定标志"
```
-v 控制台详细输出

# 目录说明

* download_file
下载文件存放路径，通过chromeOptions capability设置
* save_images
selenium 截图保存图片路径
* conftest
初始化
* conftest
存放测试用例脚本（以test开头unittest单元测试脚本）

# selenium chrome options、capability

>hhttps://www.cnblogs.com/guapitomjoy/p/12150416.html

>https://www.cnblogs.com/clement-jiao/p/10889234.html
