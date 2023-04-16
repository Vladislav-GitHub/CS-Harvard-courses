s = input('File name: ').lower().strip().split('.') # s = image.gif s = ['image', 'gif']
try:
    if s[-1] == 'gif':
        print('image/gif')
    elif s[-1] == 'jpg':
        print('image/jpg')
    elif s[-1] == 'jpeg':
        print('image/jpeg')
    elif s[-1] == 'png':
        print('image/png')
    elif s[-1] == 'pdf':
        print('application/pdf')
    elif s[-1] == 'txt':
        print('text/' + s[0])
    elif s[-1] == 'zip':
        print('application/zip')
    else:
        print('application/octet-stream')
except IndexError:
    print('application/octet-stream')