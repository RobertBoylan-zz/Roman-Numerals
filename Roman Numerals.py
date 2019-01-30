romanNumbers = [
    ['M',  1000],
    ['CM',  900],
    ['D',   500],
    ['CD',  400],
    ['C',   100],
    ['XC',   90],
    ['L',    50],
    ['XL',   40],
    ['X',    10],
    ['IX',    9],
    ['V',     5],
    ['IV',    4],
    ['I',     1]
]

def convertToNumeral(year):

    if year < 1:
        raise ValueError("Romans did not count below 1")
    if year > 3000:
        raise ValueError("Romans did not count beyond 3000")

    numeral = ""

    for romanNumber, value in romanNumbers:
        while year >= value:
            numeral += romanNumber
            year -= value

            if year < 1:
                break
        if year < 1:
            break

    return numeral

def main(): # define main function
	print(convertToNumeral(2070))

if __name__ == '__main__':
    main() # call main() function

