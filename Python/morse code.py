import arabic_reshaper
from bidi.algorithm import get_display
morse_code = {

'._': 'ا','_...': 'ب',
'_': 'ت','_._.': 'ث','.___': 'ج',
'....': 'ح','___': 'خ','_..': 'د',
'__..': 'ذ','._.': 'ر','___.': 'ز',
'...': 'س','____': 'ش','_.._': 'ص',
'..._': 'ض','.._': 'ط','__._': 'ظ',
'._._': 'ع','__.': 'غ','.._.': 'ف',
'_.__': 'ق','_._': 'ك','._..': 'ل',
'__': 'م','_.': 'ن','.._..': 'ه',
'.__': 'و','..': 'ي','.': 'ء'

}

inpt_code = input('Enter the morse code: ')
split_code = inpt_code.split(' ')
print('>>>',end='')

decoded_chars = []

for i in split_code:
    if i == '/':
        decoded_chars.append(' ') # Add a space for words
    elif i in morse_code:
        decoded_chars.append(morse_code[i])

# 1. Join the list into a single string
full_text = "".join(decoded_chars)

# 2. Reshape the letters so they connect properly
reshaped_text = arabic_reshaper.reshape(full_text)

# 3. Fix the direction (Right-to-Left) for the terminal
final_output = get_display(reshaped_text)

print(final_output)