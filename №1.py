my_string = ['http://www.google.co.jp','http://google.com','http://google.co.jp','www.xakep.ru','https://youtube.com','https://university.ylab.site/python/lecture-1-hw/']


def domain_name(url):
    if '//' in url:
        url=url.split('/')[2]
    elif 'www' or 'web' in url:
        return url.split('.')[1]
    if url.count('.')>=2:
        return url.split('.')[-3]
    return url.split('.')[-2]

for i in my_string:
    print(i,' = ',domain_name(i))

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
