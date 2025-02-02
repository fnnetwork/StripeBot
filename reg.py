import re

def reg(cc):
    regex = r'\d+'
    matches = re.findall(regex, cc)
    match = ''.join(matches)

    if len(match) < 16:
        return None  # Not a valid CC input

    n = match[:16]
    mm = match[16:18]
    yy = match[18:20]

    if yy == '20':
        yy = match[18:22]
        cvc_start = 22
    else:
        cvc_start = 20

    if n.startswith("3"):
        cvc = match[cvc_start:cvc_start + 4]  # Amex requires 4-digit CVC
    else:
        cvc = match[cvc_start:cvc_start + 3]

    # Validate extracted values
    if not re.match(r'^\d{16}$', n) or not re.match(r'^\d{2}$', mm) or not re.match(r'^\d{2,4}$', yy) or not re.match(r'^\d{3,4}$', cvc):
        return None

    return f"{n}|{mm}|{yy}|{cvc}"
	
