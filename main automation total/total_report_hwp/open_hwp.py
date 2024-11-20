import win32com.client as win32

# HWP 파일 열기 함수
def open_hwp(file_path):
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")
    hwp.XHwpWindows.Item(0).Visible = False
    hwp.Open(file_path)
    return hwp