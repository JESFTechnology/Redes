decimal = 45

binario = ""

if decimal >= 128:
    binario += "1"
    decimal = decimal-128
    print(decimal+128, " - ", 128, " = ", decimal)
else:
    binario += "0"
if decimal >= 64:
    binario += "1"
    decimal = decimal-64
    print(decimal+64, " - ", 64, " = ", decimal)
else:
    binario += "0"
if decimal >= 32:
    binario += "1"
    decimal = decimal-32
    print(decimal+32, " - ", 32, " = ", decimal)
else:
    binario += "0"
if decimal >= 16:
    binario += "1"
    decimal = decimal-16
    print(decimal+16, " - ", 16, " = ", decimal)
else:
    binario += "0"
if decimal >= 8:
    binario += "1"
    decimal = decimal-8
    print(decimal+8, " - ", 8, " = ", decimal)
else:
    binario += "0"
if decimal >= 4:
    binario += "1"
    decimal = decimal-4
    print(decimal+4, " - ", 4, " = ", decimal)
else:
    binario += "0"
if decimal >= 2:
    binario += "1"
    decimal = decimal-2
    print(decimal+2, " - ", 2, " = ", decimal)
else:
    binario += "0"
if decimal >= 1:
    binario += "1"
    decimal = decimal-1
    print(decimal+1, " - ", 1, " = ", decimal)
else:
    binario += "0"


print(binario)

