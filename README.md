google-ip-explorer
==================

由于最近GFW姨妈来得比较频繁, 所以写了个小工具. 这工具能够找出可用的Google IP地址.

## 教程

[Google IP Explorer](https://github.com/PeerXu/google-ip-explorer)是一个查找Google IP列表的工具. 可以单独使用, 也可以配合Goagent使用.

如果已经安装了gevent库, 那么可以大大地增加查找速度.

    $ git clone https://github.com/PeerXu/google-ip-explorer.git
    $ cd google-ip-explorer
    $ python google.py input.txt

Google IP列表就在output.txt文件中.

如果你需要直接使用, 那么就挑一个IP直接在浏览器里面就能使用了.

如果你需要和Goagent配合使用的话, 那么就将```proxy.ini``` 下的```[iplist]``` 下的```google_cn``` 和 ```google_hk``` 替换为output.txt的内容就可以了~
