# spider
这是一个爬虫程序，可以按关键词抓取国自然基金项目检索结果并存储为csv格式。

![image-20211008110256861](https://tva1.sinaimg.cn/large/008i3skNgy1gv7q1lj9ilj60wz0u042i02.jpg)

### Python+selenium使用cookie登录

由于网站需要用户登陆才能翻页，所以需要添加cookie。手动复制cookie很不方便，这里可以使用一个chrome插件：EditThisCookie

![image-20211008110645162](https://tva1.sinaimg.cn/large/008i3skNgy1gv7q5iatu1j60g40hx3zs02.jpg)

插件有导出功能，可以得到一个list，稍加修改就能变为python支持的格式。

![image-20211008111021481](https://tva1.sinaimg.cn/large/008i3skNgy1gv7q9a92e2j60ch0lddgz02.jpg)

