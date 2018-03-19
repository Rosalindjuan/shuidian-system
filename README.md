#app (pulsar for aiohttp)

this is application for lot, in wechat.

###aioredis安装1.00b1版本
```
# cd aioredis
# pip install .
```

安装本地模块：
```
git clone ssh://git@ph.join-clima.com/diffusion/STORE/join-store.git store
git clone ssh://git@ph.join-clima.com/diffusion/PARSER/join-parser.git parser
```

#Installation

1. Install the pyenv, python3.6.0, packages

    https://github.com/yyuu/pyenv
    https://github.com/yyuu/pyenv-virtualenv

    ```
    $pyenv install 3.6.0
    $pyenv virtualenv 3.6.0 pulsar-env
    $pip install -r requirements.txt
    ```


2. Install database for your project
    ```
    $port install redis
    $port install mongodb
    ```

3. Run application
    ```
    $python run.py
    $python aiohttp_server.py
    ```

4. Open browser

    http://localhost:8060/

5. Run integration tests
    ```
    $pip install tox
    $tox
    ```


#Pycharm

1. Debug
    ```
    $python /Applications/PyCharm.app/Contents/helpers/pydev/setup_cython.py build_ext --inplace
    ```
2. 直达目录的快捷键

    Command + Shift + g
    
    
    
# mongoDB
1. 更新文档
```
db.users.update({'is_active':false},{$set:{'is_active':true}},{multi:true})
```
    