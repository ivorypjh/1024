# 데이터 크롤링을 하는 과정에서 '검색 서비스 이용이 제한되었습니다. 
# </h3> <div class="info"> 사용 중이신 PC 또는 네트워크에서 네이버의 안정적인 
# 검색 서비스를 방해하는 내용이 감지되었습니다.' 라는 에러가 발생

# 여기에 대한 오류 수정 내용


# 크롤링을 하는 과정에서 사용자의 애플리케이션과 headers의 입력 사항이 맞지 않았고 
# 요청 header 의 내용이 잘못 되어서 오류가 발생한 것으로 보임
# headers 의 내용을 아래와 같이 수정해서 요청을 하면 발생한 오류를 해결
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
'Referer': 'http://www.naver.com/',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'}