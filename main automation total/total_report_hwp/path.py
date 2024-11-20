import json
############################## 경로 수정 필요
# JSON 파일 경로
CONFIG_FILE = r"C:\Users\wikky\Documents\SWeat auto distribution\config.json"

# JSON 파일 로드
with open(CONFIG_FILE, 'r', encoding='utf-8') as file:
    config = json.load(file)

# 설정 값 가져오기
API_PATH = config["API_PATH"]
IMAGE_PATH = config["IMAGE_PATH"]
DRIVE_PATH = config["DRIVE_PATH"]
SAVE_PATH = config["SAVE_PATH"]
SPREAD_PATH = config["SPREAD_PATH"]
WORK1_PATH = config["WORK1_PATH"]
WORK2_PATH = config["WORK2_PATH"]
FORM_PATH_P = config["FORM_PATH_P"]

# 함수로 경로 생성
def FORM_PATH_R(n):
    return config["FORM_PATH_R"].format(n=n)