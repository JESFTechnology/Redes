
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
        return decimal

    def to_bin(self):
        #Criando conversão convensional
        decimal = self.to_dec()
        binario = ""
        while decimal > 0:
            if decimal % 2 == 0:
                binario = "0" + binario
            else:
                binario = "1" + binario
            decimal = decimal // 2
        return binario
    

teste = Hex("2FA")
print(teste.to_dec())
print(teste.to_bin())