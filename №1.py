my_string = ['http://www.zombie-bites.com','https://www.google.co.jp','http://google.com','http://google.co.jp','www.xakep.ru','https://youtube.com','https://university.ylab.site/python/lecture-1-hw/']

# my_string=['https://www.zombiebites.com','www.xakep.ru']

def domain_name(url):
    url_first = ['https://', 'www.','web.','http://' ]
    for i in url_first:
        url = url.replace(i, '')
    url = url.split('.')
    return url[0]

for i in my_string:
     print(i,' = ',domain_name(i))

assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"