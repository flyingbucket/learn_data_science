# IPython简介
1.IPython是什么？
   
IPython是一个交互式Python环境，它提供了一个类似于Matlab或R的命令行界面，可以方便地执行代码并查看运行结果。
它还支持代码自动补全、代码高亮、对象信息查看、命令历史记录、内置命令和扩展功能等功能。

2.docstring是什么？

docstring（文档字符串）是Python中用来描述函数、模块、类等对象的字符串。
它是用三引号（"""）括起来的一段话，描述了该对象（函数、模块、类等）的功能、使用方法、注意事项等。   
在Python中，docstring可以用函数的__doc__属性来访问，也可以用help()函数查看。
eg.
```python
def my_function():
    """This is a docstring for my_function."""
    pass

print(my_function.__doc__)  # This is a docstring for my_function.
help(my_function)  # This is a docstring for my_function.   
```

3.如何安装IPython？

IPython可以直接从Python Package Index（PyPI）安装，命令如下：
``` 
pip install ipython
```
安装成功后，在命令行中输入ipython，即可进入IPython环境。

4.IPythony会被pip安装在哪里？

IPython会被安装在Python安装目录的Scripts目录下，具体路径如下：
```
C:\Users\username\AppData\Local\Programs\Python\Python37\Scripts
```
此路径只是一个例子，具体路径可能因系统而异。
如果安装路径中没有Scripts目录，可以手动创建。

如果在虚拟环境中运行IPython，则IPython会被安装在虚拟环境的Scripts目录下。
如果虚拟环境下没有Iphthon，也不用担心，可以直接在全局环境中安装IPython，然后在虚拟环境中激活即可，激活命令如下：
```
activate myenv
```
激活成功后，在命令行中输入ipython，即可进入IPython环境。