import os
import sys
import csv
import json

import xml.etree.ElementTree as ET

import pandas as pd

################################
######### directories  & paths
################################
# change current directory to script directory INSTEAD of dir where python is called
curr_dir = os.getcwd()
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# home, this project's files
project_dir = os.path.dirname(curr_dir)
# scripts directory, inside of project directory
# DATA directory
data_dir = os.path.join(project_dir, 'data')
# DATA subdirectories
status_dir = os.path.join(data_dir, 'status')
note_dir = os.path.join(data_dir, 'note')
estimate_dir = os.path.join(data_dir, 'estimate')
customDoc_dir = os.path.join(data_dir, 'customDoc')

# all xsds dir & data dictionary dir (xlsx, cvs, json)
xsds_dir = os.path.join(project_dir, 'xsds')
data_dict_dir = os.path.join(project_dir, 'data_dicts')
# XSD files
status_xsd = os.path.join(xsds_dir, 'StandardStatusExport.xsd')


class GenericDataDictionaryClass:
    """This is a representations of a generic class file"""

    def __init__(self, elem, attr, val, desc):
        self.element = elem
        self.attribute = attr
        self.value = val
        self.description = desc

    def __str__(self):
        return """
        element: {}
        attribute: {}
        value: {}
        description: {}
        """.format(self.element, self.attribute, self.value, self.description)


class StatusDataDictClass:
    """This is a representations of the StatusExportDataDict.xlsx file"""

    def __init__(self, elem, attr, val, desc):
        self.element = elem
        self.attribute = attr
        self.value = val
        self.description = desc

    def __str__(self):
        return """
        element: {}
        attribute: {}
        value: {}
        description: {}
        """.format(self.element, self.attribute, self.value, self.description)


class StandardStatus:  # add two (2) fields. One for file name, one for truncated file name
    """This is a instance of the any give STATUS xml file"""

    def __init__(self, contact_name, contact_type, control_point_stamp, control_point_type, phone_extension,
                 phone_number, phone_type, typeofloss_claimnumber,
                 xactnet_info_recipientsxnaddress, xactnet_info_recipientsxm8userid, xactnet_info_transactionid,
                 xactnet_info_origtransactionid):
        self.CONTACT_name = contact_name
        self.CONTACT_type = contact_type
        self.CONTROL_POINT_stamp = control_point_stamp
        self.CONTROL_POINT_type = control_point_type
        self.PHONE_extension = phone_extension
        self.PHONE_number = phone_number
        self.PHONE_type = phone_type
        self.TYPEOFLOSS_claimNumber = typeofloss_claimnumber
        self.XACTNET_INFO_recipientsXNAddress = xactnet_info_recipientsxnaddress
        self.XACTNET_INFO_recipientsXM8UserId = xactnet_info_recipientsxm8userid
        self.XACTNET_INFO_transactionId = xactnet_info_transactionid
        self.XACTNET_INFO_origTransactionId = xactnet_info_origtransactionid

    def __str__(self):
        return """
        CONTACT_name: {}
        CONTACT_type: {}
        CONTROL_POINT_stamp: {}
        CONTROL_POINT_type: {}
        PHONE_extension: {}
        PHONE_number: {}
        PHONE_type: {}
        TYPEOFLOSS_claimNumber: {}
        XACTNET_INFO_recipientsXNAddress: {}
        XACTNET_INFO_recipientsXM8UserId: {}
        XACTNET_INFO_transactionId: {}
        XACTNET_INFO_origTransactionId: {}

        """.format(self.CONTACT_name, self.CONTACT_type, self.CONTROL_POINT_stamp, self.CONTROL_POINT_type,
                   self.PHONE_extension,
                   self.PHONE_number, self.PHONE_type, self.TYPEOFLOSS_claimNumber,
                   self.XACTNET_INFO_recipientsXNAddress,
                   self.XACTNET_INFO_recipientsXM8UserId, self.XACTNET_INFO_transactionId,
                   self.XACTNET_INFO_origTransactionId)


class ActivityDiary:
    """Class for Activity Diary Data Dictionary"""

    def __init__(self):
        self.ACTIVITY_process = activity_process
        self.ACTIVITY_updated = activity_updated
        self.ACTIVITY_activity = activity_activity
        self.ACTIVITY_desc = activity_desc
        self.ACTIVITY_start = activity_start
        self.ACTIVITY_finish = activity_finish
        self.ACTIVITY_remind = activity_remind
        self.ACTIVITY_toDo = activity_todo
        self.CONTROL_POINTS_testAssignment = control_points_testassignment
        self.COVERAGE_LOSS_claimNumber = coverage_loss_claimnumber
        self.EXPENSE_desc = expense_desc
        self.EXPENSE_hours = expense_hours
        self.EXPENSE_amount = expense_amount
        self.EXPENSE_code = expense_code
        self.EXPENSE_codeDesc = expense_codedesc
        self.EXPENSE_miles = expense_miles
        self.EXPENSE_paidByEmp = expense_paidbyemp
        self.EXPENSE_personalCar = expense_personalcar
        self.EXPENSE_noCharge = expense_nocharge
        self.EXPENSE_prorated = expense_prorated
        self.XACTNET_INFO_recipientsXNAddress = xactnet_info_recipientsxnaddress
        self.XACTNET_INFO_originalTransactionId = xactnet_info_originaltransactionid
        self.XACTNET_INFO_transactionId = xactnet_info_transactionid


class CustomDoc:
    """Class for Custom Doc Data Dictionary"""

    def __init__(self):
        self.CONTROL_POINT_stamp = control_point_stamp
        self.CONTROL_POINT_type = control_point_type
        self.CONTROL_POINT_filename = control_point_filename
        self.TYPEOFLOSS_claimNumber = typeofloss_claimnumber
        self.XACTNET_INFO_transactionId = xactnet_info_transactionid


class EstimateGenericRoughDraft:
    """Calss for Estimate Generic Rough Draft"""

    def __init__(self):
        self._majorVersion = _majorversion
        self._minorVersion = _minorversion
        self._transactionId = _transactionid
        self.ADDRESS_zip = address_zip
        self.ADDRESS_type = address_type
        self.ADDRESS_street = address_street
        self.ADDRESS_city = address_city
        self.ADDRESS_state = address_state
        self.ADDRESS_primary = address_primary
        self.PHONE_type = phone_type
        self.PHONE_phone = phone_phone
        self.PHONE_ext = phone_ext
        self.PHONE_primary = phone_primary
        self.CONTACT_type = contact_type
        self.CONTACT_name = contact_name
        self.CONTACT_title = contact_title
        self.CONTACT_company = contact_company
        self.DATES_loss = dates_loss
        self.DATES_inspected = dates_inspected
        self.DATES_completed = dates_completed
        self.DATES_received = dates_received
        self.DATES_entered = dates_entered
        self.DATES_contacted = dates_contacted
        self.EST_CHANGE_reason = est_change_reason
        self.EST_CHANGE_onsite = est_change_onsite
        self.ESTIMATE_INFO_estimateType = estimate_info_estimatetype
        self.ESTIMATE_INFO_deprMat = estimate_info_deprmat
        self.ESTIMATE_INFO_deprNonMat = estimate_info_deprnonmat
        self.ESTIMATE_INFO_deprRemoval = estimate_info_deprremoval
        self.ESTIMATE_INFO_deprOandP = estimate_info_deproandp
        self.ESTIMATE_INFO_deprTaxes = estimate_info_deprtaxes
        self.ESTIMATE_INFO_inspNotPerformed = estimate_info_inspnotperformed
        self.ESTIMATE_INFO_roofDamage = estimate_info_roofdamage
        self.ESTIMATE_INFO_scopeType = estimate_info_scopetype
        self.ESTIMATE_INFO_estimateCount = estimate_info_estimatecount
        self.ESTIMATE_INFO_onsite = estimate_info_onsite
        self.ESTIMATE_INFO_printOnsite = estimate_info_printonsite
        self.ESTIMATE_INFO_onsitePayment = estimate_info_onsitepayment
        self.ESTIMATE_INFO_estimatedOnsite = estimate_info_estimatedonsite
        self.ESTIMATE_INFO_isTotalLoss = estimate_info_istotalloss
        self.ESTIMATE_INFO_backInProgress = estimate_info_backinprogress
        self.ESTIMATE_INFO_afo = estimate_info_afo
        self.ESTIMATE_INFO_xsImported = estimate_info_xsimported
        self.ESTIMATE_INFO_recipientsXNAddress = estimate_info_recipientsxnaddress
        self.ESTIMATE_INFO_causeOfLoss = estimate_info_causeofloss
        self.ESTIMATE_INFO_otherCause = estimate_info_othercause
        self.ESTIMATE_INFO_rotationTrade = estimate_info_rotationtrade
        self.ESTIMATE_INFO_carrierId = estimate_info_carrierid
        self.ESTIMATE_INFO_originalTransactionId = estimate_info_originaltransactionid
        self.ESTIMATE_INFO_usedAerialSketch = estimate_info_usedaerialsketch
        self.ESTIMATE_INFO_policyNumber = estimate_info_policynumber
        self.ESTIMATE_INFO_claimNumber = estimate_info_claimnumber
        self.ESTIMATE_INFO_estimateName = estimate_info_estimatename
        self.ESTIMATE_INFO_insuredName = estimate_info_insuredname
        self.ESTIMATE_INFO_priceList = estimate_info_pricelist
        self.ESTIMATE_INFO_laborEff = estimate_info_laboreff
        self.ESTIMATE_INFO_typeOfLoss = estimate_info_typeofloss
        self.ESTIMATE_INFO_laborCostModel = estimate_info_laborcostmodel
        self.ESTIMATE_INFO_waterLossCategory = estimate_info_waterlosscategory
        self.ESTIMATE_INFO_waterLossClass = estimate_info_waterlossclass
        self.ADDRESS_zip = address_zip
        self.ADDRESS_type = address_type
        self.ADDRESS_street = address_street
        self.ADDRESS_city = address_city
        self.ADDRESS_state = address_state
        self.ADDRESS_primary = address_primary
        self.PHONE_type = phone_type
        self.PHONE_phone = phone_phone
        self.PHONE_ext = phone_ext
        self.PHONE_primary = phone_primary
        self.OPENING_STATEMENT_ = opening_statement_
        self.PERMIT_FEE_desc = permit_fee_desc
        self.PERMIT_FEE_amount = permit_fee_amount
        self.SALES_TAX_desc = sales_tax_desc
        self.SALES_TAX_rate = sales_tax_rate
        self.SALES_TAX_base = sales_tax_base
        self.SALES_TAX_amount = sales_tax_amount
        self.SALES_TAX_taxOnDepr = sales_tax_taxondepr
        self.SALES_TAX_taxOnRecDepr = sales_tax_taxonrecdepr
        self.SIGNATURE_estimator = signature_estimator
        self.SIGNATURE_estimatorTitle = signature_estimatortitle
        self.PAYMENT_TRACKER_ptEstValue = payment_tracker_ptestvalue
        self.PAYMENT_TRACKER_ptNumItemActs = payment_tracker_ptnumitemacts
        self.PAYMENT_TRACKER_ptItemsWithRemaining = payment_tracker_ptitemswithremaining
        self.PAYMENT_TRACKER_ptTotalPaid = payment_tracker_pttotalpaid
        self.PAYMENT_TRACKER_ptRecoverableDep = payment_tracker_ptrecoverabledep
        self.PAYMENT_TRACKER_ptNonRecoverableDep = payment_tracker_ptnonrecoverabledep
        self.PAYMENT_TRACKER_ptEstRemaining = payment_tracker_ptestremaining
        self.PAYMENT_TRACKER_ptNumItemOverrides = payment_tracker_ptnumitemoverrides
        self.PAYMENT_TRACKER_ptItemOverrideAmt = payment_tracker_ptitemoverrideamt
        self.FEES_NOTE_ = fees_note_
        self.OVERHEAD_rate = overhead_rate
        self.OVERHEAD_base = overhead_base
        self.OVERHEAD_amount = overhead_amount
        self.PROFIT_rate = profit_rate
        self.PROFIT_base = profit_base
        self.PROFIT_amount = profit_amount
        self.SUBLIMIT_INFO_desc = sublimit_info_desc
        self.SUBLIMIT_INFO_singleItemLimit = sublimit_info_singleitemlimit
        self.SUBLIMIT_INFO_aggLimit = sublimit_info_agglimit
        self.SUBLIMIT_INFO_acv = sublimit_info_acv
        self.SUBLIMIT_INFO_rc = sublimit_info_rc
        self.SUBLIMIT_INFO_overage = sublimit_info_overage
        self.TOTALS_permit = totals_permit
        self.TOTALS_bscTotal = totals_bsctotal
        self.TOTALS_recDepr = totals_recdepr
        self.TOTALS_nonRecDepr = totals_nonrecdepr
        self.TOTALS_actualRecDepr = totals_actualrecdepr
        self.TOTALS_netClaim = totals_netclaim
        self.TOTALS_fullDeduct = totals_fulldeduct
        self.TOTALS_fullSalvRet = totals_fullsalvret
        self.TOTALS_fullResidualDeduct = totals_fullresidualdeduct
        self.TOTALS_residualDeduct = totals_residualdeduct
        self.TOTALS_fullResidualSalvRet = totals_fullresidualsalvret
        self.TOTALS_residualSalvRet = totals_residualsalvret
        self.TOTALS_netClaimIfRec = totals_netclaimifrec
        self.TOTALS_acvCoins = totals_acvcoins
        self.TOTALS_fullACVCoins = totals_fullacvcoins
        self.TOTALS_replCostCoins = totals_replcostcoins
        self.TOTALS_fullReplCostCoins = totals_fullreplcostcoins
        self.TOTALS_fullAmtOverLimits = totals_fullamtoverlimits
        self.TOTALS_residualAmtOverLimits = totals_residualamtoverlimits
        self.TOTALS_fullResAmtOverLimits = totals_fullresamtoverlimits
        self.TOTALS_priorPmtsAdj = totals_priorpmtsadj
        self.TOTALS_priorPmtsResidual = totals_priorpmtsresidual
        self.TOTALS_priorPmtsResidualAdj = totals_priorpmtsresidualadj
        self.TOTALS_settlementFactor = totals_settlementfactor
        self.TOTALS_subtotal = totals_subtotal
        self.TOTALS_lineItemTotal = totals_lineitemtotal
        self.TOTALS_rcv = totals_rcv
        self.TOTALS_acv = totals_acv
        self.TOTALS_directReplacement = totals_directreplacement
        self.TOTALS_directReplacementOwed = totals_directreplacementowed
        self.TOTALS_priorPmts = totals_priorpmts
        self.TOTALS_insuranceToValue = totals_insurancetovalue
        self.TOTALS_deductible = totals_deductible
        self.TOTALS_amtOverLimits = totals_amtoverlimits
        self.TOTALS_salvRetention = totals_salvretention
        self.SALES_TAX_desc = sales_tax_desc
        self.SALES_TAX_rate = sales_tax_rate
        self.SALES_TAX_base = sales_tax_base
        self.SALES_TAX_amount = sales_tax_amount
        self.SALES_TAX_taxOnDepr = sales_tax_taxondepr
        self.SALES_TAX_taxOnRecDepr = sales_tax_taxonrecdepr
        self.SALES_TAX_taxOP = sales_tax_taxop
        self.MAX_ADDL_AMTS_lineItemTotal = max_addl_amts_lineitemtotal
        self.MAX_ADDL_AMTS_subtotal = max_addl_amts_subtotal
        self.MAX_ADDL_AMTS_totalPaidWhenIncurred = max_addl_amts_totalpaidwhenincurred
        self.MAX_ADDL_AMTS_bscAdjustment = max_addl_amts_bscadjustment
        self.MAX_ADDL_AMTS_overhead = max_addl_amts_overhead
        self.MAX_ADDL_AMTS_profit = max_addl_amts_profit
        self.MAX_ADDL_AMTS_rcv = max_addl_amts_rcv
        self.MAX_ADDL_AMTS_rcvPWI = max_addl_amts_rcvpwi
        self.MAX_ADDL_AMTS_amountOverLimit = max_addl_amts_amountoverlimit
        self.MAX_ADDL_AMTS_amountOverLimitToDeduct = max_addl_amts_amountoverlimittodeduct
        self.MAX_ADDL_AMTS_maxAddlAmount = max_addl_amts_maxaddlamount
        self.MAX_ADDL_AMTS_fullResidualCoinsPWI = max_addl_amts_fullresidualcoinspwi
        self.MAX_ADDL_AMTS_residualCoinsPWI = max_addl_amts_residualcoinspwi
        self.MAX_ADDL_AMTS_fullSalvageRetentionPWI = max_addl_amts_fullsalvageretentionpwi
        self.MAX_ADDL_AMTS_salvageRetentionPWI = max_addl_amts_salvageretentionpwi
        self.MAX_ADDL_AMTS_fullAdvancePaymentsResidualPWI = max_addl_amts_fulladvancepaymentsresidualpwi
        self.MAX_ADDL_AMTS_advancePaymentsResidualPWI = max_addl_amts_advancepaymentsresidualpwi
        self.MAX_ADDL_AMTS_fullDeductResidualPWI = max_addl_amts_fulldeductresidualpwi
        self.MAX_ADDL_AMTS_deductResidualPWI = max_addl_amts_deductresidualpwi
        self.LOSS_DATA_rcl = loss_data_rcl
        self.LOSS_DATA_bd = loss_data_bd
        self.LOSS_DATA_acvLoss = loss_data_acvloss
        self.LOSS_DATA_nonRecDeprec = loss_data_nonrecdeprec
        self.LOSS_DATA_deductApplied = loss_data_deductapplied
        self.LOSS_DATA_insCarried = loss_data_inscarried
        self.LOSS_DATA_rcvInsCarried = loss_data_rcvinscarried
        self.LOSS_DATA_acvInsCarried = loss_data_acvinscarried
        self.LOSS_DATA_adjLossAmt = loss_data_adjlossamt
        self.LOSS_DATA_potentialSuppClaim = loss_data_potentialsuppclaim
        self.LOSS_DATA_total = loss_data_total
        self.LOSS_DATA_acvClaim = loss_data_acvclaim
        self.LOSS_DATA_rcvClaim = loss_data_rcvclaim
        self.LOSS_DATA_valACV = loss_data_valacv
        self.LOSS_DATA_valRCV = loss_data_valrcv
        self.LOSS_DATA_salvage = loss_data_salvage
        self.LOSS_DATA_directReplacement = loss_data_directreplacement
        self.LOSS_DATA_priorPmts = loss_data_priorpmts
        self.LOSS_DATA_coins = loss_data_coins
        self.LOSS_DATA_coinsFormula = loss_data_coinsformula
        self.LOSS_DATA_overLimits = loss_data_overlimits
        self.COVERAGE_policyDeductible = coverage_policydeductible
        self.COVERAGE_deductibleCredit = coverage_deductiblecredit
        self.COVERAGE_deductible = coverage_deductible
        self.COVERAGE_coverageName = coverage_coveragename
        self.COVERAGE_id = coverage_id
        self.COVERAGE_coverageType = coverage_coveragetype
        self.ROOM_INFO_sketchCeiling = room_info_sketchceiling
        self.ROOM_INFO_shape = room_info_shape
        self.ROOM_INFO_dimString = room_info_dimstring
        self.ROOM_INFO_sketchThumbnailId = room_info_sketchthumbnailid
        self.MISS_WALL_qty = miss_wall_qty
        self.MISS_WALL_dimString = miss_wall_dimstring
        self.MISS_WALL_opensInto = miss_wall_opensinto
        self.MISS_WALL_type = miss_wall_type
        self.ROOM_DIM_VARS_sfWalls = room_dim_vars_sfwalls
        self.ROOM_DIM_VARS_sfCeiling = room_dim_vars_sfceiling
        self.ROOM_DIM_VARS_sfWallsCeiling = room_dim_vars_sfwallsceiling
        self.ROOM_DIM_VARS_sfFloor = room_dim_vars_sffloor
        self.ROOM_DIM_VARS_syFloor = room_dim_vars_syfloor
        self.ROOM_DIM_VARS_lfFloorPerim = room_dim_vars_lffloorperim
        self.ROOM_DIM_VARS_sfLongWall = room_dim_vars_sflongwall
        self.ROOM_DIM_VARS_sfShortWall = room_dim_vars_sfshortwall
        self.ROOM_DIM_VARS_lfCeilingPerim = room_dim_vars_lfceilingperim
        self.ROOM_DIM_VARS_sfSkRoof = room_dim_vars_sfskroof
        self.ROOM_DIM_VARS_skRoofSquares = room_dim_vars_skroofsquares
        self.ROOM_DIM_VARS_lfSkRoofPerim = room_dim_vars_lfskroofperim
        self.ROOM_DIM_VARS_lfSkRoofRidge = room_dim_vars_lfskroofridge
        self.ROOM_DIM_VARS_lfSkRoofHip = room_dim_vars_lfskroofhip
        self.MISS_WALL_qty = miss_wall_qty
        self.MISS_WALL_dimString = miss_wall_dimstring
        self.MISS_WALL_opensInto = miss_wall_opensinto
        self.MISS_WALL_type = miss_wall_type
        self.SUBROOM_subroomNum = subroom_subroomnum
        self.SUBROOM_desc = subroom_desc
        self.SUBROOM_shape = subroom_shape
        self.SUBROOM_dimString = subroom_dimstring
        self.ROOM_DIM_VARS_sfWalls = room_dim_vars_sfwalls
        self.ROOM_DIM_VARS_sfCeiling = room_dim_vars_sfceiling
        self.ROOM_DIM_VARS_sfWallsCeiling = room_dim_vars_sfwallsceiling
        self.ROOM_DIM_VARS_sfFloor = room_dim_vars_sffloor
        self.ROOM_DIM_VARS_syFloor = room_dim_vars_syfloor
        self.ROOM_DIM_VARS_lfFloorPerim = room_dim_vars_lffloorperim
        self.ROOM_DIM_VARS_sfLongWall = room_dim_vars_sflongwall
        self.ROOM_DIM_VARS_sfShortWall = room_dim_vars_sfshortwall
        self.ROOM_DIM_VARS_lfCeilingPerim = room_dim_vars_lfceilingperim
        self.ROOM_DIM_VARS_sfSkRoof = room_dim_vars_sfskroof
        self.ROOM_DIM_VARS_skRoofSquares = room_dim_vars_skroofsquares
        self.ROOM_DIM_VARS_lfSkRoofPerim = room_dim_vars_lfskroofperim
        self.ROOM_DIM_VARS_lfSkRoofRidge = room_dim_vars_lfskroofridge
        self.ROOM_DIM_VARS_lfSkRoofHip = room_dim_vars_lfskroofhip
        self.ITEM_ACT_act = item_act_act
        self.ITEM_ACT_labUnit = item_act_labunit
        self.ITEM_ACT_matUnit = item_act_matunit
        self.ITEM_ACT_equUnit = item_act_equunit
        self.ITEM_ACT_mktUnit = item_act_mktunit
        self.ITEM_ACT_trade = item_act_trade
        self.ITEM_ACT_tax = item_act_tax
        self.ITEM_ACT_addons = item_act_addons
        self.ITEM_ACT_deprTotal = item_act_deprtotal
        self.ITEM_ACT_acvTotal = item_act_acvtotal
        self.ITEM_ACT_rcvTotal = item_act_rcvtotal
        self.ITEM_NOTE = item_note
        self.ITEM_actPrefix = item_actprefix
        self.ITEM_isHomeowner = item_ishomeowner
        self.ITEM_isCredit = item_iscredit
        self.ITEM_containsBSCFactoredIn = item_containsbscfactoredin
        self.ITEM_containsBSCDontApply = item_containsbscdontapply
        self.ITEM_jobTaxType = item_jobtaxtype
        self.ITEM_laborTotal = item_labortotal
        self.ITEM_laborBase = item_laborbase
        self.ITEM_laborBurden = item_laborburden
        self.ITEM_laborMarkup = item_labormarkup
        self.ITEM_laborHours = item_laborhours
        self.ITEM_material = item_material
        self.ITEM_equipment = item_equipment
        self.ITEM_marketCond = item_marketcond
        self.ITEM_acv = item_acv
        self.ITEM_lineNum = item_linenum
        self.ITEM_sublimitName = item_sublimitname
        self.ITEM_tax = item_tax
        self.ITEM_addons = item_addons
        self.ITEM_deprTotal = item_deprtotal
        self.ITEM_acvTotal = item_acvtotal
        self.ITEM_rcvTotal = item_rcvtotal
        self.ITEM_isPartOfInitSettle = item_ispartofinitsettle
        self.ITEM_type = item_type
        self.ITEM_cat = item_cat
        self.ITEM_sel = item_sel
        self.ITEM_act = item_act
        self.ITEM_desc = item_desc
        self.ITEM_descChanged = item_descchanged
        self.ITEM_calc = item_calc
        self.ITEM_qty = item_qty
        self.ITEM_unit = item_unit
        self.ITEM_unitChanged = item_unitchanged
        self.ITEM_remove = item_remove
        self.ITEM_replace = item_replace
        self.ITEM_total = item_total
        self.ITEM_isExempt = item_isexempt
        self.ITEM_isNonOP = item_isnonop
        self.ITEM_priceNote = item_pricenote
        self.ITEM_priceChanged = item_pricechanged
        self.ITEM_deprType = item_deprtype
        self.ITEM_recoverable = item_recoverable
        self.ITEM_deprUse = item_depruse
        self.ITEM_age = item_age
        self.ITEM_lifeExp = item_lifeexp
        self.ITEM_coverageName = item_coveragename
        self.ITEM_originalVendor = item_originalvendor
        self.ITEMS_total = items_total
        self.AREA_DIM_VARS_sfSkFloor = area_dim_vars_sfskfloor
        self.AREA_DIM_VARS_sfSkTotalFloor = area_dim_vars_sfsktotalfloor
        self.AREA_DIM_VARS_sfSkIntWall = area_dim_vars_sfskintwall
        self.AREA_DIM_VARS_sfSkExtWall = area_dim_vars_sfskextwall
        self.AREA_DIM_VARS_lfSkExtWallPerim = area_dim_vars_lfskextwallperim
        self.AREA_DIM_VARS_sfWalls = area_dim_vars_sfwalls
        self.AREA_DIM_VARS_sfCeiling = area_dim_vars_sfceiling
        self.AREA_DIM_VARS_sfWallsCeiling = area_dim_vars_sfwallsceiling
        self.AREA_DIM_VARS_sfFloor = area_dim_vars_sffloor
        self.AREA_DIM_VARS_syFloor = area_dim_vars_syfloor
        self.AREA_DIM_VARS_lfFloorPerim = area_dim_vars_lffloorperim
        self.AREA_DIM_VARS_sfLongWall = area_dim_vars_sflongwall
        self.AREA_DIM_VARS_sfShortWall = area_dim_vars_sfshortwall
        self.AREA_DIM_VARS_lfCeilingPerim = area_dim_vars_lfceilingperim
        self.AREA_DIM_VARS_sfSkRoof = area_dim_vars_sfskroof
        self.AREA_DIM_VARS_skRoofSquares = area_dim_vars_skroofsquares
        self.AREA_DIM_VARS_lfSkRoofPerim = area_dim_vars_lfskroofperim
        self.AREA_DIM_VARS_lfSkRoofRidge = area_dim_vars_lfskroofridge
        self.AREA_DIM_VARS_lfSkRoofHip = area_dim_vars_lfskroofhip
        self.GROUP_tax = group_tax
        self.GROUP_addons = group_addons
        self.GROUP_deprTotal = group_deprtotal
        self.GROUP_acvTotal = group_acvtotal
        self.GROUP_rcvTotal = group_rcvtotal
        self.GROUP_desc = group_desc
        self.GROUP_total = group_total
        self.PERMIT_FEE_desc = permit_fee_desc
        self.PERMIT_FEE_amount = permit_fee_amount
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.BSC_ITEM_laborHours = bsc_item_laborhours
        self.BSC_ITEM_isNonOP = bsc_item_isnonop
        self.BSC_ITEM_isExempt = bsc_item_isexempt
        self.BSC_ITEM_appliesType = bsc_item_appliestype
        self.BSC_ITEM_desc = bsc_item_desc
        self.BSC_ITEM_tradeCode = bsc_item_tradecode
        self.BSC_ITEM_amount = bsc_item_amount
        self.BSC_ITEM_qtyChanged = bsc_item_qtychanged
        self.BSC_ITEMS_bscTotal = bsc_items_bsctotal
        self.COV_AMOUNTS_desc = cov_amounts_desc
        self.COV_AMOUNTS_total = cov_amounts_total
        self.COV_AMOUNTS_grandTotal = cov_amounts_grandtotal
        self.COV_AMOUNTS_totalPct = cov_amounts_totalpct
        self.COV_AMOUNTS_grandTotalPct = cov_amounts_grandtotalpct
        self.COV_BREAKDOWN_grandTotal = cov_breakdown_grandtotal
        self.COV_BREAKDOWN_total = cov_breakdown_total
        self.LINE_ITEM_DETAIL_permit = line_item_detail_permit
        self.LINE_ITEM_DETAIL_total = line_item_detail_total
        self.LINE_ITEM_DETAIL_homeownerTotal = line_item_detail_homeownertotal
        self.LINE_ITEM_DETAIL_contractorTotal = line_item_detail_contractortotal
        self.RECAP_BY_ROOM_name = recap_by_room_name
        self.RECAP_BY_ROOM_rate = recap_by_room_rate
        self.RECAP_BY_ROOM_amount = recap_by_room_amount
        self.RECAP_BSC_TOTAL_desc = recap_bsc_total_desc
        self.RECAP_BSC_TOTAL_percentage = recap_bsc_total_percentage
        self.RECAP_BSC_TOTAL_rcv = recap_bsc_total_rcv
        self.RECAP_BSC_TOTAL_acv = recap_bsc_total_acv
        self.RECAP_BSC_TOTAL_deprec = recap_bsc_total_deprec
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.RECAP_GROUP_subtotal = recap_group_subtotal
        self.RECAP_GROUP_subtotalPercentage = recap_group_subtotalpercentage
        self.RECAP_GROUP_items = recap_group_items
        self.RECAP_GROUP_itemsPercentage = recap_group_itemspercentage
        self.RECAP_GROUP_desc = recap_group_desc
        self.RECAP_BY_ROOM_total = recap_by_room_total
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.CATEGORY_desc = category_desc
        self.CATEGORY_percentage = category_percentage
        self.CATEGORY_rcv = category_rcv
        self.CATEGORY_acv = category_acv
        self.CATEGORY_deprec = category_deprec
        self.OP_ITEMS_subtotalRCV = op_items_subtotalrcv
        self.OP_ITEMS_subtotalPercentage = op_items_subtotalpercentage
        self.OP_ITEMS_subtotalDeprec = op_items_subtotaldeprec
        self.OP_ITEMS_subtotalACV = op_items_subtotalacv
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.CATEGORY_desc = category_desc
        self.CATEGORY_percentage = category_percentage
        self.CATEGORY_rcv = category_rcv
        self.CATEGORY_acv = category_acv
        self.CATEGORY_deprec = category_deprec
        self.NON_OP_ITEMS_subtotalRCV = non_op_items_subtotalrcv
        self.NON_OP_ITEMS_subtotalPercentage = non_op_items_subtotalpercentage
        self.NON_OP_ITEMS_subtotalDeprec = non_op_items_subtotaldeprec
        self.NON_OP_ITEMS_subtotalACV = non_op_items_subtotalacv
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.RECAP_BSC_TOTAL_desc = recap_bsc_total_desc
        self.RECAP_BSC_TOTAL_percentage = recap_bsc_total_percentage
        self.RECAP_BSC_TOTAL_rcv = recap_bsc_total_rcv
        self.RECAP_BSC_TOTAL_acv = recap_bsc_total_acv
        self.RECAP_BSC_TOTAL_deprec = recap_bsc_total_deprec
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.RECAP_PERMIT_desc = recap_permit_desc
        self.RECAP_PERMIT_percentage = recap_permit_percentage
        self.RECAP_PERMIT_rcv = recap_permit_rcv
        self.RECAP_PERMIT_acv = recap_permit_acv
        self.RECAP_PERMIT_deprec = recap_permit_deprec
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.OVERHEAD_rate = overhead_rate
        self.OVERHEAD_desc = overhead_desc
        self.OVERHEAD_percentage = overhead_percentage
        self.OVERHEAD_rcv = overhead_rcv
        self.OVERHEAD_acv = overhead_acv
        self.OVERHEAD_deprec = overhead_deprec
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.PROFIT_rate = profit_rate
        self.PROFIT_desc = profit_desc
        self.PROFIT_percentage = profit_percentage
        self.PROFIT_rcv = profit_rcv
        self.PROFIT_acv = profit_acv
        self.PROFIT_deprec = profit_deprec
        self.COV_name = cov_name
        self.COV_rate = cov_rate
        self.COV_amount = cov_amount
        self.SALES_TAX_rate = sales_tax_rate
        self.SALES_TAX_desc = sales_tax_desc
        self.SALES_TAX_percentage = sales_tax_percentage
        self.SALES_TAX_rcv = sales_tax_rcv
        self.SALES_TAX_acv = sales_tax_acv
        self.SALES_TAX_deprec = sales_tax_deprec
        self.RECAP_BY_CATEGORY_subtotalRCV = recap_by_category_subtotalrcv
        self.RECAP_BY_CATEGORY_subtotalACV = recap_by_category_subtotalacv
        self.RECAP_BY_CATEGORY_subtotalDeprec = recap_by_category_subtotaldeprec
        self.OVERHEAD_rate = overhead_rate
        self.OVERHEAD_amount = overhead_amount
        self.PROFIT_rate = profit_rate
        self.PROFIT_amount = profit_amount
        self.TAX_DETAIL_desc = tax_detail_desc
        self.TAX_DETAIL_rate = tax_detail_rate
        self.TAX_DETAIL_taxNum = tax_detail_taxnum
        self.TAX_DETAIL_amount = tax_detail_amount
        self.TAX_AMOUNT_taxNum = tax_amount_taxnum
        self.TAX_AMOUNT_amount = tax_amount_amount
        self.LINE_ITEMS_overhead = line_items_overhead
        self.LINE_ITEMS_profit = line_items_profit
        self.TAX_AMOUNT_taxNum = tax_amount_taxnum
        self.TAX_AMOUNT_amount = tax_amount_amount
        self.ADDL_CHARGES_overhead = addl_charges_overhead
        self.ADDL_CHARGES_profit = addl_charges_profit
        self.TAX_AMOUNT_taxNum = tax_amount_taxnum
        self.TAX_AMOUNT_amount = tax_amount_amount
        self.BASE_SERVICE_CHARGES_overhead = base_service_charges_overhead
        self.BASE_SERVICE_CHARGES_profit = base_service_charges_profit
        self.CLOSING_STATEMENT_ = closing_statement_
        self.HEADER_ = header_
        self.HEADER_COMP_INFO = header_comp_info
        self.HEADER_compName = header_compname
        self.HEADER_dateCreated = header_datecreated
        self.PT_PAYMENT_NOTE = pt_payment_note
        self.PT_PAYMENT_date = pt_payment_date
        self.PT_PAYMENT_checkNum = pt_payment_checknum
        self.PT_PAYMENT_type = pt_payment_type
        self.PT_PAYMENT_userID = pt_payment_userid
        self.PT_PAYMENT_voided = pt_payment_voided
        self.PT_PAYMENT_recut = pt_payment_recut
        self.PT_PAYMENT_rcDeferredAmount = pt_payment_rcdeferredamount
        self.PT_PAYMENT_acvAmount = pt_payment_acvamount
        self.PT_TOTALS_ptALEPaid = pt_totals_ptalepaid
        self.PT_TOTALS_ptNumPmts = pt_totals_ptnumpmts


class EstimateStandardCarrier:
    """Class for Estimate StandardCarrier Data Dictionary"""

    def __int__(self):
        self.ACTIVITY_process = activity_process
        self.ACTIVITY_activity = activity_activity
        self.ACTIVITY_start = activity_start
        self.ACTIVITY_finish = activity_finish
        self.ACTIVITY_updated = activity_updated
        self.ACTIVITY_desc = activity_desc
        self.ACTIVITY_longDesc = activity_longdesc
        self.ACTIVITY_remind = activity_remind
        self.ACTIVITY_todo = activity_todo
        self.ADDRESS_city = address_city
        self.ADDRESS_country = address_country
        self.ADDRESS_county = address_county
        self.ADDRESS_lat = address_lat
        self.ADDRESS_lon = address_lon
        self.ADDRESS_postal = address_postal
        self.ADDRESS_primary = address_primary
        self.ADDRESS_state = address_state
        self.ADDRESS_street = address_street
        self.ADDRESS_street2 = address_street2
        self.ADDRESS_street3 = address_street3
        self.ADDRESS_type = address_type
        self.ADM_agentCode = adm_agentcode
        self.ADM_agentName = adm_agentname
        self.ADM_branchNumber = adm_branchnumber
        self.ADM_clientNumber = adm_clientnumber
        self.ADM_dateEntered = adm_dateentered
        self.ADM_dateProjCompleted = adm_dateprojcompleted
        self.ADM_dateJobCompleted = adm_datejobcompleted
        self.ADM_dateContacted = adm_datecontacted
        self.ADM_dateInspected = adm_dateinspected
        self.ADM_dateOfLoss = adm_dateofloss
        self.ADM_dateReceived = adm_datereceived
        self.ADM_fileNumber = adm_filenumber
        self.ADM_onsite = adm_onsite
        self.ADM_estimatedOnsite = adm_estimatedonsite
        self.ADM_printOnsite = adm_printonsite
        self.ADM_onsitePayment = adm_onsitepayment
        self.ADM_numRmsAffected = adm_numrmsaffected
        self.ADM_denial = adm_denial
        self.ADM_denialExplanation = adm_denialexplanation
        self.ADM_dateProjectedComplete = adm_dateprojectedcomplete
        self.ADM_dateProjectedStart = adm_dateprojectedstart
        self.ADM_gt30WorkingDays = adm_gt30workingdays
        self.ADM_gt500PersonDays = adm_gt500persondays
        self.ADMIN_INFO_branch = admin_info_branch
        self.ADMIN_INFO_accessName = admin_info_accessname
        self.ADMIN_INFO_accessPhone = admin_info_accessphone
        self.ADMIN_INFO_accessPhoneExt = admin_info_accessphoneext
        self.ATT_FILE_fileName = att_file_filename
        self.ATT_FILE_fileDesc = att_file_filedesc
        self.ATT_FILE_fileType = att_file_filetype
        self.ATT_FILE_fileDate = att_file_filedate
        self.ATT_FILE_approvalStatus = att_file_approvalstatus
        self.COL_desc = col_desc
        self.COL_otherCause = col_othercause
        self.COMPANY_name = company_name
        self.CONTACT_name = contact_name
        self.CONTACT_qcode = contact_qcode
        self.CONTACT_type = contact_type
        self.CONTACT_goesBy = contact_goesby
        self.CONTACT_position = contact_position
        self.CONTACT_mortgageHolder = contact_mortgageholder
        self.CONTACT_mortgageLoanNum = contact_mortgageloannum
        self.CONTACT_birthDate = contact_birthdate
        self.CONTACT_reference = contact_reference
        self.CONTACT_language = contact_language
        self.CONTACT_title = contact_title
        self.CONTACT_claimUnit = contact_claimunit
        self.CONTROL_POINT_reservation = control_point_reservation
        self.CONTROL_POINT_stamp = control_point_stamp
        self.CONTROL_POINT_type = control_point_type
        self.CONTROL_POINT_user = control_point_user
        self.CONTROL_POINT_userNumber = control_point_usernumber
        self.CONTROL_POINT_userId = control_point_userid
        self.CONTROL_POINT_flags = control_point_flags
        self.CONTROL_POINT_amount = control_point_amount
        self.CONTROL_POINT_userLastName = control_point_userlastname
        self.CONTROL_POINT_userFirstName = control_point_userfirstname
        self.CONTROL_POINTS_grossEstimate = control_points_grossestimate
        self.CONTROL_POINTS_bill = control_points_bill
        self.CONTROL_POINTS_referral = control_points_referral
        self.CONTROL_POINTS_testAssignment = control_points_testassignment
        self.COVERAGE_applyTo = coverage_applyto
        self.COVERAGE_coins = coverage_coins
        self.COVERAGE_covName = coverage_covname
        self.COVERAGE_covType = coverage_covtype
        self.COVERAGE_deductible = coverage_deductible
        self.COVERAGE_id = coverage_id
        self.COVERAGE_policyLimit = coverage_policylimit
        self.COVERAGE_reserveAmt = coverage_reserveamt
        self.COVERAGE_sharedLimitRefID = coverage_sharedlimitrefid
        self.COVERAGE_sharedDeductibleRefID = coverage_shareddeductiblerefid
        self.COVERAGE_addlCovType = coverage_addlcovtype
        self.COVERAGE_assocCov = coverage_assoccov
        self.COVERAGE_LOSS_claimNumber = coverage_loss_claimnumber
        self.COVERAGE_LOSS_policyNumber = coverage_loss_policynumber
        self.COVERAGE_LOSS_catastrophe = coverage_loss_catastrophe
        self.COVERAGE_LOSS_isCommercial = coverage_loss_iscommercial
        self.COVERAGE_LOSS_policyStart = coverage_loss_policystart
        self.COVERAGE_LOSS_policyEnd = coverage_loss_policyend
        self.COVERAGE_LOSS_dateInitCov = coverage_loss_dateinitcov
        self.COVERAGE_LOSS_isTotalLoss = coverage_loss_istotalloss
        self.COVERAGE_LOSS_dedApplyAcrossAllUI = coverage_loss_dedapplyacrossallui
        self.COVERAGE_LOSS_roofDamage = coverage_loss_roofdamage
        self.COVERAGE_LOSS_roofType = coverage_loss_rooftype
        self.COVERAGE_LOSS_roofAge = coverage_loss_roofage
        self.COVERAGE_LOSS_fullRoofReplacement = coverage_loss_fullroofreplacement
        self.COVERAGE_LOSS_fullSidingReplacement = coverage_loss_fullsidingreplacement
        self.COVERAGE_LOSS_fullFencingReplacement = coverage_loss_fullfencingreplacement
        self.COVERAGE_LOSS_fullHVACComponentReplacement = coverage_loss_fullhvaccomponentreplacement
        self.COVERAGE_LOSS_fullWoodFlooringReplacement = coverage_loss_fullwoodflooringreplacement
        self.COVERAGE_LOSS_waiver = coverage_loss_waiver
        self.COVERAGE_LOSS_paidBillOnly = coverage_loss_paidbillonly
        self.COVERAGE_LOSS_penaltyAfterDeduct = coverage_loss_penaltyafterdeduct
        self.COVERAGE_LOSS_absorbDed = coverage_loss_absorbded
        self.COVERAGE_LOSS_coverageNotes = coverage_loss_coveragenotes
        self.COVERAGES_lossOfUse = coverages_lossofuse
        self.COVERAGES_lossOfUseReserve = coverages_lossofusereserve
        self.COVERAGES_doNotApplyLimits = coverages_donotapplylimits
        self.EMAIL_address = email_address
        self.EST_CHANGE_estChgType = est_change_estchgtype
        self.EST_CHANGE_estChgReason = est_change_estchgreason
        self.EST_CHANGE_onsite = est_change_onsite
        self.EST_CHANGE_printOnsite = est_change_printonsite
        self.EXPENSE_hours = expense_hours
        self.EXPENSE_amount = expense_amount
        self.EXPENSE_code = expense_code
        self.EXPENSE_codeDesc = expense_codedesc
        self.EXPENSE_desc = expense_desc
        self.EXPENSE_miles = expense_miles
        self.EXPENSE_paidByEmp = expense_paidbyemp
        self.EXPENSE_personalCar = expense_personalcar
        self.EXPENSE_noCharge = expense_nocharge
        self.EXPENSE_prorated = expense_prorated
        self.LOSS_DATA_deductApplied = loss_data_deductapplied
        self.LOSS_DATA_overLimits = loss_data_overlimits
        self.MINIMUM_id = minimum_id
        self.MINIMUM_desc = minimum_desc
        self.MINIMUM_amount = minimum_amount
        self.MINIMUM_cat = minimum_cat
        self.MINIMUM_sel = minimum_sel
        self.MINIMUM_doNotApply = minimum_donotapply
        self.MINIMUM_lockedAmount = minimum_lockedamount
        self.PARAMS_priceList = params_pricelist
        self.PARAMS_defaultAct = params_defaultact
        self.PARAMS_taxJurisdiction = params_taxjurisdiction
        self.PARAMS_checkpointPL = params_checkpointpl
        self.PARAMS_plModifiedDateTime = params_plmodifieddatetime
        self.PARAMS_salesTaxModified = params_salestaxmodified
        self.PARAMS_noOPAction = params_noopaction
        self.PARAMS_defaultRepairedBy = params_defaultrepairedby
        self.PARAMS_permitType = params_permittype
        self.PARAMS_laborCostModel = params_laborcostmodel
        self.PARAMS_depRemoval = params_depremoval
        self.PARAMS_depMaterialsOnly = params_depmaterialsonly
        self.PARAMS_depAddOns = params_depaddons
        self.PARAMS_depMat = params_depmat
        self.PARAMS_depNonMat = params_depnonmat
        self.PARAMS_depTaxes = params_deptaxes
        self.PARAMS_maxDepr = params_maxdepr
        self.PARAMS_ignoreItemDeprUnder = params_ignoreitemdeprunder
        self.PARAMS_overhead = params_overhead
        self.PARAMS_profit = params_profit
        self.PARAMS_cumulativeOP = params_cumulativeop
        self.PHONE_extension = phone_extension
        self.PHONE_number = phone_number
        self.PHONE_primary = phone_primary
        self.PHONE_type = phone_type
        self.PROJECT_INFO_assignmentCode = project_info_assignmentcode
        self.PROJECT_INFO_name = project_info_name
        self.PROJECT_INFO_version = project_info_version
        self.PROJECT_INFO_profile = project_info_profile
        self.PROJECT_INFO_xactnetAddress = project_info_xactnetaddress
        self.PROJECT_INFO_created = project_info_created
        self.PROJECT_INFO_userId = project_info_userid
        self.PROJECT_INFO_showDeskAdjuster = project_info_showdeskadjuster
        self.PROJECT_INFO_showIADeskAdjuster = project_info_showiadeskadjuster
        self.PROJECT_INFO_status = project_info_status
        self.SUMMARY_homeOwnerItems = summary_homeowneritems
        self.SUMMARY_contractorItems = summary_contractoritems
        self.SUMMARY_estimateLineItemTotal = summary_estimatelineitemtotal
        self.SUMMARY_minimumChargeAdjustments = summary_minimumchargeadjustments
        self.SUMMARY_overhead = summary_overhead
        self.SUMMARY_profit = summary_profit
        self.SUMMARY_salesTax = summary_salestax
        self.SUMMARY_grossEstimate = summary_grossestimate
        self.SUMMARY_permitsAndFees = summary_permitsandfees
        self.SUMMARY_salvageRetention = summary_salvageretention
        self.SUMMARY_recoverableDepreciation = summary_recoverabledepreciation
        self.SUMMARY_nonRecoverableDepreciation = summary_nonrecoverabledepreciation
        self.SUMMARY_netEstimate = summary_netestimate
        self.SUMMARY_priceListLineItemTotal = summary_pricelistlineitemtotal
        self.SUMMARY_deductible = summary_deductible
        self.TOL_desc = tol_desc
        self.TOL_code = tol_code
        self.XACTNET_INFO_assignmentType = xactnet_info_assignmenttype
        self.XACTNET_INFO_businessUnit = xactnet_info_businessunit
        self.XACTNET_INFO_cancellation = xactnet_info_cancellation
        self.XACTNET_INFO_carrierAttribute1 = xactnet_info_carrierattribute1
        self.XACTNET_INFO_carrierAttribute2 = xactnet_info_carrierattribute2
        self.XACTNET_INFO_carrierAttribute3 = xactnet_info_carrierattribute3
        self.XACTNET_INFO_carrierExternalUniqueId = xactnet_info_carrierexternaluniqueid
        self.XACTNET_INFO_carrierId = xactnet_info_carrierid
        self.XACTNET_INFO_carrierName = xactnet_info_carriername
        self.XACTNET_INFO_carrierNameForXM8 = xactnet_info_carriernameforxm8
        self.XACTNET_INFO_collaboratorsXnAddress = xactnet_info_collaboratorsxnaddress
        self.XACTNET_INFO_collaboratorsXM8UserId = xactnet_info_collaboratorsxm8userid
        self.XACTNET_INFO_collaboratorsName = xactnet_info_collaboratorsname
        self.XACTNET_INFO_createdByReassignment = xactnet_info_createdbyreassignment
        self.XACTNET_INFO_creatorsUserNumber = xactnet_info_creatorsusernumber
        self.XACTNET_INFO_creatorsFirstName = xactnet_info_creatorsfirstname
        self.XACTNET_INFO_creatorsLastName = xactnet_info_creatorslastname
        self.XACTNET_INFO_creatorsEmailAddress = xactnet_info_creatorsemailaddress
        self.XACTNET_INFO_emergency = xactnet_info_emergency
        self.XACTNET_INFO_estimateCount = xactnet_info_estimatecount
        self.XACTNET_INFO_groupId = xactnet_info_groupid
        self.XACTNET_INFO_jobSizeCode = xactnet_info_jobsizecode
        self.XACTNET_INFO_mitigation = xactnet_info_mitigation
        self.XACTNET_INFO_profileCode = xactnet_info_profilecode
        self.XACTNET_INFO_recipientsId = xactnet_info_recipientsid
        self.XACTNET_INFO_recipientsXM8UserId = xactnet_info_recipientsxm8userid
        self.XACTNET_INFO_recipientsUserNumber = xactnet_info_recipientsusernumber
        self.XACTNET_INFO_recipientsXNAddress = xactnet_info_recipientsxnaddress
        self.XACTNET_INFO_referralCarrierId = xactnet_info_referralcarrierid
        self.XACTNET_INFO_referralCarrierName = xactnet_info_referralcarriername
        self.XACTNET_INFO_referralXNAddress = xactnet_info_referralxnaddress
        self.XACTNET_INFO_rotationTrade = xactnet_info_rotationtrade
        self.XACTNET_INFO_senderAttribute1 = xactnet_info_senderattribute1
        self.XACTNET_INFO_senderAttribute2 = xactnet_info_senderattribute2
        self.XACTNET_INFO_senderAttribute3 = xactnet_info_senderattribute3
        self.XACTNET_INFO_senderExternalUniqueId = xactnet_info_senderexternaluniqueid
        self.XACTNET_INFO_senderId = xactnet_info_senderid
        self.XACTNET_INFO_carrierOffice1 = xactnet_info_carrieroffice1
        self.XACTNET_INFO_carrierOffice2 = xactnet_info_carrieroffice2
        self.XACTNET_INFO_carrierOffice3 = xactnet_info_carrieroffice3
        self.XACTNET_INFO_sendersOfficeDescription1 = xactnet_info_sendersofficedescription1
        self.XACTNET_INFO_sendersOfficeDescription2 = xactnet_info_sendersofficedescription2
        self.XACTNET_INFO_sendersOfficeDescription3 = xactnet_info_sendersofficedescription3
        self.XACTNET_INFO_sendersXNAddress = xactnet_info_sendersxnaddress
        self.XACTNET_INFO_sourceTransactionId = xactnet_info_sourcetransactionid
        self.XACTNET_INFO_thirdPartyGeoId = xactnet_info_thirdpartygeoid
        self.XACTNET_INFO_thirdPartyId = xactnet_info_thirdpartyid
        self.XACTNET_INFO_thirdPartyId = xactnet_info_thirdpartyid
        self.XACTNET_INFO_transactionId = xactnet_info_transactionid
        self.XACTNET_INFO_transactionType = xactnet_info_transactiontype
        self.XACTNET_INFO_xaProjectId = xactnet_info_xaprojectid


class Note:
    """ Class for Note Export Data Dictionary"""

    def __init__(self):
        self.NOTES_type = notes_type
        self.NOTES_stamp = notes_stamp
        self.NOTES_userName = notes_username
        self.CONTROL_POINTS_transactionId = control_points_transactionid


def read_xml(xsd_file):
    xsd_file = xsd_file
    status_tree = ET.parse(xsd_file, parser=None)
    print("""
        status tree path: {}
        print status tree: {},
        status tree type: {},"""
          .format(xsd_file, status_tree, type(status_tree)))

    root = status_tree.getroot()
    print("""
        root: {}
        type: {}
        root.tag: {}
        root.attribute: {}
    """.format(root, type(root), root.tag, root.attrib))
    print('iterating through root:')
    for i in root:
        print(i.tag, i.attrib)

    print('#######################################################')
    print('iterating through entire tree:')
    all_elements = [elem.tag for elem in root.iter()]
    for i in all_elements:
        print(type(i))
        print(i)
    print('#######################################################')


def metadata():
    print('#' * 40)
    print("""metadata
            there are {} xml files in the data/status dir

            this project directory: {} 
            this python script's directory: {}
    /metadata"""
          .format(len(files), project_dir, os.getcwd()))
    print('#' * 40)


def printing_class_init():
    print('.')
    # for i in list_of_data_dict:
    #     x = i.element
    #     y = i.attribute
    #     j = x + '_' + y
    #     print(j)

    # for i in list_of_data_dict:
    #     a = 'self.'
    #     x = i.element
    #     y = i.attribute
    #     j = a + x + '_' + y
    #     name = x + '_' + y
    #     name = name.lower()
    #     final = j + '=' + name
    #     print(final)

    # a = '(self, '
    # for i in list_of_data_dict:
    #     name = i.element + '_' + i.attribute
    #     name = name.lower()
    #     a += name
    #     a += ', '
    #     print(a)


def xlxs2csv():
    data_dicts_dir = os.path.join(project_dir, 'data_dicts')
    path, dir, files = next(os.walk(data_dicts_dir))
    for file in files:
        if file.endswith('.xlsx'):
            base_name = os.path.splitext(file)[0] + '.csv'
            if os.path.exists(base_name):
                pass
            else:
                print(base_name)
                p = os.path.join(path, file)
                save_path = os.path.join(data_dicts_dir, base_name)
                read_file = pd.read_excel(p)
                read_file.to_csv(save_path, index=None, header=True)
    print('done')


#######################################################################
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#######################################################################
def csv2json():
    data_dicts_dir = os.path.join(project_dir, 'data_dicts')
    path, dir, files = next(os.walk(data_dicts_dir))
    for file in files:
        if file.endswith('.csv'):
            base_name = os.path.splitext(file)[0] + '.json'
            if os.path.exists(base_name):
                pass
            else:
                json_save_path = os.path.join(data_dicts_dir, base_name)
                with open(os.path.join(path, file)) as f:
                    print('-' * 30)
                    print('| FILE: ', file)
                    csv_reader = csv.reader(f)
                    line_count = 0
                    some_list = []
                    for row in csv_reader:
                        if line_count == 0:
                            print('| COLUMNS:')
                            for column in row:
                                print(' * ', column)
                            line_count += 1
                        else:
                            try:
                                x, y, z, a = row[0], row[1], row[2], row[3]
                                temp = GenericDataDictionaryClass(x, y, z, a)
                                some_list.append(vars(temp))
                            except Exception as ex:
                                x, y, z, a = row[0], row[1], None, row[2]
                                temp = GenericDataDictionaryClass(x, y, z, a)
                                some_list.append(vars(temp))
                            line_count += 1
                    print('| ROW_COUNT: ', line_count)
                    print(' ')
                with open(json_save_path, 'w') as jfile:
                    json.dump(some_list, jfile)


def main():
    # read file
    standard_carrier_data_dic = '/home/rqm/main/dev/ace/bdp-2590/xact-edi/XactAnalysis Export Documentation/Estimate ' \
                                'Export/StandardCarrier data dictionary.xlsx '
    status_data_dict = '/home/rqm/main/dev/ace/bdp-2590/xact-edi/XactAnalysis Export Documentation/Status ' \
                       'Export/StandardStatusExportDataDictionary.xlsx'

    # all example XML files in 'file'
    path, dirs, files = next(os.walk(status_dir))
    path, dirs, files = next(os.walk(data_dict_dir))

    # get every possible data type from the documentation
    # get every row in the csv
    for file in files:
        list_of_data_dict = []
        if file.endswith('.csv'):
            with open(os.path.join(path, file)) as csv_file:
                csv_reader = csv.reader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        try:
                            x, y, z, a = row[0], row[1], row[2], row[3]
                            temp = GenericDataDictionaryClass(x, y, z, a)
                            list_of_data_dict.append(temp)
                        except Exception as ex:
                            x, y, z, a = row[0], row[1], None, row[2]
                            temp = GenericDataDictionaryClass(x, y, z, a)
                            list_of_data_dict.append(temp)
                        line_count += 1
            print('FILE: ')
            print(file)
            for i in list_of_data_dict:
                a = 'self.'
                b = i.element
                c = i.attribute
                bc = b + '_' + c
                alltogether = a + bc + '=' + bc.lower()
                print(alltogether)
            print('- -- -' * 15)
            # for i in list_of_data_dict:
            #     b = i.element
            #     c = i.attribute
            #     bc = b + '_' + c
            #     bcp = bc.lower() + ', '
            #     params = '(self, '
            #     params += bcp
            #     print(params)
            # print('- -- -' * 15)

    # test_file = files[5]
    # z = os.path.join(path, test_file)
    # test_file_tree = ET.parse(z, parser=None)
    # root = test_file_tree.getroot()
    #
    # print('~ ' * 70)
    # print('fuckin around with parsing an example XML:')
    # print("""
    # test file path/name:            {}
    # test file root:                 {}
    # test file, # of child nodes:    {}
    # """
    #       .format(z, root, 'tbd'))
    # for i in list_of_data_dict:
    #     print(i)
    # print('~ ' * 70)
    # for i in root:
    #     print(i)
    #     print(i.tag)
    #     print(i.attrib)
    #     print('_ ' * 20)
    #
    # print('?/???///??/?///////')
    # for child in root.iter():
    #     print('child:')
    #     print(child)
    #     print('child.attribute:')
    #     print(child.attrib)
    #     try:
    #         for i, j in child.attrib.items():
    #             print(' ')
    #             print(i, ' : ', j)
    #     except:
    #         pass
    #     print('child.tag:')
    #     print(child.tag)
    #     print(' ')
    #
    # # for i in root.findall('CONTACT'):
    # #     print('#$!')
    # #     print(i)


if __name__ == '__main__':
    main()
    # csv2json()
    # xlxs2csv()
