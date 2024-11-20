path.py 본인 경로에 맞게 수정

-----가상환경 생성
python -m venv [가상환경이름:venv 권장]
venv\Scripts\activate (가상환경 실행)

-----구글 클라우드 플랫폼에서 
서비스 계정생성, 이후 json 파일 설치 -> 이름 API.json으로 변경
OAuth 2.0 클라이언트 아이디 생성, 이후 json 파일 설치 -> 이름 client_secrets.json으로 변경

-----한글 오류 표시 제거
https://employeecoding.tistory.com/67 

-----필요 라이브러리 설치법
pip install pipreqs
pipreqs .
pip install -r requirements.txt