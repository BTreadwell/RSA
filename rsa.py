import primeGenerator
import random

#get primes and calc modulus and totient
p, q = primeGenerator.get_prime(), primeGenerator.get_prime()
modulus  = p * q
ttnt = (p-1) * (q-1)

"""
primeGenerator does not generate true primes every run, the following values will work until primeGenerator is fixed
p = 6244831837086619900858276525331291964968265023700168813423023006366333686760339862892892921445930638131265594230413285079044496271789556081325775620151013401085684607923426103476106812516476443381943192720078167552331486705993800493656625650056341032866918310909279989332478663335351975140466216905639090367518419032646277641353202986917265365172684807650488053174773216537951400583222414803854897971822920487530174921227905215735631156197008810614644068908214048739930984857908484567238043428837928700488680702692921607610066825282304733300369460249981416979671587498846537166875618974656937775657948633050246623447

q = 1154456500319363498408280334282426581809694404276431621574064690127574772806282398702709482169698663648562202296106578328237154303111925646677169141786081934601430930669996910418989345368690376716242363199352356040158103600672744487543854058088434982168719374227707412937746126272117024607850856465492790305649416809266756299698879499531391120070453496255931016581126476426125333173116450938472451820328002503848152326911041020284438139141056506253016826178159742335046507571547628498237914298326159179544088755799904739431759452465287051725051523483394051460752606938801219778739510664348008399032710054345071944923
"""

#choose e such that e is coprime with ttnt
e = 1
while ttnt % e == 0:
    e = random.choice(primeGenerator.PRIMES_LT_1000)

#calculate d
d = pow(e, -1, ttnt)

#save private/public key
PRIVATE_KEY = (modulus, d)
PUBLIC_KEY = (modulus, e)

def run(key, msg):

    #convert to array of bytes, then join that array into a string
    byte_array = []
    for digit in msg:
        byte_array.append(bin(ord(digit))[2:].zfill(8))
    byte_string = ''.join(byte_array)

    #convert byte string into a base 2 number
    number = int(byte_string, 2)

    #perform encryption/decryption on number using supplied key
    new_number = pow(number, key[1], key[0])

    #strip the leading '0b'
    new_num_bin = bin(new_number)[2:]
    #convert to string
    new_num_bin_str = str(new_num_bin)
    #pad with leading zeroes
    while len(new_num_bin_str) % 8 != 0:
        new_num_bin_str = '0' + new_num_bin_str

    #separate string into individual bytes
    new_list = []
    for x in range(len(new_num_bin_str)//8):
        new_list.append(int(new_num_bin_str[8*x:8*x+8], 2))

    #convert numeric values to characters in a list
    new_list_chars = [chr(x) for x in new_list]
    #return message
    return ''.join(new_list_chars)
"""
Test
#encrypt apple
new = run(PUBLIC_KEY, 'Apple')
#decrypt message
x = run(PRIVATE_KEY, new)
#should print 'Apple'
print(x)
"""
