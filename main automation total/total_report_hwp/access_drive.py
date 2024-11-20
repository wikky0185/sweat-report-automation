import os
from google.oauth2 import service_account
import gspread
from googleapiclient.discovery import build
from gspread_dataframe import get_as_dataframe
from total_report_hwp.path import API_PATH, IMAGE_PATH, DRIVE_PATH, SPREAD_PATH, WORK1_PATH, WORK2_PATH


########인증
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'] # 인증 범위 설정
credentials = service_account.Credentials.from_service_account_file(API_PATH, scopes=SCOPES)  # 서비스 계정 인증 설정
gc = gspread.authorize(credentials) # Google Sheets 인증 설정 (gspread)
drive_service = build('drive', 'v3', credentials=credentials) # Google Drive API 인증 설정

# Google Drive에서 이미지 다운로드 함수
# Google Drive에서 이미지 다운로드
def drive_images(dt1, start_row=None, end_row=None): 
    # 슬라이싱된 데이터 가져오기
    sliced_dt1 = dt1.iloc[start_row:end_row] if start_row is not None or end_row is not None else dt1
    
    # 슬라이싱된 데이터에서 인덱스 가져오기
    matching_indices = sliced_dt1.index.tolist()

    if not matching_indices:
        print(f"지정된 범위 {start_row}-{end_row}에서 데이터가 없습니다.")
        return {}

    # 드라이브에서 폴더 목록 가져오기
    subfolders = drive_service.files().list(
        q=f"'{DRIVE_PATH}' in parents and mimeType = 'application/vnd.google-apps.folder'",
        fields='files(id, name)'
    ).execute().get('files', [])
    
    sorted_subfolders = sorted(subfolders, key=lambda x: x['name'])
    folder_images = {}

    for idx in matching_indices:
        if idx < len(sorted_subfolders):  # 인덱스 범위 확인
            subfolder = sorted_subfolders[idx]  # 해당 인덱스의 폴더 선택
            print(f"폴더 불러오는 중 : {subfolder['name']}")
            
            # 폴더 내 이미지 처리
            image_files = drive_service.files().list(
                q=f"'{subfolder['id']}' in parents and mimeType contains 'image/png'",
                fields='files(id, name)'
            ).execute().get('files', [])
            
            image_paths = []
            if len(image_files) >= 4:
                for i, file in enumerate(image_files[:4]):
                    file_path = os.path.join(IMAGE_PATH, f"{subfolder['name']}_image_{i+1}.png")
                    request = drive_service.files().get_media(fileId=file['id'])
                    with open(file_path, 'wb') as f:
                        f.write(request.execute())
                    image_paths.append(file_path)
                folder_images[subfolder['name']] = image_paths
            else:
                print(f"폴더 {subfolder['name']} 내에 이미지가 4장 미만입니다.")
        else:
            print(f"인덱스 {idx}가 범위를 초과하여 처리되지 않았습니다.")
    
    return folder_images


# 구글 스프레드시트에서 데이터 가져오기
def drive_txt1():
    # 스프레드시트 열기
    spreadsheet = gc.open(SPREAD_PATH)
    
    # 첫 번째 시트 가져오기
    worksheet1 = spreadsheet.worksheet(WORK1_PATH)  # 첫 번째 시트 이름
    df1 = get_as_dataframe(worksheet1)

    return df1

def drive_txt2():
    # 스프레드시트 열기
    spreadsheet = gc.open(SPREAD_PATH)
    
    # 두 번째 시트 가져오기
    worksheet2 = spreadsheet.worksheet(WORK2_PATH)  # 두 번째 시트 이름
    df2 = get_as_dataframe(worksheet2)

    return df2


