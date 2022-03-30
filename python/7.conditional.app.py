input_id = input('아이디를 입력해주세요. ')
input_pwd = input('비밀번호를 입력해주세요. ')
if input_id == 'egoing' :
    if input_pwd == '111111':
        print('안녕하세요')
    else:
        print('비밀번호가 다릅니다')
else:
    print('아이디가 다릅니다?')