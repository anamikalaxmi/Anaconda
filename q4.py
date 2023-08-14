def gs(basic, grade):
	hra=basic*0.2
	da=0.5*basic
	if grade.lower()=="a":
		allow=1700
	elif grade.lower()=="b":
		allow=1500
	elif grade.lower()=="c":
		allow=1300
	pf=0.11*basic
	gross=basic+hra+da+allow-pf
	print("Gross Salary=",gs)

