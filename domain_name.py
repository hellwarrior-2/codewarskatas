#Exercise 5kyu
#Extract the domain name from a URL
#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

#domain_name("http://github.com/carbonfive/raygun") == "github" 
#domain_name("http://www.zombie-bites.com") == "zombie-bites"
#domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
  ans = url.replace('http://', '')
  ans = ans.replace('https://', '')
  ans = ans.replace('www.', '')  
  i = ans.split('.', 1)[0]
  return  i  

#tests cases
print(domain_name("http://google.com")) #return "google"
print(domain_name("http://google.co.jp")) #return "google"
print(domain_name("www.xakep.ru")) #return "xakep"
print(domain_name("https://youtube.com")) #return "youtube"