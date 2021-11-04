import time
import requests
import re
import pandas as pd

nameList = []


class QCC(object):
    """企查查爬虫"""

    def __init__(self):
        self._headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        }

    def get_cookie(self):
        """发起一次测试请求，获取到搜索的cookie"""
        url = 'https://www.qcc.com/web/search/risk?key=测试'
        response = requests.get(url, headers=self._headers, allow_redirects=False)
        response.encoding = 'utf8'
        result = re.findall(r'div>您的请求ID是: <strong>\n(.*?)</strong></div>', response.text)
        if result:
            return result[0]

    def search(self, search_keyword):
        """搜索"""
        url = 'https://www.qcc.com/web/search/risk?key={}'.format(search_keyword)
        headers = self._headers
        headers['cookie'] = 'acw_tc={}'.format(self.get_cookie())
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        tmp = re.findall(r'(.*?)条\n', response.text)
        for item in tmp:
            tmp_result = re.findall(r'\d+', item)
            nameList.append(tmp_result[0])

    def run(self, str):
        """启动函数"""
        self.search(search_keyword=str)


if __name__ == '__main__':
    file = 'temp.xlsx'
    sheet = pd.read_excel(file)
    df = pd.DataFrame(sheet)
    l = len(df['name'])
    for i in range(l):
        try:
            if i > 0 and df['name'][i] == df['name'][i - 1]:
                pass
            else:
                nameList = []
                t = QCC()
                t.run(df['name'][i])
            print(df['name'][i], end=' ')
            for item in nameList:
                print(item, end=' ')
            print("")
            time.sleep(1)
        except:
            time.sleep(1)
        continue
