# 'https://www.zhipin.com/c100010000/?query=%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%BC%80%E5%8F%91&page=2&ka=page-2'
# 'https://www.zhipin.com/c100010000/?query=%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%BC%80%E5%8F%91&page=1&ka=page-2'


class WebCrawler:
    def __init__(self, job):
        pass


# 职位
jobs = ['大数据开发']
db_name = ['BigDataDevelopment']
for i in range(len(jobs)):
    job = jobs[i]
    a = WebCrawler(job)

    # 保存数据
