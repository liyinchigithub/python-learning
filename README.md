# python-learning

# 环境配置

>安装python、pip

# 更新pip

```python
pip install --upgrade pip
```

# python依赖管理

* Java可以通过Maven(pom.xml)、Gradle(build.gradle)来管理依赖。
* Nodejs通过npm(package.json)来管理第三方插件。
* Python通过Virtualenv(requirements.txt)、Pipenv、Conda这三种来管理第三方库。

## 依赖管理要解决的问题：
当多个项目需要使用不同的第三方库时就会出现这样的问题,例如：
A项目开发的比较早使用的是Python2.7版本，该项目使用的第三方依赖也是比较低的版本；
B项目是后来开发的使用Python最新版本Python3.8以及目前最新的版本的相关依赖。
这时就要配置每个项目使用的每个第三方库对应的版本号。
依赖管理就是配置每个项目使用了哪些第三方库以及这些第三放库对应的版本号。


## Virtualenv（requirements.txt）

Virtualenv(virtual environment) : 

虚拟环境解决的办法是为每个项目创建一套独立的环境，各自项目使用各自的环境，这样每个项目的第三方库就互不影响了。 每套环境包含Python具体的环境（如Python3.8）以及需要安装的第三方库。 创建好虚拟环境然后指定当前项目对应的虚拟环境就行了， 这样项目所使用的依赖只需要去各自的虚拟环境venv/lib目录下找就行了。

>备注：使用PyCharm创建项目时会让你先选择依赖管理，选择Virtualenv，项目创建完后会自动创建一个venv目录。可以点击的Terminal来激活当前虚拟环境，通过pip来安装第三方依赖。

### 创建虚拟目录

```shell
# python -m venv 虚拟环境名称，名称是随意起的
python -m venv tutorial-env
```
### 激活虚拟环境
当激活虚拟环境时命令行上会有个虚拟环境名前缀。

#### Unix或MacOS上激活虚拟环境
```shell
source tutorial-env/bin/activate
```
#### windows上激活虚拟环境
```shell
tutorial-env\Scripts\activate.bat
```

### Virtualenv的缺点
* 如果安装新的第三方库或者更新的版本号都要手动执行pip freeze > requirements.txt比较麻烦，可能造成忘记更新requirements.txt文件。
* requirements.txt会记录安装的第三方库所依赖的第三方库。
* Virtualenv会在项目中生成一个venv目录，venv包含了所有第三方库及Python环境，会造成项目比较大。


#### 冻结第三方库，就是将所有第三方库及版本号保存到requirements.txt文本文件中
```shell
pip freeze > requirements.txt
```


### 单元测试

* pytest
```shell
pytest

* unittest
```shell
python -m unittest -v test52_unittest01.py
```