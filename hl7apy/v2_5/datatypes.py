# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2014, CRS4
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

DATATYPES = {'AD': ('sequence',
        (('AD_1', (0, 1)),
         ('AD_2', (0, 1)),
         ('AD_3', (0, 1)),
         ('AD_4', (0, 1)),
         ('AD_5', (0, 1)),
         ('AD_6', (0, 1)),
         ('AD_7', (0, 1)),
         ('AD_8', (0, 1)))),
 'AD_1': ('leaf', 'ST', 'STREET_ADDRESS', None),
 'AD_2': ('leaf', 'ST', 'OTHER_DESIGNATION', None),
 'AD_3': ('leaf', 'ST', 'CITY', None),
 'AD_4': ('leaf', 'ST', 'STATE_OR_PROVINCE', None),
 'AD_5': ('leaf', 'ST', 'ZIP_OR_POSTAL_CODE', None),
 'AD_6': ('leaf', 'ID', 'COUNTRY', None),
 'AD_7': ('leaf', 'ID', 'ADDRESS_TYPE', None),
 'AD_8': ('leaf', 'ST', 'OTHER_GEOGRAPHIC_DESIGNATION', None),
 'AUI': ('sequence',
         (('AUI_1', (0, 1)), ('AUI_2', (0, 1)), ('AUI_3', (0, 1)))),
 'AUI_1': ('leaf', 'ST', 'AUTHORIZATION_NUMBER', None),
 'AUI_2': ('leaf', 'DT', 'DATE', None),
 'AUI_3': ('leaf', 'ST', 'SOURCE', None),
 'CCD': ('sequence', (('CCD_1', (1, 1)), ('CCD_2', (0, 1)))),
 'CCD_1': ('leaf', 'ID', 'INVOCATION_EVENT', None),
 'CCD_2': ('leaf', 'TS', 'DATE_TIME', None),
 'CCP': ('sequence',
         (('CCP_1', (0, 1)), ('CCP_2', (0, 1)), ('CCP_3', (0, 1)))),
 'CCP_1': ('leaf',
           'NM',
           'CHANNEL_CALIBRATION_SENSITIVITY_CORRECTION_FACTOR',
           None),
 'CCP_2': ('leaf', 'NM', 'CHANNEL_CALIBRATION_BASELINE', None),
 'CCP_3': ('leaf', 'NM', 'CHANNEL_CALIBRATION_TIME_SKEW', None),
 'CD': ('sequence',
        (('CD_1', (0, 1)),
         ('CD_2', (0, 1)),
         ('CD_3', (0, 1)),
         ('CD_4', (0, 1)),
         ('CD_5', (0, 1)),
         ('CD_6', (0, 1)))),
 'CD_1': ('leaf', 'WVI', 'CHANNEL_IDENTIFIER', None),
 'CD_2': ('leaf', 'WVS', 'WAVEFORM_SOURCE', None),
 'CD_3': ('leaf', 'CSU', 'CHANNEL_SENSITIVITY_UNITS', None),
 'CD_4': ('leaf', 'CCP', 'CHANNEL_CALIBRATION_PARAMETERS', None),
 'CD_5': ('leaf', 'NM', 'CHANNEL_SAMPLING_FREQUENCY', None),
 'CD_6': ('leaf', 'NR', 'MINIMUM_MAXIMUM_DATA_VALUES', None),
 'CE': ('sequence',
        (('CE_1', (0, 1)),
         ('CE_2', (0, 1)),
         ('CE_3', (0, 1)),
         ('CE_4', (0, 1)),
         ('CE_5', (0, 1)),
         ('CE_6', (0, 1)))),
 'CE_1': ('leaf', 'ST', 'IDENTIFIER', None),
 'CE_2': ('leaf', 'ST', 'TEXT', None),
 'CE_3': ('leaf', 'ID', 'NAME_OF_CODING_SYSTEM', None),
 'CE_4': ('leaf', 'ST', 'ALTERNATE_IDENTIFIER', None),
 'CE_5': ('leaf', 'ST', 'ALTERNATE_TEXT', None),
 'CE_6': ('leaf', 'ID', 'NAME_OF_ALTERNATE_CODING_SYSTEM', None),
 'CF': ('sequence',
        (('CF_1', (0, 1)),
         ('CF_2', (0, 1)),
         ('CF_3', (0, 1)),
         ('CF_4', (0, 1)),
         ('CF_5', (0, 1)),
         ('CF_6', (0, 1)))),
 'CF_1': ('leaf', 'ST', 'IDENTIFIER', None),
 'CF_2': ('leaf', 'FT', 'FORMATTED_TEXT', None),
 'CF_3': ('leaf', 'ID', 'NAME_OF_CODING_SYSTEM', None),
 'CF_4': ('leaf', 'ST', 'ALTERNATE_IDENTIFIER', None),
 'CF_5': ('leaf', 'FT', 'ALTERNATE_FORMATTED_TEXT', None),
 'CF_6': ('leaf', 'ID', 'NAME_OF_ALTERNATE_CODING_SYSTEM', None),
 'CNE': ('sequence',
         (('CNE_1', (1, 1)),
          ('CNE_2', (0, 1)),
          ('CNE_3', (0, 1)),
          ('CNE_4', (0, 1)),
          ('CNE_5', (0, 1)),
          ('CNE_6', (0, 1)),
          ('CNE_7', (0, 1)),
          ('CNE_8', (0, 1)),
          ('CNE_9', (0, 1)))),
 'CNE_1': ('leaf', 'ST', 'IDENTIFIER', None),
 'CNE_2': ('leaf', 'ST', 'TEXT', None),
 'CNE_3': ('leaf', 'ID', 'NAME_OF_CODING_SYSTEM', None),
 'CNE_4': ('leaf', 'ST', 'ALTERNATE_IDENTIFIER', None),
 'CNE_5': ('leaf', 'ST', 'ALTERNATE_TEXT', None),
 'CNE_6': ('leaf', 'ID', 'NAME_OF_ALTERNATE_CODING_SYSTEM', None),
 'CNE_7': ('leaf', 'ST', 'CODING_SYSTEM_VERSION_ID', None),
 'CNE_8': ('leaf', 'ST', 'ALTERNATE_CODING_SYSTEM_VERSION_ID', None),
 'CNE_9': ('leaf', 'ST', 'ORIGINAL_TEXT', None),
 'CNN': ('sequence',
         (('CNN_1', (0, 1)),
          ('CNN_2', (0, 1)),
          ('CNN_3', (0, 1)),
          ('CNN_4', (0, 1)),
          ('CNN_5', (0, 1)),
          ('CNN_6', (0, 1)),
          ('CNN_7', (0, 1)),
          ('CNN_8', (0, 1)),
          ('CNN_9', (0, 1)),
          ('CNN_10', (0, 1)),
          ('CNN_11', (0, 1)))),
 'CNN_1': ('leaf', 'ST', 'ID_NUMBER', None),
 'CNN_10': ('leaf', 'ST', 'ASSIGNING_AUTHORITY_UNIVERSAL_ID', None),
 'CNN_11': ('leaf', 'ID', 'ASSIGNING_AUTHORITY_UNIVERSAL_ID_TYPE', None),
 'CNN_2': ('leaf', 'ST', 'FAMILY_NAME', None),
 'CNN_3': ('leaf', 'ST', 'GIVEN_NAME', None),
 'CNN_4': ('leaf',
           'ST',
           'SECOND_AND_FURTHER_GIVEN_NAMES_OR_INITIALS_THEREOF',
           None),
 'CNN_5': ('leaf', 'ST', 'SUFFIX_E_G_JR_OR_III', None),
 'CNN_6': ('leaf', 'ST', 'PREFIX_E_G_DR', None),
 'CNN_7': ('leaf', 'IS', 'DEGREE_E_G_MD', None),
 'CNN_8': ('leaf', 'IS', 'SOURCE_TABLE', None),
 'CNN_9': ('leaf', 'IS', 'ASSIGNING_AUTHORITY_NAMESPACE_ID', None),
 'CP': ('sequence',
        (('CP_1', (1, 1)),
         ('CP_2', (0, 1)),
         ('CP_3', (0, 1)),
         ('CP_4', (0, 1)),
         ('CP_5', (0, 1)),
         ('CP_6', (0, 1)))),
 'CP_1': ('leaf', 'MO', 'PRICE', None),
 'CP_2': ('leaf', 'ID', 'PRICE_TYPE', None),
 'CP_3': ('leaf', 'NM', 'FROM_VALUE', None),
 'CP_4': ('leaf', 'NM', 'TO_VALUE', None),
 'CP_5': ('leaf', 'CE', 'RANGE_UNITS', None),
 'CP_6': ('leaf', 'ID', 'RANGE_TYPE', None),
 'CQ': ('sequence', (('CQ_1', (0, 1)), ('CQ_2', (0, 1)))),
 'CQ_1': ('leaf', 'NM', 'QUANTITY', None),
 'CQ_2': ('leaf', 'CE', 'UNITS', None),
 'CSU': ('sequence',
         (('CSU_1', (1, 1)),
          ('CSU_2', (0, 1)),
          ('CSU_3', (0, 1)),
          ('CSU_4', (0, 1)),
          ('CSU_5', (0, 1)),
          ('CSU_6', (0, 1)),
          ('CSU_7', (0, 1)))),
 'CSU_1': ('leaf', 'NM', 'CHANNEL_SENSITIVITY', None),
 'CSU_2': ('leaf', 'ST', 'UNIT_OF_MEASURE_IDENTIFIER', None),
 'CSU_3': ('leaf', 'ST', 'UNIT_OF_MEASURE_DESCRIPTION', None),
 'CSU_4': ('leaf', 'ID', 'UNIT_OF_MEASURE_CODING_SYSTEM', None),
 'CSU_5': ('leaf', 'ST', 'ALTERNATE_UNIT_OF_MEASURE_IDENTIFIER', None),
 'CSU_6': ('leaf', 'ST', 'ALTERNATE_UNIT_OF_MEASURE_DESCRIPTION', None),
 'CSU_7': ('leaf', 'ID', 'ALTERNATE_UNIT_OF_MEASURE_CODING_SYSTEM', None),
 'CWE': ('sequence',
         (('CWE_1', (0, 1)),
          ('CWE_2', (0, 1)),
          ('CWE_3', (0, 1)),
          ('CWE_4', (0, 1)),
          ('CWE_5', (0, 1)),
          ('CWE_6', (0, 1)),
          ('CWE_7', (0, 1)),
          ('CWE_8', (0, 1)),
          ('CWE_9', (0, 1)))),
 'CWE_1': ('leaf', 'ST', 'IDENTIFIER', None),
 'CWE_2': ('leaf', 'ST', 'TEXT', None),
 'CWE_3': ('leaf', 'ID', 'NAME_OF_CODING_SYSTEM', None),
 'CWE_4': ('leaf', 'ST', 'ALTERNATE_IDENTIFIER', None),
 'CWE_5': ('leaf', 'ST', 'ALTERNATE_TEXT', None),
 'CWE_6': ('leaf', 'ID', 'NAME_OF_ALTERNATE_CODING_SYSTEM', None),
 'CWE_7': ('leaf', 'ST', 'CODING_SYSTEM_VERSION_ID', None),
 'CWE_8': ('leaf', 'ST', 'ALTERNATE_CODING_SYSTEM_VERSION_ID', None),
 'CWE_9': ('leaf', 'ST', 'ORIGINAL_TEXT', None),
 'CX': ('sequence',
        (('CX_1', (1, 1)),
         ('CX_2', (0, 1)),
         ('CX_3', (0, 1)),
         ('CX_4', (0, 1)),
         ('CX_5', (0, 1)),
         ('CX_6', (0, 1)),
         ('CX_7', (0, 1)),
         ('CX_8', (0, 1)),
         ('CX_9', (0, 1)),
         ('CX_10', (0, 1)))),
 'CX_1': ('leaf', 'ST', 'ID_NUMBER', None),
 'CX_10': ('leaf', 'CWE', 'ASSIGNING_AGENCY_OR_DEPARTMENT', None),
 'CX_2': ('leaf', 'ST', 'CHECK_DIGIT', None),
 'CX_3': ('leaf', 'ID', 'CHECK_DIGIT_SCHEME', None),
 'CX_4': ('leaf', 'HD', 'ASSIGNING_AUTHORITY', None),
 'CX_5': ('leaf', 'ID', 'IDENTIFIER_TYPE_CODE', None),
 'CX_6': ('leaf', 'HD', 'ASSIGNING_FACILITY', None),
 'CX_7': ('leaf', 'DT', 'EFFECTIVE_DATE', None),
 'CX_8': ('leaf', 'DT', 'EXPIRATION_DATE', None),
 'CX_9': ('leaf', 'CWE', 'ASSIGNING_JURISDICTION', None),
 'DDI': ('sequence',
         (('DDI_1', (0, 1)), ('DDI_2', (1, 1)), ('DDI_3', (0, 1)))),
 'DDI_1': ('leaf', 'NM', 'DELAY_DAYS', None),
 'DDI_2': ('leaf', 'MO', 'MONETARY_AMOUNT', None),
 'DDI_3': ('leaf', 'NM', 'NUMBER_OF_DAYS', None),
 'DIN': ('sequence', (('DIN_1', (1, 1)), ('DIN_2', (1, 1)))),
 'DIN_1': ('leaf', 'TS', 'DATE', None),
 'DIN_2': ('leaf', 'CE', 'INSTITUTION_NAME', None),
 'DLD': ('sequence', (('DLD_1', (1, 1)), ('DLD_2', (0, 1)))),
 'DLD_1': ('leaf', 'IS', 'DISCHARGE_LOCATION', None),
 'DLD_2': ('leaf', 'TS', 'EFFECTIVE_DATE', None),
 'DLN': ('sequence',
         (('DLN_1', (1, 1)), ('DLN_2', (0, 1)), ('DLN_3', (0, 1)))),
 'DLN_1': ('leaf', 'ST', 'LICENSE_NUMBER', None),
 'DLN_2': ('leaf', 'IS', 'ISSUING_STATE_PROVINCE_COUNTRY', None),
 'DLN_3': ('leaf', 'DT', 'EXPIRATION_DATE', None),
 'DLT': ('sequence',
         (('DLT_1', (0, 1)),
          ('DLT_2', (0, 1)),
          ('DLT_3', (0, 1)),
          ('DLT_4', (0, 1)))),
 'DLT_1': ('leaf', 'NR', 'NORMAL_RANGE', None),
 'DLT_2': ('leaf', 'NM', 'NUMERIC_THRESHOLD', None),
 'DLT_3': ('leaf', 'ID', 'CHANGE_COMPUTATION', None),
 'DLT_4': ('leaf', 'NM', 'DAYS_RETAINED', None),
 'DR': ('sequence', (('DR_1', (0, 1)), ('DR_2', (0, 1)))),
 'DR_1': ('leaf', 'TS', 'RANGE_START_DATE_TIME', None),
 'DR_2': ('leaf', 'TS', 'RANGE_END_DATE_TIME', None),
 'DTN': ('sequence', (('DTN_1', (1, 1)), ('DTN_2', (1, 1)))),
 'DTN_1': ('leaf', 'IS', 'DAY_TYPE', None),
 'DTN_2': ('leaf', 'NM', 'NUMBER_OF_DAYS', None),
 'ED': ('sequence',
        (('ED_1', (0, 1)),
         ('ED_2', (1, 1)),
         ('ED_3', (0, 1)),
         ('ED_4', (1, 1)),
         ('ED_5', (1, 1)))),
 'ED_1': ('leaf', 'HD', 'SOURCE_APPLICATION', None),
 'ED_2': ('leaf', 'ID', 'TYPE_OF_DATA', None),
 'ED_3': ('leaf', 'ID', 'DATA_SUBTYPE', None),
 'ED_4': ('leaf', 'ID', 'ENCODING', None),
 'ED_5': ('leaf', 'TX', 'DATA', None),
 'EI': ('sequence',
        (('EI_1', (0, 1)),
         ('EI_2', (0, 1)),
         ('EI_3', (0, 1)),
         ('EI_4', (0, 1)))),
 'EIP': ('sequence', (('EIP_1', (0, 1)), ('EIP_2', (0, 1)))),
 'EIP_1': ('leaf', 'EI', 'PLACER_ASSIGNED_IDENTIFIER', None),
 'EIP_2': ('leaf', 'EI', 'FILLER_ASSIGNED_IDENTIFIER', None),
 'EI_1': ('leaf', 'ST', 'ENTITY_IDENTIFIER', None),
 'EI_2': ('leaf', 'IS', 'NAMESPACE_ID', None),
 'EI_3': ('leaf', 'ST', 'UNIVERSAL_ID', None),
 'EI_4': ('leaf', 'ID', 'UNIVERSAL_ID_TYPE', None),
 'ELD': ('sequence',
         (('ELD_1', (0, 1)),
          ('ELD_2', (0, 1)),
          ('ELD_3', (0, 1)),
          ('ELD_4', (0, 1)))),
 'ELD_1': ('leaf', 'ST', 'SEGMENT_ID', None),
 'ELD_2': ('leaf', 'NM', 'SEGMENT_SEQUENCE', None),
 'ELD_3': ('leaf', 'NM', 'FIELD_POSITION', None),
 'ELD_4': ('leaf', 'CE', 'CODE_IDENTIFYING_ERROR', None),
 'ERL': ('sequence',
         (('ERL_1', (1, 1)),
          ('ERL_2', (1, 1)),
          ('ERL_3', (0, 1)),
          ('ERL_4', (0, 1)),
          ('ERL_5', (0, 1)),
          ('ERL_6', (0, 1)))),
 'ERL_1': ('leaf', 'ST', 'SEGMENT_ID', None),
 'ERL_2': ('leaf', 'NM', 'SEGMENT_SEQUENCE', None),
 'ERL_3': ('leaf', 'NM', 'FIELD_POSITION', None),
 'ERL_4': ('leaf', 'NM', 'FIELD_REPETITION', None),
 'ERL_5': ('leaf', 'NM', 'COMPONENT_NUMBER', None),
 'ERL_6': ('leaf', 'NM', 'SUB_COMPONENT_NUMBER', None),
 'FC': ('sequence', (('FC_1', (1, 1)), ('FC_2', (0, 1)))),
 'FC_1': ('leaf', 'IS', 'FINANCIAL_CLASS_CODE', None),
 'FC_2': ('leaf', 'TS', 'EFFECTIVE_DATE', None),
 'FN': ('sequence',
        (('FN_1', (1, 1)),
         ('FN_2', (0, 1)),
         ('FN_3', (0, 1)),
         ('FN_4', (0, 1)),
         ('FN_5', (0, 1)))),
 'FN_1': ('leaf', 'ST', 'SURNAME', None),
 'FN_2': ('leaf', 'ST', 'OWN_SURNAME_PREFIX', None),
 'FN_3': ('leaf', 'ST', 'OWN_SURNAME', None),
 'FN_4': ('leaf', 'ST', 'SURNAME_PREFIX_FROM_PARTNER_SPOUSE', None),
 'FN_5': ('leaf', 'ST', 'SURNAME_FROM_PARTNER_SPOUSE', None),
 'HD': ('sequence', (('HD_1', (0, 1)), ('HD_2', (0, 1)), ('HD_3', (0, 1)))),
 'HD_1': ('leaf', 'IS', 'NAMESPACE_ID', None),
 'HD_2': ('leaf', 'ST', 'UNIVERSAL_ID', None),
 'HD_3': ('leaf', 'ID', 'UNIVERSAL_ID_TYPE', None),
 'ICD': ('sequence',
         (('ICD_1', (0, 1)), ('ICD_2', (1, 1)), ('ICD_3', (0, 1)))),
 'ICD_1': ('leaf', 'IS', 'CERTIFICATION_PATIENT_TYPE', None),
 'ICD_2': ('leaf', 'ID', 'CERTIFICATION_REQUIRED', None),
 'ICD_3': ('leaf', 'TS', 'DATE_TIME_CERTIFICATION_REQUIRED', None),
 'JCC': ('sequence',
         (('JCC_1', (0, 1)), ('JCC_2', (0, 1)), ('JCC_3', (0, 1)))),
 'JCC_1': ('leaf', 'IS', 'JOB_CODE', None),
 'JCC_2': ('leaf', 'IS', 'JOB_CLASS', None),
 'JCC_3': ('leaf', 'TX', 'JOB_DESCRIPTION_TEXT', None),
 'LA1': ('sequence',
         (('LA1_1', (0, 1)),
          ('LA1_2', (0, 1)),
          ('LA1_3', (0, 1)),
          ('LA1_4', (0, 1)),
          ('LA1_5', (0, 1)),
          ('LA1_6', (0, 1)),
          ('LA1_7', (0, 1)),
          ('LA1_8', (0, 1)),
          ('LA1_9', (0, 1)))),
 'LA1_1': ('leaf', 'IS', 'POINT_OF_CARE', None),
 'LA1_2': ('leaf', 'IS', 'ROOM', None),
 'LA1_3': ('leaf', 'IS', 'BED', None),
 'LA1_4': ('leaf', 'HD', 'FACILITY', None),
 'LA1_5': ('leaf', 'IS', 'LOCATION_STATUS', None),
 'LA1_6': ('leaf', 'IS', 'PATIENT_LOCATION_TYPE', None),
 'LA1_7': ('leaf', 'IS', 'BUILDING', None),
 'LA1_8': ('leaf', 'IS', 'FLOOR', None),
 'LA1_9': ('leaf', 'AD', 'ADDRESS', None),
 'LA2': ('sequence',
         (('LA2_1', (0, 1)),
          ('LA2_2', (0, 1)),
          ('LA2_3', (0, 1)),
          ('LA2_4', (0, 1)),
          ('LA2_5', (0, 1)),
          ('LA2_6', (0, 1)),
          ('LA2_7', (0, 1)),
          ('LA2_8', (0, 1)),
          ('LA2_9', (0, 1)),
          ('LA2_10', (0, 1)),
          ('LA2_11', (0, 1)),
          ('LA2_12', (0, 1)),
          ('LA2_13', (0, 1)),
          ('LA2_14', (0, 1)),
          ('LA2_15', (0, 1)),
          ('LA2_16', (0, 1)))),
 'LA2_1': ('leaf', 'IS', 'POINT_OF_CARE', None),
 'LA2_10': ('leaf', 'ST', 'OTHER_DESIGNATION', None),
 'LA2_11': ('leaf', 'ST', 'CITY', None),
 'LA2_12': ('leaf', 'ST', 'STATE_OR_PROVINCE', None),
 'LA2_13': ('leaf', 'ST', 'ZIP_OR_POSTAL_CODE', None),
 'LA2_14': ('leaf', 'ID', 'COUNTRY', None),
 'LA2_15': ('leaf', 'ID', 'ADDRESS_TYPE', None),
 'LA2_16': ('leaf', 'ST', 'OTHER_GEOGRAPHIC_DESIGNATION', None),
 'LA2_2': ('leaf', 'IS', 'ROOM', None),
 'LA2_3': ('leaf', 'IS', 'BED', None),
 'LA2_4': ('leaf', 'HD', 'FACILITY', None),
 'LA2_5': ('leaf', 'IS', 'LOCATION_STATUS', None),
 'LA2_6': ('leaf', 'IS', 'PATIENT_LOCATION_TYPE', None),
 'LA2_7': ('leaf', 'IS', 'BUILDING', None),
 'LA2_8': ('leaf', 'IS', 'FLOOR', None),
 'LA2_9': ('leaf', 'ST', 'STREET_ADDRESS', None),
 'MA': ('sequence',
        (('MA_1', (0, 1)),
         ('MA_2', (0, 1)),
         ('MA_3', (0, 1)),
         ('MA_4', (0, 1)),
         ('MA_5', (0, 1)),
         ('MA_6', (0, 1)))),
 'MA_1': ('leaf', 'NM', 'SAMPLE_1_FROM_CHANNEL_1', None),
 'MA_2': ('leaf', 'NM', 'SAMPLE_1_FROM_CHANNEL_2', None),
 'MA_3': ('leaf', 'NM', 'SAMPLE_1_FROM_CHANNEL_N', None),
 'MA_4': ('leaf', 'NM', 'SAMPLE_2_FROM_CHANNEL_1', None),
 'MA_5': ('leaf', 'NM', 'SAMPLE_2_FROM_CHANNEL_N', None),
 'MA_6': ('leaf', 'NM', 'SAMPLE_N_FROM_CHANNEL_N', None),
 'MO': ('sequence', (('MO_1', (0, 1)), ('MO_2', (0, 1)))),
 'MOC': ('sequence', (('MOC_1', (0, 1)), ('MOC_2', (0, 1)))),
 'MOC_1': ('leaf', 'MO', 'MONETARY_AMOUNT', None),
 'MOC_2': ('leaf', 'CE', 'CHARGE_CODE', None),
 'MOP': ('sequence',
         (('MOP_1', (1, 1)), ('MOP_2', (1, 1)), ('MOP_3', (0, 1)))),
 'MOP_1': ('leaf', 'ID', 'MONEY_OR_PERCENTAGE_INDICATOR', None),
 'MOP_2': ('leaf', 'NM', 'MONEY_OR_PERCENTAGE_QUANTITY', None),
 'MOP_3': ('leaf', 'ID', 'CURRENCY_DENOMINATION', None),
 'MO_1': ('leaf', 'NM', 'QUANTITY', None),
 'MO_2': ('leaf', 'ID', 'DENOMINATION', None),
 'MSG': ('sequence',
         (('MSG_1', (1, 1)), ('MSG_2', (1, 1)), ('MSG_3', (1, 1)))),
 'MSG_1': ('leaf', 'ID', 'MESSAGE_CODE', None),
 'MSG_2': ('leaf', 'ID', 'TRIGGER_EVENT', None),
 'MSG_3': ('leaf', 'ID', 'MESSAGE_STRUCTURE', None),
 'NA': ('sequence',
        (('NA_1', (1, 1)),
         ('NA_2', (0, 1)),
         ('NA_3', (0, 1)),
         ('NA_4', (0, 1)))),
 'NA_1': ('leaf', 'NM', 'VALUE1', None),
 'NA_2': ('leaf', 'NM', 'VALUE2', None),
 'NA_3': ('leaf', 'NM', 'VALUE3', None),
 'NA_4': ('leaf', 'NM', 'VALUE4', None),
 'NDL': ('sequence',
         (('NDL_1', (0, 1)),
          ('NDL_2', (0, 1)),
          ('NDL_3', (0, 1)),
          ('NDL_4', (0, 1)),
          ('NDL_5', (0, 1)),
          ('NDL_6', (0, 1)),
          ('NDL_7', (0, 1)),
          ('NDL_8', (0, 1)),
          ('NDL_9', (0, 1)),
          ('NDL_10', (0, 1)),
          ('NDL_11', (0, 1)))),
 'NDL_1': ('leaf', 'CNN', 'NAME', None),
 'NDL_10': ('leaf', 'IS', 'BUILDING', None),
 'NDL_11': ('leaf', 'IS', 'FLOOR', None),
 'NDL_2': ('leaf', 'TS', 'START_DATE_TIME', None),
 'NDL_3': ('leaf', 'TS', 'END_DATE_TIME', None),
 'NDL_4': ('leaf', 'IS', 'POINT_OF_CARE', None),
 'NDL_5': ('leaf', 'IS', 'ROOM', None),
 'NDL_6': ('leaf', 'IS', 'BED', None),
 'NDL_7': ('leaf', 'HD', 'FACILITY', None),
 'NDL_8': ('leaf', 'IS', 'LOCATION_STATUS', None),
 'NDL_9': ('leaf', 'IS', 'PATIENT_LOCATION_TYPE', None),
 'NR': ('sequence', (('NR_1', (0, 1)), ('NR_2', (0, 1)))),
 'NR_1': ('leaf', 'NM', 'LOW_VALUE', None),
 'NR_2': ('leaf', 'NM', 'HIGH_VALUE', None),
 'OCD': ('sequence', (('OCD_1', (1, 1)), ('OCD_2', (1, 1)))),
 'OCD_1': ('leaf', 'CNE', 'OCCURRENCE_CODE', None),
 'OCD_2': ('leaf', 'DT', 'OCCURRENCE_DATE', None),
 'OSD': ('sequence',
         (('OSD_1', (1, 1)),
          ('OSD_2', (1, 1)),
          ('OSD_3', (0, 1)),
          ('OSD_4', (1, 1)),
          ('OSD_5', (0, 1)),
          ('OSD_6', (0, 1)),
          ('OSD_7', (0, 1)),
          ('OSD_8', (1, 1)),
          ('OSD_9', (0, 1)),
          ('OSD_10', (1, 1)),
          ('OSD_11', (0, 1)))),
 'OSD_1': ('leaf', 'ID', 'SEQUENCE_RESULTS_FLAG', None),
 'OSD_10': ('leaf', 'ST', 'FILLER_ORDER_NUMBER_UNIVERSAL_ID', None),
 'OSD_11': ('leaf', 'ID', 'FILLER_ORDER_NUMBER_UNIVERSAL_ID_TYPE', None),
 'OSD_2': ('leaf', 'ST', 'PLACER_ORDER_NUMBER_ENTITY_IDENTIFIER', None),
 'OSD_3': ('leaf', 'IS', 'PLACER_ORDER_NUMBER_NAMESPACE_ID', None),
 'OSD_4': ('leaf', 'ST', 'FILLER_ORDER_NUMBER_ENTITY_IDENTIFIER', None),
 'OSD_5': ('leaf', 'IS', 'FILLER_ORDER_NUMBER_NAMESPACE_ID', None),
 'OSD_6': ('leaf', 'ST', 'SEQUENCE_CONDITION_VALUE', None),
 'OSD_7': ('leaf', 'NM', 'MAXIMUM_NUMBER_OF_REPEATS', None),
 'OSD_8': ('leaf', 'ST', 'PLACER_ORDER_NUMBER_UNIVERSAL_ID', None),
 'OSD_9': ('leaf', 'ID', 'PLACER_ORDER_NUMBER_UNIVERSAL_ID_TYPE', None),
 'OSP': ('sequence',
         (('OSP_1', (1, 1)), ('OSP_2', (0, 1)), ('OSP_3', (0, 1)))),
 'OSP_1': ('leaf', 'CNE', 'OCCURRENCE_SPAN_CODE', None),
 'OSP_2': ('leaf', 'DT', 'OCCURRENCE_SPAN_START_DATE', None),
 'OSP_3': ('leaf', 'DT', 'OCCURRENCE_SPAN_STOP_DATE', None),
 'PIP': ('sequence',
         (('PIP_1', (1, 1)),
          ('PIP_2', (0, 1)),
          ('PIP_3', (0, 1)),
          ('PIP_4', (0, 1)),
          ('PIP_5', (0, 1)))),
 'PIP_1': ('leaf', 'CE', 'PRIVILEGE', None),
 'PIP_2': ('leaf', 'CE', 'PRIVILEGE_CLASS', None),
 'PIP_3': ('leaf', 'DT', 'EXPIRATION_DATE', None),
 'PIP_4': ('leaf', 'DT', 'ACTIVATION_DATE', None),
 'PIP_5': ('leaf', 'EI', 'FACILITY', None),
 'PL': ('sequence',
        (('PL_1', (0, 1)),
         ('PL_2', (0, 1)),
         ('PL_3', (0, 1)),
         ('PL_4', (0, 1)),
         ('PL_5', (0, 1)),
         ('PL_6', (0, 1)),
         ('PL_7', (0, 1)),
         ('PL_8', (0, 1)),
         ('PL_9', (0, 1)),
         ('PL_10', (0, 1)),
         ('PL_11', (0, 1)))),
 'PLN': ('sequence',
         (('PLN_1', (1, 1)),
          ('PLN_2', (1, 1)),
          ('PLN_3', (0, 1)),
          ('PLN_4', (0, 1)))),
 'PLN_1': ('leaf', 'ST', 'ID_NUMBER', None),
 'PLN_2': ('leaf', 'IS', 'TYPE_OF_ID_NUMBER', None),
 'PLN_3': ('leaf', 'ST', 'STATE_OTHER_QUALIFYING_INFORMATION', None),
 'PLN_4': ('leaf', 'DT', 'EXPIRATION_DATE', None),
 'PL_1': ('leaf', 'IS', 'POINT_OF_CARE', None),
 'PL_10': ('leaf', 'EI', 'COMPREHENSIVE_LOCATION_IDENTIFIER', None),
 'PL_11': ('leaf', 'HD', 'ASSIGNING_AUTHORITY_FOR_LOCATION', None),
 'PL_2': ('leaf', 'IS', 'ROOM', None),
 'PL_3': ('leaf', 'IS', 'BED', None),
 'PL_4': ('leaf', 'HD', 'FACILITY', None),
 'PL_5': ('leaf', 'IS', 'LOCATION_STATUS', None),
 'PL_6': ('leaf', 'IS', 'PERSON_LOCATION_TYPE', None),
 'PL_7': ('leaf', 'IS', 'BUILDING', None),
 'PL_8': ('leaf', 'IS', 'FLOOR', None),
 'PL_9': ('leaf', 'ST', 'LOCATION_DESCRIPTION', None),
 'PPN': ('sequence',
         (('PPN_1', (0, 1)),
          ('PPN_2', (0, 1)),
          ('PPN_3', (0, 1)),
          ('PPN_4', (0, 1)),
          ('PPN_5', (0, 1)),
          ('PPN_6', (0, 1)),
          ('PPN_7', (0, 1)),
          ('PPN_8', (0, 1)),
          ('PPN_9', (0, 1)),
          ('PPN_10', (0, 1)),
          ('PPN_11', (0, 1)),
          ('PPN_12', (0, 1)),
          ('PPN_13', (0, 1)),
          ('PPN_14', (0, 1)),
          ('PPN_15', (0, 1)),
          ('PPN_16', (0, 1)),
          ('PPN_17', (0, 1)),
          ('PPN_18', (0, 1)),
          ('PPN_19', (0, 1)),
          ('PPN_20', (0, 1)),
          ('PPN_21', (0, 1)),
          ('PPN_22', (0, 1)),
          ('PPN_23', (0, 1)),
          ('PPN_24', (0, 1)))),
 'PPN_1': ('leaf', 'ST', 'ID_NUMBER', None),
 'PPN_10': ('leaf', 'ID', 'NAME_TYPE_CODE', None),
 'PPN_11': ('leaf', 'ST', 'IDENTIFIER_CHECK_DIGIT', None),
 'PPN_12': ('leaf', 'ID', 'CHECK_DIGIT_SCHEME', None),
 'PPN_13': ('leaf', 'ID', 'IDENTIFIER_TYPE_CODE', None),
 'PPN_14': ('leaf', 'HD', 'ASSIGNING_FACILITY', None),
 'PPN_15': ('leaf', 'TS', 'DATE_TIME_ACTION_PERFORMED', None),
 'PPN_16': ('leaf', 'ID', 'NAME_REPRESENTATION_CODE', None),
 'PPN_17': ('leaf', 'CE', 'NAME_CONTEXT', None),
 'PPN_18': ('leaf', 'DR', 'NAME_VALIDITY_RANGE', None),
 'PPN_19': ('leaf', 'ID', 'NAME_ASSEMBLY_ORDER', None),
 'PPN_2': ('leaf', 'FN', 'FAMILY_NAME', None),
 'PPN_20': ('leaf', 'TS', 'EFFECTIVE_DATE', None),
 'PPN_21': ('leaf', 'TS', 'EXPIRATION_DATE', None),
 'PPN_22': ('leaf', 'ST', 'PROFESSIONAL_SUFFIX', None),
 'PPN_23': ('leaf', 'CWE', 'ASSIGNING_JURISDICTION', None),
 'PPN_24': ('leaf', 'CWE', 'ASSIGNING_AGENCY_OR_DEPARTMENT', None),
 'PPN_3': ('leaf', 'ST', 'GIVEN_NAME', None),
 'PPN_4': ('leaf',
           'ST',
           'SECOND_AND_FURTHER_GIVEN_NAMES_OR_INITIALS_THEREOF',
           None),
 'PPN_5': ('leaf', 'ST', 'SUFFIX_E_G_JR_OR_III', None),
 'PPN_6': ('leaf', 'ST', 'PREFIX_E_G_DR', None),
 'PPN_7': ('leaf', 'IS', 'DEGREE_E_G_MD', None),
 'PPN_8': ('leaf', 'IS', 'SOURCE_TABLE', None),
 'PPN_9': ('leaf', 'HD', 'ASSIGNING_AUTHORITY', None),
 'PRL': ('sequence',
         (('PRL_1', (1, 1)), ('PRL_2', (0, 1)), ('PRL_3', (0, 1)))),
 'PRL_1': ('leaf', 'CE', 'PARENT_OBSERVATION_IDENTIFIER', None),
 'PRL_2': ('leaf', 'ST', 'PARENT_OBSERVATION_SUB_IDENTIFIER', None),
 'PRL_3': ('leaf', 'TX', 'PARENT_OBSERVATION_VALUE_DESCRIPTOR', None),
 'PT': ('sequence', (('PT_1', (0, 1)), ('PT_2', (0, 1)))),
 'PTA': ('sequence',
         (('PTA_1', (1, 1)),
          ('PTA_2', (0, 1)),
          ('PTA_3', (0, 1)),
          ('PTA_4', (1, 1)))),
 'PTA_1': ('leaf', 'IS', 'POLICY_TYPE', None),
 'PTA_2': ('leaf', 'IS', 'AMOUNT_CLASS', None),
 'PTA_3': ('leaf', 'NM', 'MONEY_OR_PERCENTAGE_QUANTITY', None),
 'PTA_4': ('leaf', 'MOP', 'MONEY_OR_PERCENTAGE', None),
 'PT_1': ('leaf', 'ID', 'PROCESSING_ID', None),
 'PT_2': ('leaf', 'ID', 'PROCESSING_MODE', None),
 'QIP': ('sequence', (('QIP_1', (1, 1)), ('QIP_2', (1, 1)))),
 'QIP_1': ('leaf', 'ST', 'SEGMENT_FIELD_NAME', None),
 'QIP_2': ('leaf', 'ST', 'VALUES', None),
 'QSC': ('sequence',
         (('QSC_1', (1, 1)),
          ('QSC_2', (0, 1)),
          ('QSC_3', (0, 1)),
          ('QSC_4', (0, 1)))),
 'QSC_1': ('leaf', 'ST', 'SEGMENT_FIELD_NAME', None),
 'QSC_2': ('leaf', 'ID', 'RELATIONAL_OPERATOR', None),
 'QSC_3': ('leaf', 'ST', 'VALUE', None),
 'QSC_4': ('leaf', 'ID', 'RELATIONAL_CONJUNCTION', None),
 'RCD': ('sequence',
         (('RCD_1', (0, 1)), ('RCD_2', (0, 1)), ('RCD_3', (0, 1)))),
 'RCD_1': ('leaf', 'ST', 'SEGMENT_FIELD_NAME', None),
 'RCD_2': ('leaf', 'ID', 'HL7_DATA_TYPE', None),
 'RCD_3': ('leaf', 'NM', 'MAXIMUM_COLUMN_WIDTH', None),
 'RFR': ('sequence',
         (('RFR_1', (1, 1)),
          ('RFR_2', (0, 1)),
          ('RFR_3', (0, 1)),
          ('RFR_4', (0, 1)),
          ('RFR_5', (0, 1)),
          ('RFR_6', (0, 1)),
          ('RFR_7', (0, 1)))),
 'RFR_1': ('leaf', 'NR', 'NUMERIC_RANGE', None),
 'RFR_2': ('leaf', 'IS', 'ADMINISTRATIVE_SEX', None),
 'RFR_3': ('leaf', 'NR', 'AGE_RANGE', None),
 'RFR_4': ('leaf', 'NR', 'GESTATIONAL_AGE_RANGE', None),
 'RFR_5': ('leaf', 'ST', 'SPECIES', None),
 'RFR_6': ('leaf', 'ST', 'RACE_SUBSPECIES', None),
 'RFR_7': ('leaf', 'TX', 'CONDITIONS', None),
 'RI': ('sequence', (('RI_1', (0, 1)), ('RI_2', (0, 1)))),
 'RI_1': ('leaf', 'IS', 'REPEAT_PATTERN', None),
 'RI_2': ('leaf', 'ST', 'EXPLICIT_TIME_INTERVAL', None),
 'RMC': ('sequence',
         (('RMC_1', (1, 1)),
          ('RMC_2', (0, 1)),
          ('RMC_3', (0, 1)),
          ('RMC_4', (1, 1)))),
 'RMC_1': ('leaf', 'IS', 'ROOM_TYPE', None),
 'RMC_2': ('leaf', 'IS', 'AMOUNT_TYPE', None),
 'RMC_3': ('leaf', 'NM', 'COVERAGE_AMOUNT', None),
 'RMC_4': ('leaf', 'MOP', 'MONEY_OR_PERCENTAGE', None),
 'RP': ('sequence',
        (('RP_1', (0, 1)),
         ('RP_2', (0, 1)),
         ('RP_3', (0, 1)),
         ('RP_4', (0, 1)))),
 'RPT': ('sequence',
         (('RPT_1', (1, 1)),
          ('RPT_2', (0, 1)),
          ('RPT_3', (0, 1)),
          ('RPT_4', (0, 1)),
          ('RPT_5', (0, 1)),
          ('RPT_6', (0, 1)),
          ('RPT_7', (0, 1)),
          ('RPT_8', (0, 1)),
          ('RPT_9', (0, 1)),
          ('RPT_10', (0, 1)),
          ('RPT_11', (0, 1)))),
 'RPT_1': ('leaf', 'CWE', 'REPEAT_PATTERN_CODE', None),
 'RPT_10': ('leaf', 'IS', 'EVENT_OFFSET_UNITS', None),
 'RPT_11': ('leaf', 'GTS', 'GENERAL_TIMING_SPECIFICATION', None),
 'RPT_2': ('leaf', 'ID', 'CALENDAR_ALIGNMENT', None),
 'RPT_3': ('leaf', 'NM', 'PHASE_RANGE_BEGIN_VALUE', None),
 'RPT_4': ('leaf', 'NM', 'PHASE_RANGE_END_VALUE', None),
 'RPT_5': ('leaf', 'NM', 'PERIOD_QUANTITY', None),
 'RPT_6': ('leaf', 'IS', 'PERIOD_UNITS', None),
 'RPT_7': ('leaf', 'ID', 'INSTITUTION_SPECIFIED_TIME', None),
 'RPT_8': ('leaf', 'ID', 'EVENT', None),
 'RPT_9': ('leaf', 'NM', 'EVENT_OFFSET_QUANTITY', None),
 'RP_1': ('leaf', 'ST', 'POINTER', None),
 'RP_2': ('leaf', 'HD', 'APPLICATION_ID', None),
 'RP_3': ('leaf', 'ID', 'TYPE_OF_DATA', None),
 'RP_4': ('leaf', 'ID', 'SUBTYPE', None),
 'SAD': ('sequence',
         (('SAD_1', (0, 1)), ('SAD_2', (0, 1)), ('SAD_3', (0, 1)))),
 'SAD_1': ('leaf', 'ST', 'STREET_OR_MAILING_ADDRESS', None),
 'SAD_2': ('leaf', 'ST', 'STREET_NAME', None),
 'SAD_3': ('leaf', 'ST', 'DWELLING_NUMBER', None),
 'SCV': ('sequence', (('SCV_1', (0, 1)), ('SCV_2', (0, 1)))),
 'SCV_1': ('leaf', 'CWE', 'PARAMETER_CLASS', None),
 'SCV_2': ('leaf', 'ST', 'PARAMETER_VALUE', None),
 'SN': ('sequence',
        (('SN_1', (0, 1)),
         ('SN_2', (0, 1)),
         ('SN_3', (0, 1)),
         ('SN_4', (0, 1)))),
 'SN_1': ('leaf', 'ST', 'COMPARATOR', None),
 'SN_2': ('leaf', 'NM', 'NUM1', None),
 'SN_3': ('leaf', 'ST', 'SEPARATOR_SUFFIX', None),
 'SN_4': ('leaf', 'NM', 'NUM2', None),
 'SPD': ('sequence',
         (('SPD_1', (1, 1)),
          ('SPD_2', (0, 1)),
          ('SPD_3', (0, 1)),
          ('SPD_4', (0, 1)))),
 'SPD_1': ('leaf', 'ST', 'SPECIALTY_NAME', None),
 'SPD_2': ('leaf', 'ST', 'GOVERNING_BOARD', None),
 'SPD_3': ('leaf', 'ID', 'ELIGIBLE_OR_CERTIFIED', None),
 'SPD_4': ('leaf', 'DT', 'DATE_OF_CERTIFICATION', None),
 'SPS': ('sequence',
         (('SPS_1', (0, 1)),
          ('SPS_2', (0, 1)),
          ('SPS_3', (0, 1)),
          ('SPS_4', (0, 1)),
          ('SPS_5', (0, 1)),
          ('SPS_6', (0, 1)),
          ('SPS_7', (0, 1)))),
 'SPS_1': ('leaf', 'CWE', 'SPECIMEN_SOURCE_NAME_OR_CODE', None),
 'SPS_2': ('leaf', 'CWE', 'ADDITIVES', None),
 'SPS_3': ('leaf', 'TX', 'SPECIMEN_COLLECTION_METHOD', None),
 'SPS_4': ('leaf', 'CWE', 'BODY_SITE', None),
 'SPS_5': ('leaf', 'CWE', 'SITE_MODIFIER', None),
 'SPS_6': ('leaf', 'CWE', 'COLLECTION_METHOD_MODIFIER_CODE', None),
 'SPS_7': ('leaf', 'CWE', 'SPECIMEN_ROLE', None),
 'SRT': ('sequence', (('SRT_1', (1, 1)), ('SRT_2', (0, 1)))),
 'SRT_1': ('leaf', 'ST', 'SORT_BY_FIELD', None),
 'SRT_2': ('leaf', 'ID', 'SEQUENCING', None),
 'TQ': ('sequence',
        (('TQ_1', (0, 1)),
         ('TQ_2', (0, 1)),
         ('TQ_3', (0, 1)),
         ('TQ_4', (0, 1)),
         ('TQ_5', (0, 1)),
         ('TQ_6', (0, 1)),
         ('TQ_7', (0, 1)),
         ('TQ_8', (0, 1)),
         ('TQ_9', (0, 1)),
         ('TQ_10', (0, 1)),
         ('TQ_11', (0, 1)),
         ('TQ_12', (0, 1)))),
 'TQ_1': ('leaf', 'CQ', 'QUANTITY', None),
 'TQ_10': ('leaf', 'OSD', 'ORDER_SEQUENCING', None),
 'TQ_11': ('leaf', 'CE', 'OCCURRENCE_DURATION', None),
 'TQ_12': ('leaf', 'NM', 'TOTAL_OCCURRENCES', None),
 'TQ_2': ('leaf', 'RI', 'INTERVAL', None),
 'TQ_3': ('leaf', 'ST', 'DURATION', None),
 'TQ_4': ('leaf', 'TS', 'START_DATE_TIME', None),
 'TQ_5': ('leaf', 'TS', 'END_DATE_TIME', None),
 'TQ_6': ('leaf', 'ST', 'PRIORITY', None),
 'TQ_7': ('leaf', 'ST', 'CONDITION', None),
 'TQ_8': ('leaf', 'TX', 'TEXT', None),
 'TQ_9': ('leaf', 'ID', 'CONJUNCTION', None),
 'TS': ('sequence', (('TS_1', (1, 1)), ('TS_2', (0, 1)))),
 'TS_1': ('leaf', 'DTM', 'TIME', None),
 'TS_2': ('leaf', 'ID', 'DEGREE_OF_PRECISION', None),
 'UVC': ('sequence', (('UVC_1', (1, 1)), ('UVC_2', (0, 1)))),
 'UVC_1': ('leaf', 'CNE', 'VALUE_CODE', None),
 'UVC_2': ('leaf', 'MO', 'VALUE_AMOUNT', None),
 'VARIES': None,
 'VH': ('sequence',
        (('VH_1', (0, 1)),
         ('VH_2', (0, 1)),
         ('VH_3', (0, 1)),
         ('VH_4', (0, 1)))),
 'VH_1': ('leaf', 'ID', 'START_DAY_RANGE', None),
 'VH_2': ('leaf', 'ID', 'END_DAY_RANGE', None),
 'VH_3': ('leaf', 'TM', 'START_HOUR_RANGE', None),
 'VH_4': ('leaf', 'TM', 'END_HOUR_RANGE', None),
 'VID': ('sequence',
         (('VID_1', (0, 1)), ('VID_2', (0, 1)), ('VID_3', (0, 1)))),
 'VID_1': ('leaf', 'ID', 'VERSION_ID', None),
 'VID_2': ('leaf', 'CE', 'INTERNATIONALIZATION_CODE', None),
 'VID_3': ('leaf', 'CE', 'INTERNATIONAL_VERSION_ID', None),
 'VR': ('sequence', (('VR_1', (0, 1)), ('VR_2', (0, 1)))),
 'VR_1': ('leaf', 'ST', 'FIRST_DATA_CODE_VALUE', None),
 'VR_2': ('leaf', 'ST', 'LAST_DATA_CODE_VALUE', None),
 'WVI': ('sequence', (('WVI_1', (1, 1)), ('WVI_2', (0, 1)))),
 'WVI_1': ('leaf', 'NM', 'CHANNEL_NUMBER', None),
 'WVI_2': ('leaf', 'ST', 'CHANNEL_NAME', None),
 'WVS': ('sequence', (('WVS_1', (1, 1)), ('WVS_2', (0, 1)))),
 'WVS_1': ('leaf', 'ST', 'SOURCE_ONE_NAME', None),
 'WVS_2': ('leaf', 'ST', 'SOURCE_TWO_NAME', None),
 'XAD': ('sequence',
         (('XAD_1', (0, 1)),
          ('XAD_2', (0, 1)),
          ('XAD_3', (0, 1)),
          ('XAD_4', (0, 1)),
          ('XAD_5', (0, 1)),
          ('XAD_6', (0, 1)),
          ('XAD_7', (0, 1)),
          ('XAD_8', (0, 1)),
          ('XAD_9', (0, 1)),
          ('XAD_10', (0, 1)),
          ('XAD_11', (0, 1)),
          ('XAD_12', (0, 1)),
          ('XAD_13', (0, 1)),
          ('XAD_14', (0, 1)))),
 'XAD_1': ('leaf', 'SAD', 'STREET_ADDRESS', None),
 'XAD_10': ('leaf', 'IS', 'CENSUS_TRACT', None),
 'XAD_11': ('leaf', 'ID', 'ADDRESS_REPRESENTATION_CODE', None),
 'XAD_12': ('leaf', 'DR', 'ADDRESS_VALIDITY_RANGE', None),
 'XAD_13': ('leaf', 'TS', 'EFFECTIVE_DATE', None),
 'XAD_14': ('leaf', 'TS', 'EXPIRATION_DATE', None),
 'XAD_2': ('leaf', 'ST', 'OTHER_DESIGNATION', None),
 'XAD_3': ('leaf', 'ST', 'CITY', None),
 'XAD_4': ('leaf', 'ST', 'STATE_OR_PROVINCE', None),
 'XAD_5': ('leaf', 'ST', 'ZIP_OR_POSTAL_CODE', None),
 'XAD_6': ('leaf', 'ID', 'COUNTRY', None),
 'XAD_7': ('leaf', 'ID', 'ADDRESS_TYPE', None),
 'XAD_8': ('leaf', 'ST', 'OTHER_GEOGRAPHIC_DESIGNATION', None),
 'XAD_9': ('leaf', 'IS', 'COUNTY_PARISH_CODE', None),
 'XCN': ('sequence',
         (('XCN_1', (0, 1)),
          ('XCN_2', (0, 1)),
          ('XCN_3', (0, 1)),
          ('XCN_4', (0, 1)),
          ('XCN_5', (0, 1)),
          ('XCN_6', (0, 1)),
          ('XCN_7', (0, 1)),
          ('XCN_8', (0, 1)),
          ('XCN_9', (0, 1)),
          ('XCN_10', (0, 1)),
          ('XCN_11', (0, 1)),
          ('XCN_12', (0, 1)),
          ('XCN_13', (0, 1)),
          ('XCN_14', (0, 1)),
          ('XCN_15', (0, 1)),
          ('XCN_16', (0, 1)),
          ('XCN_17', (0, 1)),
          ('XCN_18', (0, 1)),
          ('XCN_19', (0, 1)),
          ('XCN_20', (0, 1)),
          ('XCN_21', (0, 1)),
          ('XCN_22', (0, 1)),
          ('XCN_23', (0, 1)))),
 'XCN_1': ('leaf', 'ST', 'ID_NUMBER', None),
 'XCN_10': ('leaf', 'ID', 'NAME_TYPE_CODE', None),
 'XCN_11': ('leaf', 'ST', 'IDENTIFIER_CHECK_DIGIT', None),
 'XCN_12': ('leaf', 'ID', 'CHECK_DIGIT_SCHEME', None),
 'XCN_13': ('leaf', 'ID', 'IDENTIFIER_TYPE_CODE', None),
 'XCN_14': ('leaf', 'HD', 'ASSIGNING_FACILITY', None),
 'XCN_15': ('leaf', 'ID', 'NAME_REPRESENTATION_CODE', None),
 'XCN_16': ('leaf', 'CE', 'NAME_CONTEXT', None),
 'XCN_17': ('leaf', 'DR', 'NAME_VALIDITY_RANGE', None),
 'XCN_18': ('leaf', 'ID', 'NAME_ASSEMBLY_ORDER', None),
 'XCN_19': ('leaf', 'TS', 'EFFECTIVE_DATE', None),
 'XCN_2': ('leaf', 'FN', 'FAMILY_NAME', None),
 'XCN_20': ('leaf', 'TS', 'EXPIRATION_DATE', None),
 'XCN_21': ('leaf', 'ST', 'PROFESSIONAL_SUFFIX', None),
 'XCN_22': ('leaf', 'CWE', 'ASSIGNING_JURISDICTION', None),
 'XCN_23': ('leaf', 'CWE', 'ASSIGNING_AGENCY_OR_DEPARTMENT', None),
 'XCN_3': ('leaf', 'ST', 'GIVEN_NAME', None),
 'XCN_4': ('leaf',
           'ST',
           'SECOND_AND_FURTHER_GIVEN_NAMES_OR_INITIALS_THEREOF',
           None),
 'XCN_5': ('leaf', 'ST', 'SUFFIX_E_G_JR_OR_III', None),
 'XCN_6': ('leaf', 'ST', 'PREFIX_E_G_DR', None),
 'XCN_7': ('leaf', 'IS', 'DEGREE_E_G_MD', None),
 'XCN_8': ('leaf', 'IS', 'SOURCE_TABLE', None),
 'XCN_9': ('leaf', 'HD', 'ASSIGNING_AUTHORITY', None),
 'XON': ('sequence',
         (('XON_1', (0, 1)),
          ('XON_2', (0, 1)),
          ('XON_3', (0, 1)),
          ('XON_4', (0, 1)),
          ('XON_5', (0, 1)),
          ('XON_6', (0, 1)),
          ('XON_7', (0, 1)),
          ('XON_8', (0, 1)),
          ('XON_9', (0, 1)),
          ('XON_10', (0, 1)))),
 'XON_1': ('leaf', 'ST', 'ORGANIZATION_NAME', None),
 'XON_10': ('leaf', 'ST', 'ORGANIZATION_IDENTIFIER', None),
 'XON_2': ('leaf', 'IS', 'ORGANIZATION_NAME_TYPE_CODE', None),
 'XON_3': ('leaf', 'NM', 'ID_NUMBER', None),
 'XON_4': ('leaf', 'NM', 'CHECK_DIGIT', None),
 'XON_5': ('leaf', 'ID', 'CHECK_DIGIT_SCHEME', None),
 'XON_6': ('leaf', 'HD', 'ASSIGNING_AUTHORITY', None),
 'XON_7': ('leaf', 'ID', 'IDENTIFIER_TYPE_CODE', None),
 'XON_8': ('leaf', 'HD', 'ASSIGNING_FACILITY', None),
 'XON_9': ('leaf', 'ID', 'NAME_REPRESENTATION_CODE', None),
 'XPN': ('sequence',
         (('XPN_1', (0, 1)),
          ('XPN_2', (0, 1)),
          ('XPN_3', (0, 1)),
          ('XPN_4', (0, 1)),
          ('XPN_5', (0, 1)),
          ('XPN_6', (0, 1)),
          ('XPN_7', (0, 1)),
          ('XPN_8', (0, 1)),
          ('XPN_9', (0, 1)),
          ('XPN_10', (0, 1)),
          ('XPN_11', (0, 1)),
          ('XPN_12', (0, 1)),
          ('XPN_13', (0, 1)),
          ('XPN_14', (0, 1)))),
 'XPN_1': ('leaf', 'FN', 'FAMILY_NAME', None),
 'XPN_10': ('leaf', 'DR', 'NAME_VALIDITY_RANGE', None),
 'XPN_11': ('leaf', 'ID', 'NAME_ASSEMBLY_ORDER', None),
 'XPN_12': ('leaf', 'TS', 'EFFECTIVE_DATE', None),
 'XPN_13': ('leaf', 'TS', 'EXPIRATION_DATE', None),
 'XPN_14': ('leaf', 'ST', 'PROFESSIONAL_SUFFIX', None),
 'XPN_2': ('leaf', 'ST', 'GIVEN_NAME', None),
 'XPN_3': ('leaf',
           'ST',
           'SECOND_AND_FURTHER_GIVEN_NAMES_OR_INITIALS_THEREOF',
           None),
 'XPN_4': ('leaf', 'ST', 'SUFFIX_E_G_JR_OR_III', None),
 'XPN_5': ('leaf', 'ST', 'PREFIX_E_G_DR', None),
 'XPN_6': ('leaf', 'IS', 'DEGREE_E_G_MD', None),
 'XPN_7': ('leaf', 'ID', 'NAME_TYPE_CODE', None),
 'XPN_8': ('leaf', 'ID', 'NAME_REPRESENTATION_CODE', None),
 'XPN_9': ('leaf', 'CE', 'NAME_CONTEXT', None),
 'XTN': ('sequence',
         (('XTN_1', (0, 1)),
          ('XTN_2', (0, 1)),
          ('XTN_3', (0, 1)),
          ('XTN_4', (0, 1)),
          ('XTN_5', (0, 1)),
          ('XTN_6', (0, 1)),
          ('XTN_7', (0, 1)),
          ('XTN_8', (0, 1)),
          ('XTN_9', (0, 1)),
          ('XTN_10', (0, 1)),
          ('XTN_11', (0, 1)),
          ('XTN_12', (0, 1)))),
 'XTN_1': ('leaf', 'ST', 'TELEPHONE_NUMBER', None),
 'XTN_10': ('leaf', 'ST', 'EXTENSION_PREFIX', None),
 'XTN_11': ('leaf', 'ST', 'SPEED_DIAL_CODE', None),
 'XTN_12': ('leaf', 'ST', 'UNFORMATTED_TELEPHONE_NUMBER', None),
 'XTN_2': ('leaf', 'ID', 'TELECOMMUNICATION_USE_CODE', None),
 'XTN_3': ('leaf', 'ID', 'TELECOMMUNICATION_EQUIPMENT_TYPE', None),
 'XTN_4': ('leaf', 'ST', 'EMAIL_ADDRESS', None),
 'XTN_5': ('leaf', 'NM', 'COUNTRY_CODE', None),
 'XTN_6': ('leaf', 'NM', 'AREA_CITY_CODE', None),
 'XTN_7': ('leaf', 'NM', 'LOCAL_NUMBER', None),
 'XTN_8': ('leaf', 'NM', 'EXTENSION', None),
 'XTN_9': ('leaf', 'ST', 'ANY_TEXT', None)}
