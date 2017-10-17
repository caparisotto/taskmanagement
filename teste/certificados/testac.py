#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector as mariadb

from datetime import datetime,timedelta,tzinfo
from django.utils import timezone
import pytz

import smtplib
import sys
import commands
from email.MIMEText import MIMEText

def enviamail(origem,senha,destino,servidor,porta,tipo,cliente,aplicacao,data):
	try :
		serv=smtplib.SMTP()
   		serv.connect(servidor,porta)
   		serv.starttls()
   		serv.login(origem,senha)
		datahoje = datetime.now().strftime("%a, %d %b %Y %X ")
		if tipo == 1:
			texto = "Essa é uma mensagem de testes vinda do futuro...não, brincadeira....vinda da aplicação de certificados."
   			msg1 = MIMEText("%s"% texto)
   			msg1['Subject']='Just Testing'
		else:
			texto = "Certificado do cliente %s,  para a aplicacao %s, expira em %s" %(cliente,aplicacao,str(data))
   			msg1 = MIMEText("%s"% texto)
   			msg1['Subject']='Certificado Expirando'
   		msg1['From']=origem
   		msg1['To']=destino
   		msg1['Date']=datahoje
   		serv.sendmail(origem,destino, msg1.as_string())
   		serv.quit()
	except Exception, e:
   		return 1,e
	else:
   		return 0,None

conn = mariadb.connect(user='mbmonitor', password='7f13SNbp83xnC41', database='mbmonitor')
cur = conn.cursor()
cur.execute("""SELECT nome,aplicacao,validade from certificados_certificados""")
rows = cur.fetchall()  

datahoje = datetime.now(timezone.utc)

for elemento in rows:
	name = elemento[0]
	app = elemento[1]
	date = elemento[2]
	oneweekfromhere = datahoje + timedelta(days=7) 

	datateste =  oneweekfromhere.strftime("%y %m %d %H ")
	datacertificado =  date.strftime("%y %m %d %H")

	if datateste > datacertificado:
		cur.execute("""select mailorigem,senha,smtpserver,smtpport,maildestino from certificados_email_alertas;""")
		rows = cur.fetchall()
		mo = rows[0][0]
		ps = rows[0][1]
		ss = rows[0][2]
		sp = rows[0][3]
		md = rows[0][4]
		ret, e = enviamail(mo,ps,md,ss,sp,2,name,app,date)
		if ret == 0:
			print 'mail ok'
		else:
			print 'rr %s' %(e)
	else:
		print 'stats ok'

