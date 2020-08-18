from django.db import connections

from report.models import *

def get_branches_vistacode_map():
  temp_tbl_branches = TblBranch.objects.using('ticket_sale').values('branchcodevista', 'branch_callname', 'branch_thainame').exclude(branch_server=None).filter(branch_status=1)
  tbl_branches = []
  for detail in temp_tbl_branches:
    temp = {
      'branchcodevista': detail['branchcodevista'],
      'branch_callname_plus': f"{detail['branch_callname']} {detail['branch_thainame']}"
    }
    tbl_branches.append(temp)
  return tbl_branches

def try_format_time(in_datetime, datetime_format):
  try:
    in_datetime = in_datetime.strftime(datetime_format)
  except:
    in_datetime = None
  return in_datetime

def none_to_empty(value):
  if value == None:
    return ''
  else:
    return value

def get_mcash_topup_report_datas(start_date, end_date, card_number="", status="all"):
  cursor = connections['mcash_topup'].cursor()

  sql = f"\
    SELECT \
      tbl_res_ver.TransDate as ver_trans_date, \
      tbl_res_ver.[refNo1], \
      tbl_partner.[PartnerName], \
      tbl_res_top.[sourceTxNo], \
      tbl_res_top.[refNo2], \
      tbl_res_top.[vistaTransNo], \
      tbl_res_top.[vvmTransNo], \
      CAST(CAST(tbl_res_ver.amount as int) / 100 as DECIMAL(16,2)) as amount, \
      tbl_res_top.TransDate as top_trans_date, \
      tbl_partner.[User] \
    FROM [MCashTopup].[dbo].[tbl_ResponseVerifyTrans] tbl_res_ver (NOLOCK) \
    LEFT JOIN [MCashTopup].[dbo].[tbl_ResponseTopupTrans] tbl_res_top (NOLOCK) \
      ON tbl_res_top.refNo1 = tbl_res_ver.refNo1 \
      AND tbl_res_top.refNo2 = tbl_res_ver.refNo2 \
    JOIN [MCashTopup].[dbo].[tbl_Partner] as tbl_partner (NOLOCK)\
      ON tbl_partner.[PartnerId] = tbl_res_ver.[PartnerId] \
    WHERE tbl_res_ver.TransDate BETWEEN '{start_date}' AND '{end_date}' \
    "

  if card_number:
    sql += f"AND tbl_res_ver.[refNo1] = '{card_number}' "
  
  sql += "ORDER BY tbl_res_ver.TransDate DESC"

  cursor.execute(sql)
  formatted_datas = []
  for row in cursor.fetchall():
    temp = {
      'ver_trans_date': none_to_empty(try_format_time(row[0], '%d/%m/%Y %H:%M:%S')),
      'ref_no1'       : none_to_empty(row[1]),
      'partner_name'  : none_to_empty(row[2]),
      'source_tx_no'  : none_to_empty(row[3]),
      'ref_no2'       : none_to_empty(row[4]),
      'vista_trans_no': none_to_empty(row[5]),
      'vvm_trans_no'  : none_to_empty(row[6]),
      'amount'        : none_to_empty(row[7]),
      'top_trans_date': none_to_empty(try_format_time(row[8], '%d/%m/%Y %H:%M:%S')),
      'user'          : none_to_empty(row[9])
    }

    count_none = row.count(None)
    if count_none == 0:
      temp['status'] = 'completed'
    elif row[6] == None and count_none == 1:
      temp['status'] = 'topup_failed'
    else:
      temp['status'] = 'verify_failed'

    if status == 'all':
      formatted_datas.append(temp)
    elif status == 'completed':
      if temp['status'] == 'completed':
        formatted_datas.append(temp)
    elif status == 'topup_failed':
      if temp['status'] == 'topup_failed':
        formatted_datas.append(temp)
    elif status == 'verify_failed':
      if temp['status'] == 'verify_failed':
        formatted_datas.append(temp)

  return formatted_datas