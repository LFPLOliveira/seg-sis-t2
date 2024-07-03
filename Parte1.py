from Crypto.Util import number
import math

# Função de verificação de e_student que é coprimo a L


def choose_large_e(L):
    e_student = pow(2, 32) + 1
    if math.gcd(e_student, L) == 1:
        return e_student
    else:
        raise ValueError(
            "The chosen value for e_student is not coprime with L.")


# Gerar primos p e q
bitsA = 2048
p = number.getPrime(bitsA)
print("p:", p)
print("")
q = number.getPrime(bitsA)
print("q:", q)
print("")

modulus = p * q

# Função de Euler
lambda_n = (p - 1) * (q - 1)

# Escolher e_student
e_student = choose_large_e(lambda_n)
print("e:", e_student)

# Inverso de e_student mod L
d_student = pow(e_student, -1, lambda_n)
print("d:", d_student)

# Chave públca e privada do aluno
public_key_student = (e_student, modulus)
print(public_key_student)
print("")

private_key_student = (d_student, modulus)
print(private_key_student)
print("")


# Gerar um número de exatamente 128 bits


def get_128_bit_integer():
    s = number.getRandomInteger(128)
    while s.bit_length() != 128:
        s = number.getRandomInteger(128)
    return s


# Gerar s
s = get_128_bit_integer()
print(f"s: {s}")
print(f"Number of bits in s: {s.bit_length()}")

# Chave pública do prof.
e_professor = int('2E76A0094D4CEE0AC516CA162973C895', 16)
N_professor = int('1985008F25A025097712D26B5A322982B6EBAFA5826B6EDA3B91F78B7BD63981382581218D33A9983E4E14D4B26113AA2A83BBCCFDE24310AEE3362B6100D06CC1EA429018A0FF3614C077F59DE55AADF449AF01E42ED6545127DC1A97954B89729249C6060BA4BD3A59490839072929C0304B2D7CBBA368AEBC4878A6F0DA3FE58CECDA638A506C723BDCBAB8C355F83C0839BF1457A3B6B89307D672BBF530C93F022E693116FE4A5703A665C6010B5192F6D1FAB64B5795876B2164C86ABD7650AEDAF5B6AFCAC0438437BB3BDF5399D80F8D9963B5414EAFBFA1AA2DD0D24988ACECA8D50047E5A78082295A987369A67D3E54FFB7996CBE2C5EAD794391', 16)

x = pow(s, e_professor, N_professor)

# Assinar x com chave privada do aluno
signature_student = pow(x, d_student, modulus)

print(f"x: {hex(x)}\n")
print(f"signature_student: {hex(signature_student)}\n")
print(
    f"public_key_student: (e_student: {hex(e_student)}, modulus: {hex(modulus)})\n")
