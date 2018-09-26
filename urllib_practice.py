import urllib3
import certifi
import xlwt
import io
from urllib.parse import urlencode
from lxml import html
from lxml import etree

def parse_file(fileStr):
    parser = etree.HTMLParser(encoding="utf-8")
    dom_tree = etree.parse(fileStr,parser)
    html_text = etree.tostring(dom_tree, encoding="utf-8").decode("utf-8")
    tree = html.fromstring(html_text)

    comment_users = tree.xpath("//div//span[@class='comment-info']//a")
    comment_times = tree.xpath("//div//span[@class='comment-time ']") #获取评论时间
    comment_texts = tree.xpath("//div//span[@class='short']")  #获取评论

    comments_excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
    table = comments_excel.add_sheet('comments',cell_overwrite_ok=True)


    table.write(0,0,"用户名")
    table.write(0,1,"评论时间")
    table.write(0,2,"评论")
    i = 1
    for user in comment_users:
        table.write(i,0,user.text)
        i+=1
    i = 1
    for txt in comment_times:
        table.write(i,1,txt.text)
        i+=1
    i = 1
    for com in comment_texts:
        table.write(i,2,com.text)
        i+=1
    comments_excel.save(r'comments.xls')

# 获取请求路径
def get_url(start,limit,sort='new_score',status = 'p',percent_type = 'h'):
     data = {'start': start, 'limit': limit, 'sort': sort, 'status': status, 'percent_type': percent_type}
     encoded_args = urlencode(data)
     prefix = 'https://movie.douban.com/subject/26985127/comments?'
     url = prefix + encoded_args
     return url

# 获取数据保存文件
def get_data_to_file(url):
     http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
     req = http.request('POST',url)
     fileStr = "data.html"
     dataFile = open(fileStr,"wb")
     if req.status == 200:
         with dataFile as f:
              f.write(req.data)
         return fileStr
     else:
         return False

     
def main():
    url = get_url(0,20)
    fileStr = get_data_to_file(url)
    if fileStr!=False:
        parse_file(fileStr)

main()





# str1 = "https://movie.douban.com/subject/26985127/comments?start=0&limit=20&sort=new_score&status=P&percent_type=h"
# str2 = "https://movie.douban.com/subject/26985127/comments?start=20&limit=20&sort=new_score&status=P&percent_type=h"