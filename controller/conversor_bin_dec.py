ip = "10101100.00010000.00000001.00000001"
novo_ip = ""
for octeto in ip.split("."):
    decimal = 0
    for i in range(8):
        decimal += int(octeto[i]) * (2 ** (7 - i))
    novo_ip += str(decimal) + "."
print(novo_ip[:-1])
