link = input('Enter your link :')
link = link.replace('https://', "")
link=link.replace('www.', '')
value_of_start = link.rfind('/')
print(link[:value_of_start])
