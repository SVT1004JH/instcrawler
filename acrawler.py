import requests
import json
import urllib.request
import os
def crawler(base_url):
    a = requests.get(base_url)

    b = json.loads(a.text) #a를 문자열 딕셔너리로 바꿈

    while True:
        # 다 찾게 되어 비어있는 리스트가 나왔을 경우
        if b['items'] == []:
            break # 프로그램 종료

        # min_id 갱신
        min_id = b['items'][-1]['id']
        for c in b['items'] :
            if 'videos' in c.keys() : #c의 key값에 'videos'가 있을 때
                print(c['videos']['standard_resolution']['url'])#여기에 영상 링크 있음
                urllib.request.urlretrieve(c['videos']['standard_resolution']['url'] , filename = c['videos']['standard_resolution']['url'].split('?')[0].split('/')[-1])#영상저장

            else :
                print(c['images']['standard_resolution']['url']) # 여기에 이미지 링크 있음
                urllib.request.urlretrieve(c['images']['standard_resolution']['url'], filename = c['images']['standard_resolution']['url'].split('?')[0].split('/')[-1])#사진저장

        # min_id 이용해서 url 업데이터
        url = base_url + '?max_id=' + min_id

        # 업데이트 된 url에 접속
        a = requests.get(url)

        # 가져온 json 데이터 보내기
        b = json.loads(a.text)


if __name__ == '__main__':
    u = input("인스타 아이디 : ") #원하는 주소 입력
    base_url = "https://www.instagram.com/"+u+"/media/"

    p = input("원하는 폴더 : ") #원하는 폴더를 받음
    os.chdir(p)

    crawler(base_url)
