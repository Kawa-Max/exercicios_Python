
def leiaDinheiro(msg):
    ok = False
    while not ok:
        valor = str(input(msg)).replace('.', ',').strip()
        if valor.isnumeric():
            ok = True
            return float(valor)
        else:
            print(f"\033[31mEEEERRROO \033[96mburro, '\033[34m{valor}\033[96m' não é um valor númerico")
