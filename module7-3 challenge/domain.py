url = input('Enter the URL: \n')
accepted = ['https://www.','http://www.']
if url[:11] == accepted[1]:
    split_url = url.split('.')
    split_url[0] = accepted[0]
    url = '.'.join(split_url)
while url[:12] not in accepted:
    print('urls begin with http://www.')
    url = input('Enter the URL: \n')
print(f'The domain is {(url.split('.')[-1]).upper()}')