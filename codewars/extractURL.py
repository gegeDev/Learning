def domain_name(url):
    if url.startswith("http"): url = url[url.index("/") + 2:]
    if url.startswith("www."): url = url[url.index(".") + 1:]
    return(url[:url.index(".")])
    
print(domain_name("https://www.google.com.pl"))
print(domain_name("www.google.com.pl"))
print(domain_name("http://google.com.pl"))
