import total_report_hwp as th
import os

def report_total(row, index, di, dt2, act_r):
    if act_r == 1:
        image_paths = di[list(di.keys())[index % len(di)]] 
        base = th.sel_work2(row, dt2) 
        sel_f = th.sel_form(row)
        hwp = th.open_hwp(sel_f) 
        th.txt_r(hwp,row,base) 
        th.images_r(hwp,image_paths) 
        th.save_name_r(hwp,row,base) 
        hwp.Quit()
        del hwp
    elif act_r == 0:
        pass

def iamge_total(row, index, di, dt2, act_p):
    if act_p == 1:    
        image_paths = di[list(di.keys())[index % len(di)]] 
        base = th.sel_work2(row, dt2) 
        hwp = th.open_hwp(th.FORM_PATH_P) 
        th.txt_p(hwp,row,base) 
        th.images_p(hwp,image_paths) 
        th.save_name_p(hwp,row,base) 
        hwp.Quit() 
        del hwp
    elif act_p == 0:
        pass

def image_del(index, di):
    image_paths = di[list(di.keys())[index % len(di)]] 
    for image_path in image_paths: # 로컬 저장소에 다운로드한 이미지 파일 삭제
        os.remove(image_path)

def range(start_row, end_row):
    if start_row is None:
        start_row = None
    else:
        start_row -= 1
    return start_row, end_row