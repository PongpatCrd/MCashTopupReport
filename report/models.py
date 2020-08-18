from django.db import models

# Create your models here.

# ticket_sale
class TblBranch(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    branch_id = models.CharField(db_column='Branch_ID', max_length=2)  # Field name made lowercase.
    complex_id = models.IntegerField(db_column='Complex_ID', blank=True, null=True)  # Field name made lowercase.
    complex_name = models.CharField(db_column='Complex_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    complex_order = models.IntegerField(db_column='Complex_Order', blank=True, null=True)  # Field name made lowercase.
    branchcodevista = models.CharField(db_column='BranchCodeVista', max_length=5, blank=True, null=True)  # Field name made lowercase.
    branch_fullname = models.CharField(db_column='Branch_FullName', max_length=30)  # Field name made lowercase.
    branch_thainame = models.CharField(db_column='Branch_ThaiName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    branch_nickname = models.CharField(db_column='Branch_NickName', max_length=3, blank=True, null=True)  # Field name made lowercase.
    branch_callname = models.CharField(db_column='Branch_CallName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branch_server = models.CharField(db_column='Branch_Server', max_length=25, blank=True, null=True)  # Field name made lowercase.
    branch_trans = models.CharField(db_column='Branch_Trans', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_group = models.IntegerField(db_column='Branch_Group', blank=True, null=True)  # Field name made lowercase.
    branch_program = models.CharField(db_column='Branch_Program', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_dbuser = models.CharField(db_column='Branch_DbUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_dbpass = models.CharField(db_column='Branch_DbPass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_dbname = models.CharField(db_column='Branch_DbName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_dbtype = models.SmallIntegerField(db_column='Branch_DbType', blank=True, null=True)  # Field name made lowercase.
    branch_notheatre = models.IntegerField(db_column='Branch_NoTheatre', blank=True, null=True)  # Field name made lowercase.
    branch_noseat = models.IntegerField(db_column='Branch_NoSeat', blank=True, null=True)  # Field name made lowercase.
    branch_nolane = models.IntegerField(db_column='Branch_NoLane', blank=True, null=True)  # Field name made lowercase.
    branch_noroom = models.IntegerField(db_column='Branch_NoRoom', blank=True, null=True)  # Field name made lowercase.
    branch_nobox = models.IntegerField(db_column='Branch_NoBox', blank=True, null=True)  # Field name made lowercase.
    branch_notable = models.IntegerField(db_column='Branch_NoTable', blank=True, null=True)  # Field name made lowercase.
    branch_noice = models.IntegerField(db_column='Branch_NoIce', blank=True, null=True)  # Field name made lowercase.
    branch_orderbox = models.IntegerField(db_column='Branch_OrderBox', blank=True, null=True)  # Field name made lowercase.
    branch_orderbow = models.IntegerField(db_column='Branch_OrderBow', blank=True, null=True)  # Field name made lowercase.
    branch_db = models.CharField(db_column='Branch_DB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_performancelocation = models.CharField(db_column='Branch_PerformanceLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_location = models.CharField(db_column='Branch_Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_zone = models.CharField(db_column='Branch_Zone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_region = models.CharField(db_column='Branch_Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_conprice = models.CharField(db_column='Branch_ConPrice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_ename = models.CharField(db_column='Branch_EName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    branch_tname = models.CharField(db_column='Branch_TName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_mjbname = models.CharField(db_column='Branch_MJBName', max_length=3, blank=True, null=True)  # Field name made lowercase.
    branch_nickconcert = models.CharField(db_column='Branch_NickConcert', max_length=6, blank=True, null=True)  # Field name made lowercase.
    branch_boxcompany = models.SmallIntegerField(db_column='Branch_BoxCompany', blank=True, null=True)  # Field name made lowercase.
    branch_ipbowl = models.CharField(db_column='Branch_IPBowl', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branch_ipconc = models.CharField(db_column='Branch_IPConc', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branch_ipbowluser = models.CharField(db_column='Branch_IPBowlUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_ipbowlpass = models.CharField(db_column='Branch_IPBowlPass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_dbbowl = models.CharField(db_column='Branch_DBBowl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_dbconc = models.CharField(db_column='Branch_DBConc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_groupbow = models.SmallIntegerField(db_column='Branch_GroupBow', blank=True, null=True)  # Field name made lowercase.
    branch_status = models.SmallIntegerField(db_column='Branch_Status', blank=True, null=True)  # Field name made lowercase.
    branch_bowversion = models.CharField(db_column='Branch_BowVersion', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branch_bowlink = models.CharField(db_column='Branch_BowLink', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branch_locationmjc = models.CharField(db_column='Branch_LocationMJC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    branch_open = models.CharField(db_column='Branch_Open', max_length=8, blank=True, null=True)  # Field name made lowercase.
    branch_close = models.CharField(db_column='Branch_Close', max_length=8, blank=True, null=True)  # Field name made lowercase.
    branch_openbow = models.CharField(db_column='Branch_OpenBow', max_length=8, blank=True, null=True)  # Field name made lowercase.
    branch_contributelocation = models.CharField(db_column='Branch_ContributeLocation', max_length=3, blank=True, null=True)  # Field name made lowercase.
    branch_ipbms = models.CharField(db_column='Branch_IPBMS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchivrstatus = models.CharField(db_column='BranchIVRStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    con_email = models.CharField(db_column='Con_Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bow_status = models.SmallIntegerField(db_column='Bow_Status', blank=True, null=True)  # Field name made lowercase.
    directlineno = models.CharField(db_column='DirectLineNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    directline_server = models.CharField(db_column='DirectLine_Server', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_vistadate = models.CharField(db_column='Branch_VISTADate', max_length=8, blank=True, null=True)  # Field name made lowercase.
    bow_area = models.CharField(db_column='Bow_Area', max_length=10, blank=True, null=True)  # Field name made lowercase.
    branch_servername = models.CharField(db_column='Branch_ServerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kiosk_qty = models.SmallIntegerField(db_column='Kiosk_Qty', blank=True, null=True)  # Field name made lowercase.
    kiosk_std = models.SmallIntegerField(db_column='Kiosk_Std', blank=True, null=True)  # Field name made lowercase.
    kiosk_pro = models.SmallIntegerField(db_column='Kiosk_Pro', blank=True, null=True)  # Field name made lowercase.
    kiosk_photo = models.SmallIntegerField(db_column='Kiosk_Photo', blank=True, null=True)  # Field name made lowercase.
    branch_kiosksaleservername = models.CharField(db_column='Branch_KioskSaleServerName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tbl_Branch'
        unique_together = (('id', 'branch_id'),)
# ticket_sale

# mcash_topup
class TblConfig(models.Model):
    configid = models.AutoField(db_column='ConfigId', primary_key=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId')  # Field name made lowercase.
    configname = models.CharField(db_column='ConfigName', max_length=200)  # Field name made lowercase.
    configdesc = models.TextField(db_column='ConfigDesc')  # Field name made lowercase.
    configvalue = models.CharField(db_column='ConfigValue', max_length=200)  # Field name made lowercase.
    configstatus = models.BooleanField(db_column='ConfigStatus', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Config'


class TblItem(models.Model):
    itemid = models.CharField(db_column='ItemId', max_length=15)  # Field name made lowercase.
    itemdesc = models.CharField(db_column='ItemDesc', max_length=255)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='ItemPrice')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Item'


class TblLogtrans(models.Model):
    logid = models.AutoField(db_column='LogId', primary_key=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId')  # Field name made lowercase.
    functionname = models.CharField(db_column='FunctionName', max_length=200)  # Field name made lowercase.
    requestparam = models.TextField(db_column='RequestParam')  # Field name made lowercase.
    responeparam = models.TextField(db_column='ResponeParam', blank=True, null=True)  # Field name made lowercase.
    rescode = models.CharField(db_column='Rescode', max_length=4)  # Field name made lowercase.
    resmessage = models.TextField(db_column='ResMessage')  # Field name made lowercase.
    resmessagedesc = models.TextField(db_column='ResMessageDesc')  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    logdate = models.DateTimeField(db_column='LogDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LogTrans'


class TblPartner(models.Model):
    partnerid = models.AutoField(db_column='PartnerId', primary_key=True)  # Field name made lowercase.
    partnername = models.CharField(db_column='PartnerName', max_length=200)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=200)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200)  # Field name made lowercase.
    partnerstatus = models.BooleanField(db_column='PartnerStatus', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Partner'


class TblResponsetopuptrans(models.Model):
    transid = models.AutoField(db_column='TransId', primary_key=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId')  # Field name made lowercase.
    txtype = models.CharField(db_column='txType', max_length=4)  # Field name made lowercase.
    sourcetxno = models.CharField(db_column='sourceTxNo', max_length=32)  # Field name made lowercase.
    refno1 = models.CharField(db_column='refNo1', max_length=20)  # Field name made lowercase.
    refno2 = models.CharField(db_column='refNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vistatransno = models.CharField(db_column='vistaTransNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vvmtransno = models.CharField(db_column='vvmTransNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transdate = models.DateTimeField(db_column='TransDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ResponseTopupTrans'


class TblResponseverifytrans(models.Model):
    transid = models.AutoField(db_column='TransId', primary_key=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId')  # Field name made lowercase.
    txtype = models.CharField(db_column='txType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sourcetxno = models.CharField(db_column='sourceTxNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    refno1 = models.CharField(db_column='refNo1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='refNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(blank=True, null=True)
    info1th = models.CharField(db_column='Info1Th', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info1en = models.CharField(db_column='Info1En', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info2th = models.CharField(db_column='Info2Th', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info2en = models.CharField(db_column='Info2En', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info3th = models.CharField(db_column='Info3Th', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info3en = models.CharField(db_column='Info3En', max_length=32, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(max_length=2, blank=True, null=True)
    transdate = models.DateTimeField(db_column='TransDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ResponseVerifyTrans'


class TblTopuptrans(models.Model):
    transid = models.AutoField(db_column='TransId', primary_key=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId')  # Field name made lowercase.
    txtype = models.CharField(db_column='txType', max_length=4)  # Field name made lowercase.
    sourcechannel = models.CharField(db_column='sourceChannel', max_length=3)  # Field name made lowercase.
    sourcetxno = models.CharField(db_column='sourceTxNo', max_length=32)  # Field name made lowercase.
    timestamp = models.CharField(max_length=14)
    bankcode = models.CharField(db_column='bankCode', max_length=3)  # Field name made lowercase.
    profileid = models.CharField(db_column='profileId', max_length=20)  # Field name made lowercase.
    terminal = models.CharField(max_length=11)
    refno1 = models.CharField(db_column='refNo1', max_length=20)  # Field name made lowercase.
    refno2 = models.CharField(db_column='refNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField()
    transdate = models.DateTimeField(db_column='TransDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_TopupTrans'


class TblVerifytrans(models.Model):
    transid = models.AutoField(db_column='TransId', primary_key=True)  # Field name made lowercase.
    partnerid = models.IntegerField(db_column='PartnerId')  # Field name made lowercase.
    txtype = models.CharField(db_column='txType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sourcechannel = models.CharField(db_column='sourceChannel', max_length=3, blank=True, null=True)  # Field name made lowercase.
    sourcetxno = models.CharField(db_column='sourceTxNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(max_length=14, blank=True, null=True)
    bankcode = models.CharField(db_column='bankCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    profileid = models.CharField(db_column='profileId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    terminal = models.CharField(max_length=11, blank=True, null=True)
    refno1 = models.CharField(db_column='refNo1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='refNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField()
    language = models.CharField(max_length=2, blank=True, null=True)
    transdate = models.DateTimeField(db_column='TransDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_VerifyTrans'
# mcash_topup