# coding:utf-8
import urllib.request


class HtmlOuter(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        x = 1
        for data in self.datas:
            for d in data:
                print(d)
                print(x)
                urllib.request.urlretrieve(d, 'D:\\img\\' + str(x) + '.jpg')
                x = x + 1
