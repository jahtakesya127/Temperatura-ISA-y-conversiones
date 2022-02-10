import argparse, sys
from colorama import Fore

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--temperature', default=1, type=int, required=False)
parser.add_argument('-a', '--altitude', default=1, type=int, required=False)
parser.add_argument('--hpa', default=0, type=float, required=False)
parser.add_argument('--inhg', default=0, type=float, required=False)
parser.add_argument('--ms', default=0, type=float, required=False)
parser.add_argument('--km', default=0, type=float, required=False)
parser.add_argument('--ft', default=0, type=float, required=False)
parser.add_argument('--nm', default=0, type=float, required=False)
parser.add_argument('-o', '--output', default=0, type=str, required=False)

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

temp = args.temperature
alt = args.altitude
inHg = args.inhg
hPa = args.hpa
ms = args.ms
km = args.km
ft = args.ft
nm = args.nm
output = args.output

def inHg_hPa():

	hPa = 33.8638
	res = inHg * hPa
	print(inHg, "inHg SON", round(res, 2), "hPa")

def hPa_inHg():
	inHg = 0.02953
	res = hPa * inHg
	print(hPa, "hPa SON", round(res, 2),  "inHg")


def ft_ms():
	ms = 0.3048
	res = ft * ms
	print(ft, "FT SON", round(res, 2), "MS")

def ms_ft():
	ft = 3.28084
	res = ms * ft
	print(ms, "MS SON", round(res, 2), "FT")

def nm_km():
	km = 1.85
	res = nm * km
	print(nm, "NM SON", round(res, 2),  "KMS")

def km_nm():
	nm = 0.54
	res = nm * km
	print(km, "KMS SON", round(res, 2),  "NM")

def troposfera_isa():
	global msl_temp
	msl_temp = 15
	lst = [alt / 1000]
	for i in lst:
		msl_temp -= 1.98 * i
	isa_actual()

def tropopausa():
	global msl_temp
	msl_temp = -56.5
	isa_actual()

def isa_actual():
	temp_isa = temp - msl_temp
	print (f'{Fore.MAGENTA} [*] ISA ESTÁNDAR A', alt, "PIES: "  ,round(msl_temp, 2))
	print (f'{Fore.MAGENTA} [*] ISA ACTUAL: ', round(temp_isa, 2)) if temp_isa < 0 else print(' [*] ISA ACTUAL: +', round(temp_isa, 2))


if output == "hpa":
	inHg_hPa()
elif output == "inhg":
	hPa_inHg()
	pass
elif output == "ms":
	ft_ms()
elif output == "ft":
	ms_ft()
elif output == "nm":
	km_nm()
elif output == "km":
	nm_km()
else:
	if temp and alt == "zzz":
		print("Indiqueee temperatura y altitud")
		print(temp, alt)
	elif alt <= 36089:
		troposfera_isa()
	elif alt > 36089 and alt > 65617:
		tropopausa()

