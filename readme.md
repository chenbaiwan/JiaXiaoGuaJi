# 厦门地区驾校理论时间挂机

## 提供两种使用方式

仅限厦门地区<http://www.jppt.com.cn>

### 1、谷歌浏览器 + [postman插件](https://chrome.google.com/webstore/detail/postman-rest-client-short/mkhojklkhkdaghjjfdnphfphiaiohkef?utm_source=chrome-ntp-icon)

安装postman && 导入[驾校挂机.json](https://raw.githubusercontent.com/chenbaiwan/JiaXiaoGuaJi/master/%E9%A9%BE%E6%A0%A1%E6%8C%82%E6%9C%BA.json)

*我试了下用url导入好像没有成功，那就下载到本地从文件导入吧～*

**登录 -> 开始挂机 -> (挂机....) -> 保存进度 -> 退出登录**

### 2、python + [requests模块](http://docs.python-requests.org/en/latest/)

修改`account.txt`中的账号密码

	python guaji.py
