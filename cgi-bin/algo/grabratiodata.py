import pandas as pd
import math
import pickle
# import numpy as np

def grabratio(stockcode):
	def executefunc(exe_str):
		# return eval(exe_str)
		try:
			return eval(exe_str)
		except:
			return float('nan')

	global year_fac
	incometable = pd.read_html("https://finance.yahoo.com/quote/{}.HK/financials?p={}.HK".format(stockcode,stockcode),header=0)
	bstable = pd.read_html("https://finance.yahoo.com/quote/{}.HK/balance-sheet?p={}.HK".format(stockcode,stockcode),header=0)
	cashflowtable = pd.read_html("https://finance.yahoo.com/quote/{}.HK/cash-flow?p={}.HK".format(stockcode,stockcode),header=0)
	incomestat = incometable[0].set_index(["Revenue"])
	bs = bstable[0].set_index(["Period Ending"])
	cashflow = cashflowtable[0].set_index(["Period Ending"])
	year = [i.split("/")[2] for i in incomestat.columns.values]

	inputdict = {}
	for i in year:
		inputdict.update({i:[]})

	global np
	np = {}
	global totalasset
	totalasset = {}
	global ca
	ca = {}
	global cl
	cl = {}
	global short_term_debt
	short_term_debt = {}
	global cash
	cash = {}
	global short_invest
	short_invest = {}
	global tr
	tr = {}
	global operating_exp
	operating_exp = {}
	global dep
	dep = {}
	global retained
	retained = {}
	global ebit
	ebit = {}
	global equity
	equity = {}
	global totalrev
	totalrev ={}
	global fe
	fe = {}
	global gp
	gp = {}
	global interest
	interest = {}
	global tl
	tl = {}
	global inventory
	inventory = {}
	global op
	op = {}
	global fa
	fa = {}
	global logta
	logta = {}
	global cogs
	cogs = {}
	global stockcapital
	stockcapital = {}
	global receivable
	receivable = {}
	global long_lia
	long_lia = {}
	global ext_items
	ext_items = {}

	for i in range(len(year)):
		tmpnp = [float(ii) for ii in incomestat.ix["Net Income",i].tolist() if (math.isnan(float(ii)))==False][0]
		np.update({year[i]:tmpnp})

		totalasset.update({year[i]:float(bs.ix["Total Assets",i])})
		ca.update({year[i]:float(bs.ix["Total Current Assets",i])})
		cl.update({year[i]:float(bs.ix["Total Current Liabilities",i])})
		short_term_debt.update({year[i]:float(bs.ix["Short/Current Long Term Debt",i])})
		cash.update({year[i]:float(bs.ix["Cash And Cash Equivalents",i])})
		short_invest.update({year[i]:float(bs.ix["Short Term Investments",i])})
		tr.update({year[i]:float(bs.ix["Net Receivables",i])})
		operating_exp.update({year[i]:float(incomestat.ix["Total Operating Expenses",i])})
		dep.update({year[i]:float(cashflow.ix["Depreciation",i])})
		retained.update({year[i]:float(bs.ix["Retained Earnings",i])})

		tmpebit = incomestat.ix["Earnings Before Interest and Taxes",i]
		if tmpebit == '-': tmpebit = incomestat.ix["Income Before Tax",i]
		ebit.update({year[i]:float(tmpebit)})

		equity.update({year[i]:float(bs.ix["Total Stockholder Equity",i])})
		totalrev.update({year[i]:float(incomestat.ix["Total Revenue",i])})

		tmp_interest = incomestat.ix["Interest Expense",i]
		if tmp_interest == '-': tmp_interest = 0
		tmp_inctax = incomestat.ix["Income Tax Expense",i]
		if tmp_inctax  == '-': tmp_interest = 0
		fe.update({year[i]:float(tmp_interest)+float(tmp_inctax)})

		gp.update({year[i]:float(incomestat.ix["Gross Profit",i])})
		interest.update({year[i]:float(tmp_interest)})
		tl.update({year[i]:float(bs.ix["Total Liabilities",i])})
		inventory.update({year[i]:float(bs.ix["Inventory",i])})
		op.update({year[i]:float(incomestat.ix["Operating Income or Loss",i])})

		tmp_lti = bs.ix["Long Term Investments",i]
		if tmp_lti == '-': tmp_lti = 0
		tmp_ppe = bs.ix["Property Plant and Equipment",i]
		if tmp_ppe == '-': tmp_ppe = 0
		tmp_oa = bs.ix["Other Assets",i]
		if tmp_oa == '-': tmp_oa = 0
		fa.update({year[i]:float(tmp_lti)+float(tmp_ppe)+float(tmp_oa)})

		tmp_cogs = incomestat.ix["Cost of Revenue",i]
		if tmp_cogs == '-': tmp_cogs = 0
		cogs.update({year[i]:float(tmp_cogs)})

		tmp_pstock = bs.ix["Preferred Stock",i]
		if tmp_pstock == '-': tmp_pstock = 0
		tmp_cstock = bs.ix["Common Stock",i]
		if tmp_cstock == '-': tmp_cstock = 0
		stockcapital.update({year[i]:float(tmp_cstock) + float(tmp_pstock)})

		long_lia.update({year[i]:float(bs.ix["Long Term Debt",i])})

		tmp_ext = incomestat.ix["Extraordinary Items",i]
		if tmp_ext == "-": tmp_ext = 0
		ext_items.update({year[i]:float(tmp_ext)})


	for i in year:
		year_fac = i
		# X1
		inputdict[i].append(executefunc("np[year_fac]/totalasset[year_fac]"))
		# X2
		inputdict[i].append(executefunc("tl[year_fac]/totalasset[year_fac]"))
		# X3
		inputdict[i].append(executefunc("(ca[year_fac]-cl[year_fac])/totalasset[year_fac]"))
		# X4
		inputdict[i].append(executefunc("ca[year_fac]/short_term_debt[year_fac]"))
		# X5
		inputdict[i].append(executefunc("((cash[year_fac]+short_invest[year_fac]+tr[year_fac]-short_term_debt[year_fac])/(operating_exp[year_fac]-dep[year_fac]))*365"))
		# X6
		inputdict[i].append(executefunc("retained[year_fac]/totalasset[year_fac]"))
		# X7
		inputdict[i].append(executefunc("ebit[year_fac]/totalasset[year_fac]"))
		# X8
		inputdict[i].append(executefunc("(totalasset[year_fac]-tl[year_fac])/tl[year_fac]"))
		# X9
		inputdict[i].append(executefunc("totalrev[year_fac]/totalasset[year_fac]"))
		# X10
		inputdict[i].append(executefunc("equity[year_fac]/totalasset[year_fac]"))
		# X11
		inputdict[i].append(executefunc("(gp[year_fac]+ext_items[year_fac]+fe[year_fac])/totalasset[year_fac]"))
		# X12
		inputdict[i].append(executefunc("gp[year_fac]/short_term_debt[year_fac]"))
		# X13
		inputdict[i].append(executefunc("(gp[year_fac]+dep[year_fac])/totalrev[year_fac]"))
		# X14
		inputdict[i].append(executefunc("(gp[year_fac]+interest[year_fac])/totalasset[year_fac]"))
		# X15
		inputdict[i].append(executefunc("(tl[year_fac] * 365)/(gp[year_fac] + dep[year_fac])"))
		# X16
		inputdict[i].append(executefunc("(gp[year_fac] + dep[year_fac])/tl[year_fac]"))
		# X17
		inputdict[i].append(executefunc("totalasset[year_fac]/tl[year_fac]"))
		# X18
		inputdict[i].append(executefunc("gp[year_fac]/totalasset[year_fac]"))
		# X19
		inputdict[i].append(executefunc("gp[year_fac]/totalrev[year_fac]"))
		# X20
		inputdict[i].append(executefunc("(inventory[year_fac] * 365)/totalrev[year_fac]"))
		# X21
		inputdict[i].append(executefunc("totalrev[year_fac]/totalrev[str(int(year_fac)-1)]"))
		# X22
		inputdict[i].append(executefunc("op[year_fac]/totalasset[year_fac]"))
		# X23
		inputdict[i].append(executefunc("np[year_fac]/totalrev[year_fac]"))
		# X24
		inputdict[i].append(executefunc("(gp[str(int(year_fac)-1)]+gp[str(int(year_fac)-2)]+gp[str(int(year_fac)-3)])/totalasset[year_fac]"))
		# X25
		inputdict[i].append(executefunc("(equity[year_fac]-stockcapital[year_fac])/totalasset[year_fac]"))
		# X26
		inputdict[i].append(executefunc("(np[year_fac]+dep[year_fac])/tl[year_fac]"))
		# X27
		inputdict[i].append(executefunc("op[year_fac]/fe[year_fac]"))
		# X28
		inputdict[i].append(executefunc("(ca[year_fac]-cl[year_fac])/fa[year_fac]"))
		# X29
		inputdict[i].append(executefunc("math.log(totalasset[year_fac])"))
		# X30
		inputdict[i].append(executefunc("(tl[year_fac]-cash[year_fac])/totalrev[year_fac]"))
		# X31
		inputdict[i].append(executefunc("(gp[year_fac] + interest[year_fac])/totalrev[year_fac]"))
		# X32
		inputdict[i].append(executefunc("(cl[year_fac] * 365)/cogs[year_fac]"))
		# X33
		inputdict[i].append(executefunc("operating_exp[year_fac]/short_term_debt[year_fac]"))
		# X34
		inputdict[i].append(executefunc("operating_exp[year_fac]/tl[year_fac]"))
		# X35
		inputdict[i].append(executefunc("gp[year_fac]/totalasset[year_fac]"))
		# X36
		inputdict[i].append(executefunc("totalrev[year_fac]/totalasset[year_fac]"))
		# X37
		inputdict[i].append(executefunc("(ca[year_fac]-inventory[year_fac])/long_lia[year_fac]"))
		# X38
		inputdict[i].append(executefunc("stockcapital[year_fac])/totalasset[year_fac]"))
		# X39
		inputdict[i].append(executefunc("gp[year_fac])/totalrev[year_fac]"))
		# X40
		inputdict[i].append(executefunc("(ca[year_fac]-inventory[year_fac]-tr[year_fac])/short_term_debt[year_fac]"))
		# X41
		inputdict[i].append(executefunc("tl[year_fac])/((op[year_fac]+dep[year_fac])*(12/365))"))
		# X42
		inputdict[i].append(executefunc("op[year_fac]/totalrev[year_fac]"))
		# X43
		inputdict[i].append(executefunc("(totalrev[year_fac]/((tr[str(int(year_fac)-1)] + tr[year_fac])/2)) + (365/(cogs[year_fac]/((tr[str(int(year_fac)-1)] + tr[year_fac])/2)))"))
		# X44
		inputdict[i].append(executefunc("(tr[year_fac]*365)/totalrev[year_fac]"))
		# X45
		inputdict[i].append(executefunc("np[year_fac]/inventory[year_fac]"))
		# X46
		inputdict[i].append(executefunc("(ca[year_fac]-inventory[year_fac])/short_term_debt[year_fac]"))
		# X47
		inputdict[i].append(executefunc("(inventory[year_fac]*365)/cogs[year_fac]"))
		# X48
		inputdict[i].append(executefunc("(op[year_fac]-dep[year_fac])/totalasset[year_fac]"))
		# X49
		inputdict[i].append(executefunc("(op[year_fac]-dep[year_fac])/totalrev[year_fac]"))
		# X50
		inputdict[i].append(executefunc("ca[year_fac]/tl[year_fac]"))
		# X51
		inputdict[i].append(executefunc("short_term_debt[year_fac]/totalasset[year_fac]"))
		# X52
		inputdict[i].append(executefunc("(short_term_debt[year_fac]*365)/cogs[year_fac]"))
		# X53
		inputdict[i].append(executefunc("equity[year_fac])/fa[year_fac]"))
		# X54
		inputdict[i].append(executefunc("stockcapital[year_fac])/fa[year_fac]"))
		# X55
		inputdict[i].append(executefunc("ca[year_fac]-cl[year_fac]"))
		# X56
		inputdict[i].append(executefunc("(totalrev[year_fac]-cogs[year_fac])/totalrev[year_fac]"))
		# X57
		inputdict[i].append(executefunc("(ca[year_fac]-inventory[year_fac]-short_term_debt[year_fac])/(totalrev[year_fac]-gp[year_fac]-dep[year_fac])"))
		# X58
		inputdict[i].append(executefunc("(totalrev[year_fac]-np[year_fac])/totalrev[year_fac]"))
		# X59
		inputdict[i].append(executefunc("long_lia[year_fac]/equity[year_fac]"))
		# X60
		inputdict[i].append(executefunc("totalrev[year_fac]/inventory[year_fac]"))
		# X61
		inputdict[i].append(executefunc("totalrev[year_fac]/tr[year_fac]"))
		# X62
		inputdict[i].append(executefunc("(short_term_debt[year_fac]*365)/totalrev[year_fac]"))
		# X63
		inputdict[i].append(executefunc("totalrev[year_fac]/short_term_debt[year_fac]"))
		# X64
		inputdict[i].append(executefunc("totalrev[year_fac]/fa[year_fac]"))

	return inputdict
