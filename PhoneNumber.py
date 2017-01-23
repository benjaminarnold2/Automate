def isPhone(text):

    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):

        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

message = 'here is some text 123-123-1234 and some more text 123-123-1234. This is the end of the text 123-123-1234.'

for i in range(len(message)):

    chunk = message[i:i+12]
    if isPhone(chunk):
        print('Found number: ' + chunk)
