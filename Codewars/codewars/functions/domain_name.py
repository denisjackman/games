def domain_name(url):
    if url == None:
        return url
    from urlparse import urlparse
    if url.find("http") == -1:
        temp = url
    else:
        temp = urlparse(url).hostname
    nutemp = temp.split(".")
    if nutemp[0] == "www":
        return nutemp[1]
    else:
        return nutemp[0]

print domain_name("http://github.com/carbonfive/raygun") == "github"
print domain_name("http://www.zombie-bites.com") == "zombie-bites"
print domain_name("https://www.cnet.com") == "cnet"
print domain_name("https://google")
print domain_name("www.fatcat.ro")

'''
Test.describe("Basic tests")
Test.assert_equals(domain_name("http://github.com/carbonfive/raygun"), "github")
Test.assert_equals(domain_name("http://www.zombie-bites.com"), "zombie-bites"")
Test.assert_equals(domain_name("https://www.cnet.com"),"cnet")
Test.assert_equals(domain_name("www.fatcat.ro"),"fatcat")
'''