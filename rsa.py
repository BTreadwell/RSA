import primeGenerator
import random

#get primes and calc modulus and totient
###p, q = primeGenerator.get_prime(), primeGenerator.get_prime()
#to save run time while testing, primeGenerator will not be run every time, instead I ran it once and saved those values here.
p = 9275890190115278248558852283151173493790341881582824177509531376024660579276717222960494392692348676416842416457987894143889051236474871973740322296140627563528007708422417024743907237948916034154492961983432268266345280812032368815025048611222699624192834318161283534962018761710186531549273055511707714932862880348745386833318484503124794982620750436858863268641175740610549751879175015414936626508113481631675858904435661662049400044541394955872807302485324331629737015653942268079096769802711524541808884464469596945339968951589474161854687173228748463100160332907495136254814101082466458530728413662231237694911
q = 13620252930688734489101487852028172794954813101773647108012078378727988543494751420022367001676915888314760828700135527826886069938134428412686795471843715194555585187326712904092828903129793093819160974082416271378980792418886497274352638697075898921499899243333610898230156536931919410965936646139721783867887489779048110521229788650056045038196294714100134434229235190683468251788112661432407673328185522795938558983018995188386673339225842509799605945350808876627076517651168748422157425812719887808064788706186495458760543953944870958006439463544108299211498035384193489321830765157979350569297193784010411048007

modulus  = p * q
ttnt = (p-1) * (q-1)
#choose e such that e is coprime with ttnt
e = 1
while modulus % e == 0:
    e = random.choice(primeGenerator.PRIMES_LT_1000)
#calculate d, k can be any integer
k = random.randint(2, 1000)
d = int((1 + k*ttnt) // e)

PRIVATE_KEY = (modulus, d)
PUBLIC_KEY = (modulus, e)

#to encrypt:
###encrypted_data = (msg**e % modulus) OR pow(msg, e, modulus)
#to decrypt:
###decrypted_data = pow(encrypted_data, d, n)

"""
def run(key, msg):

    byte_array = []
    for digit in msg:
        byte_array.append(bin(ord(digit))[2:].zfill(8))
    byte_string = ''.join(byte_array)

    number = int(byte_string, 2)

    new_number = pow(number, key[1], key[0])

    new_num_bin = bin(new_number)[2:]
    new_num_bin_str = str(new_num_bin)
    while len(new_num_bin_str) % 8 != 0:
        new_num_bin_str = '0' + new_num_bin_str

    new_list = []
    for x in range(len(new_num_bin_str)//8):
        new_list.append(int(new_num_bin_str[8*x:8*x+8], 2))
    print(new_list)

    new_list_chars = [chr(x) for x in new_list]
    for x in range(len(new_list_chars)):
        print(new_list[x], '\t', ord(new_list_chars[x]))
    return ''.join(new_list_chars)
new = run(PUBLIC_KEY, 'hello world')
print("###")
x = run(PRIVATE_KEY, new)
"""
#####to encrypt
#get ord() of each digit
#convert to bin
#use [:2] to strip '0b'
#and then .zfill(8) to make length of 8
#add each of these to an array
# ''.join() the array
#convert to int
#then perform calculation
#after calculation
#convert int to pin
#strip[:2] to get rid of '0b'
#pad with leading zeroes till length is divisible by 8
#for every group of 8, convert to int, add to list
#for every int, get the chr() add to another list
# ''.join() list
#this is encrypted text

#####should probably be the same with decryption just with diff keys.
#idk we'll see lol
