#coding=UTF-8
# arvutab brutopalgast netopalga
def bruto_to_neto(bruto):
	if bruto <= 144:
		neto = bruto * 0.96
	else:
		tulumaks = (bruto * 0.96 - 144) * 0.21
		neto = bruto * 0.96 - tulumaks
	return neto
isa = 500
ema = 378
sissetulek = bruto_to_neto(isa) + bruto_to_neto(ema)
print sissetulek		
