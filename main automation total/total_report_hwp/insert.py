import pandas as pd
import os
from total_report_hwp.path import SAVE_PATH

def sel_work2(row, dt2):
    school_name = row['수업학교']
    matching_row = dt2[dt2['선택지'] == school_name]
    base = matching_row.iloc[0]
    
    return base

################################################ (이미지)

def images_r(hwp, image_paths):# 이미지 삽입 함수 (튜터링 보고서)
    hwp.InsertPicture(image_paths[0], True, 1, False, False, 0, 90, 60)
    hwp.InsertPicture(image_paths[1], True, 1, False, False, 0, 90, 60)

def images_p(hwp, image_paths):  # 이미지 삽입 함수 (사진 보고서)
    for i, image_path in enumerate(image_paths[:4]):
        hwp.InsertPicture(image_path, True, 1, False, False, 0, 90, 75)
        hwp.MovePos(101)

############################################### (텍스트)

def txt_r(hwp, row, base): # 텍스트 삽입 함수 (튜터링 보고서)
    hwp.PutFieldText("주차", row["주차"])
    hwp.PutFieldText("수업방법", row["수업방법"])
    hwp.PutFieldText("학교", base["학교"])
    hwp.PutFieldText("수업장소", base["주소"]+"("+(base["학년반"])+")")
    hwp.PutFieldText("시작시간", base[row["주차"]]+base["시작시간"])
    hwp.PutFieldText("종료시간", base[row["주차"]]+base["종료시간"])
    hwp.PutFieldText("학년반1", base["학년반"])

    for tutor_num in range(1, 5):
        if pd.notna(row.get(f"튜터{tutor_num}")):
            hwp.PutFieldText(f"튜터{tutor_num}시간", base["시간"])
            hwp.PutFieldText(f"튜터{tutor_num}", row[f"튜터{tutor_num}"])
            hwp.PutFieldText(f"튜터{tutor_num}구분", row[f"튜터{tutor_num}구분"])
            hwp.PutFieldText(f"튜터{tutor_num}내용", row[f"튜터{tutor_num}내용"])

    hwp.PutFieldText("튜터링경과", row["튜터링경과"])
    hwp.PutFieldText("준비", row["준비"])

def txt_p(hwp, row, base):# 텍스트 삽입 함수 (사진 보고서)
    hwp.PutFieldText("학교", base["학교"])
    hwp.PutFieldText("학년반", base["학년반"])
    hwp.PutFieldText("이름", base["반짱"])
    hwp.PutFieldText("연락처", base["연락처"])
    hwp.PutFieldText("주소", base["주소"] + " "+base["학교"] + " "+ base["학년반"])
    hwp.PutFieldText("인원", row["인원"])
    hwp.PutFieldText("세부내용", row["세부내용"])
    hwp.PutFieldText("날짜", base[row["주차"]])
    hwp.PutFieldText("시간", base["시간"])

############################################### (파일 저장 이름)

def save_name_r(hwp,row,base): # 파일 이름 설정 (튜터링보고서)
    #파일 이름 지정  
    school = base["학교"]
    grade_class = base["학년반"]
    week = row["주차"]
    file_name = f"[{school} ({grade_class}) {week}]SWeat 튜터링 보고서.hwp" 
    save_path = os.path.join(SAVE_PATH, file_name)

    # 파일 저장
    hwp.SaveAs(save_path)
    print(f"saved {save_path}")

def save_name_p(hwp,row,base): # 파일 이름 설정 (사진보고서)
    school = base["학교"]         
    grade_class = base["학년반"]
    week = row["주차"]
    file_name = f"[{school} ({grade_class}) {week}] 지역사회봉사단 자원봉사활동 사진 보고서.hwp"
    save_path = os.path.join(SAVE_PATH, file_name)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # 파일 저장 및 종료
    hwp.SaveAs(save_path)
    print(f"saved {save_path}")

