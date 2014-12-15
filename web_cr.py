# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://google.com">')
start_link = page.find('<a href=')
find1 =  page.find('"',start_link)

find2 = page.find('"',find1+1)
print find1
print find2

url =  page[find1+1:find2]
print url
