import total_report_hwp as th
"""
(Start = None, end = None이면 전체 보고서)
(Start = 1, end = 1 이면 1번째 행 보고서)
(Start = 1, end = 3 이면 1~3번째 행 보고서)
(activate_r 값이 1이면 report total 활성화 0이면 report total비활성화 / activate_i도 동일)
"""
#############################################
start, end = th.range(None,None)
activate_r, activate_i = 1, 1
#############################################

# 드라이브에서 데이터 불러오는 함수
dt1 = th.drive_txt1()  # 설문지 텍스트
dt2 = th.drive_txt2()  # 기본 정보 텍스트
di = th.drive_images(dt1, start, end) # 이미지 데이터
th.open_hwp

for index, row in dt1.iloc[start:end].iterrows():
    th.report_total(row, index, di, dt2, activate_r)  # 튜터링 보고서 생성
    th.iamge_total(row, index, di, dt2, activate_i)  # 사진 보고서 생성
    th.image_del(index, di)  # 로컬에 설치한 이미지 삭제