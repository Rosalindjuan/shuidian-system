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
    
    
#公众号测试配置
##1. 设置公众号
- 接口配置域名及token
```
URL     http://debug.join-clima.com/wechat
Token   123456
```
- JS安全域名
```
域名     join-clima.com
```
- 网页授权回调域名
```
域名     debug.join-clima.com
```
    
##2. 设置配置文件join.yaml中的wechat配置
```
wechat:
  appid: 'wxf6b77f2ddcab675f'
  secret: 'cfeffa66a1ec353142041cc102aefb28'
  token: '123456'

```
如果需要cdn时将join.yaml中的cdn里面的host替换成自己的cdn；process_env为false时就是不使用cdn，true时使用cdn；
在webpack.prod.js文件里的publicPath需要手动改成cdn的路径。


##3. 创建公众号菜单
[创建菜单链接](https://mp.weixin.qq.com/debug/cgi-bin/apiinfo?t=index&type=%E8%87%AA%E5%AE%9A%E4%B9%89%E8%8F%9C%E5%8D%95&form=%E8%87%AA%E5%AE%9A%E4%B9%89%E8%8F%9C%E5%8D%95%E5%88%9B%E5%BB%BA%E6%8E%A5%E5%8F%A3%20/menu/create)

菜单的编码如下：
```
{
    "button": [
        {
            "type": "view",
            "name": "主页",
            "url": "http://debug.join-clima.com"
        },
        {
            "name": "调试",
            "sub_button": [
                {
                    "type": "view",
                    "name": "登出",
                    "url": "http://debug.join-clima.com/signout"
                },
                {
                    "type": "view",
                    "name": "jsapi demo",
                    "url": "http://debug.join-clima.com/wxjs"
                }
            ]
        }
    ]
}
```
    
    
