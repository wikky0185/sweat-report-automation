import total_report_hwp as th

# (출력 행의 범위 지정해서 출력 index 0부터 시작)
# (만약 0번째 데이터만 출력 start=0, end=1)
############################################# (Start = 0, end = 1 이면 0번째행 부터 1번째행 이전까지)
start, end = None, None  # 시작 행 (None이면 처음부터), 끝 행 (None이면 끝까지)
############################################# 

# 드라이브에서 데이터 불러오는 함수
dt1 = th.drive_txt1()  # 설문지 텍스트
dt2 = th.drive_txt2()  # 기본 정보 텍스트
di = th.drive_images(dt1, start, end) # 이미지 데이터
th.open_hwp

for index, row in dt1.iloc[start:end].iterrows():
    th.report_total(row, index, di, dt2)  # 튜터링 보고서 생성
    th.picture_total(row, index, di, dt2)  # 사진 보고서 생성
    th.image_del(index, di)  # 로컬에 설치한 이미지 삭제