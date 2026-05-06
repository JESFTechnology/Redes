
class Hex():
    def __init__(self, value):
        self.value = value

    def to_dec(self):
        #Criando conversão convensional
        decimal = 0
        for i in range(len(self.value)):
            if self.value[i] == "0":
                decimal += 0 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i] == "1":
                decimal += 1 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i] == "2":
                decimal += 2 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i] == "3":
                decimal += 3 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i] == "4":
                decimal += 4 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i] == "5":
                decimal += 5 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i] == "6":
                decimal += 6 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i] == "7":
                decimal += 7 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i] == "8":
                decimal += 8 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i] == "9":
                decimal += 9 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i].upper() == "A":
                decimal += 10 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i].upper() == "B":
                decimal += 11 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i].upper() == "C":
                decimal += 12 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i].upper() == "D":
                decimal += 13 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i].upper() == "E":
                decimal += 14 * (16 ** (len(self.value) - 1 - i))
            elif self.value[i].upper() == "F":
                decimal += 15 * (16 ** (len(self.value) - 1 - i))
            else:
                return True, 0
        return False, decimal

    def to_bin(self):
        #Criando conversão convensional
        error, decimal = self.to_dec()
        binario = ""
        while decimal > 0:
            if decimal % 2 == 0:
                binario = "0" + binario
            else:
                binario = "1" + binario
            decimal = decimal // 2

        #Inverter texto do binário
        #binario = binario[::-1]

        return error, binario
    

class Bin():
    def __init__(self, value):
        self.value = value

    def to_dec(self):
        decimal = 0
        error = False
        for i in range(len(self.value)):
            if self.value[i] == "0":
                decimal += 0 * (2 ** (len(self.value) - 1 - i))
            elif self.value[i] == "1":
                decimal += 1 * (2 ** (len(self.value) - 1 - i))
            else:
                error = True
        return error, decimal

    def to_hex(self):
        #Criando conversão convensional
        error, decimal = self.to_dec()
        hexadecimal = ""
        while decimal > 0:
            if decimal % 16 == 0:
                hexadecimal = "0" + hexadecimal
            elif decimal % 16 == 1:
                hexadecimal = "1" + hexadecimal
            elif decimal % 16 == 2:
                hexadecimal = "2" + hexadecimal
            elif decimal % 16 == 3:
                hexadecimal = "3" + hexadecimal
            elif decimal % 16 == 4:
                hexadecimal = "4" + hexadecimal
            elif decimal % 16 == 5:
                hexadecimal = "5" + hexadecimal
            elif decimal % 16 == 6:
                hexadecimal = "6" + hexadecimal
            elif decimal % 16 == 7:
                hexadecimal = "7" + hexadecimal
            elif decimal % 16 == 8:
                hexadecimal = "8" + hexadecimal
            elif decimal % 16 == 9:
                hexadecimal = "9" + hexadecimal
            elif decimal % 16 == 10:
                hexadecimal = "A" + hexadecimal
            elif decimal % 16 == 11:
                hexadecimal = "B" + hexadecimal
            elif decimal % 16 == 12:
                hexadecimal = "C" + hexadecimal
            elif decimal % 16 == 13:
                hexadecimal = "D" + hexadecimal
            elif decimal % 16 == 14:
                hexadecimal = "E" + hexadecimal
            elif decimal % 16 == 15:
                hexadecimal = "F" + hexadecimal
            decimal = decimal // 16

        #Inverter texto do binário
        #hexadecimal = hexadecimal[::-1]

        return error, hexadecimal

class Dec():
    def __init__(self, value):
        self.value = value

    def to_bin(self):
        decimal = self.value
        binario = ""
        while decimal > 0:
            if decimal % 2 == 0:
                binario = "0" + binario
            else:
                binario = "1" + binario
            decimal = decimal // 2

        #Inverter texto do binário
        #binario = binario[::-1]

        return False, binario
    
    def to_hex(self):
        decimal = self.value
        hexadecimal = ""
        while decimal > 0:
            if decimal % 16 == 0:
                hexadecimal = "0" + hexadecimal
            elif decimal % 16 == 1:
                hexadecimal = "1" + hexadecimal
            elif decimal % 16 == 2:
                hexadecimal = "2" + hexadecimal
            elif decimal % 16 == 3:
                hexadecimal = "3" + hexadecimal
            elif decimal % 16 == 4:
                hexadecimal = "4" + hexadecimal
            elif decimal % 16 == 5:
                hexadecimal = "5" + hexadecimal
            elif decimal % 16 == 6:
                hexadecimal = "6" + hexadecimal
            elif decimal % 16 == 7:
                hexadecimal = "7" + hexadecimal
            elif decimal % 16 == 8:
                hexadecimal = "8" + hexadecimal
            elif decimal % 16 == 9:
                hexadecimal = "9" + hexadecimal
            elif decimal % 16 == 10:
                hexadecimal = "A" + hexadecimal
            elif decimal % 16 == 11:
                hexadecimal = "B" + hexadecimal
            elif decimal % 16 == 12:
                hexadecimal = "C" + hexadecimal
            elif decimal % 16 == 13:
                hexadecimal = "D" + hexadecimal
            elif decimal % 16 == 14:
                hexadecimal = "E" + hexadecimal
            elif decimal % 16 == 15:
                hexadecimal = "F" + hexadecimal
            else:
                return True, hexadecimal
            decimal = decimal // 16

        #Inverter texto do binário
        #hexadecimal = hexadecimal[::-1]

        return False, hexadecimal