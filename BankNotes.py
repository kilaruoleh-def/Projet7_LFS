# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020
@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    AMT_CREDIT : float
    AMT_ANNUITY : float
    AMT_GOODS_PRICE : float
    REGION_POPULATION_RELATIVE : float
    DAYS_BIRTH : float
    DAYS_ID_PUBLISH : float
    OCCUPATION_TYPE : float
    WEEKDAY_APPR_PROCESS_START : float
    HOUR_APPR_PROCESS_START : float
    EXT_SOURCE_1 : float
    EXT_SOURCE_2 : float
    EXT_SOURCE_3 : float
    AMT_REQ_CREDIT_BUREAU_YEAR : float