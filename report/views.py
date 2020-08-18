from django.shortcuts import render
from datetime import datetime, timedelta

from report.models import *
from report.controllers import *

# Create your views here.
def mcash_topup_report(request):
  tbl_branches = get_branches_vistacode_map()

  start_date = request.GET.get('criteria_start_date', '')
  end_date = request.GET.get('criteria_end_date', '')
  card_number = request.GET.get('criteria_card_number', '')
  status = request.GET.get('criteria_status', 'all')

  if start_date and end_date and status:
    start_date = datetime.strptime(start_date, '%d/%m/%Y')
    end_date = datetime.strptime(end_date, '%d/%m/%Y') + timedelta(days=1)

    mcash_topup_report_datas = get_mcash_topup_report_datas(start_date, end_date, card_number, status)
  else:
    mcash_topup_report_datas = []

  context = {
    'tbl_branches'            : tbl_branches,
    'mcash_topup_report_datas': mcash_topup_report_datas,
    'criteria_template'       : 'mcash_topup_report_criteria',
    'response_template'       : 'mcash_topup_report_table',
    'current_criteria_data'   : request.GET
  }
  return render(request, 'report/index.html', context)
