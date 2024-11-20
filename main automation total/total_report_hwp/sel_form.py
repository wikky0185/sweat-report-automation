import pandas as pd
from total_report_hwp.path import FORM_PATH_R

def sel_form(row):
    if pd.isna(row["튜터4"]):
        if pd.isna(row["튜터3"]):
            if pd.isna(row["튜터2"]):
                return FORM_PATH_R(1)
            else:
                return FORM_PATH_R(2)
        else:
            return FORM_PATH_R(3)
    else:
        return FORM_PATH_R(4)