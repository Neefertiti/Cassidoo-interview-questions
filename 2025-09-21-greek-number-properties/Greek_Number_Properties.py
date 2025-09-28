import argparse
def getProperDivisors(num, debug):
    factors = []
    for i in range(1, num + 1):
        if num !=i and num % i == 0:
            factors.append(i)
    if debug:
        print (f"Proper Factors of {num} are {factors} ")
    return factors

def getProperDivsorsSum(num, debug):
    factors = getProperDivisors(num, debug)
    sum = 0
    for factor in factors:
        sum += factor
    if debug:
        print (f"The sum of the Proper Factors of {num} is {sum}")
    return sum

def determineGreekNumberProperty(num, debug):
    amicable = False
    proper_sum = getProperDivsorsSum(num, debug)
    if num == proper_sum:
        greek_property = "perfect"
    else:
        possible_amicable_sum = getProperDivsorsSum(proper_sum, debug)
        if possible_amicable_sum == num:
            amicable = True
        if proper_sum < num:
            greek_property = "deficient"
        else:
            greek_property = "abundant"

    print (greek_property)
    if amicable:
        print (f"Amicable with {proper_sum}")


def testGreekNumberProperty(debug=True):
    abun_num_to_test = [12, 18, 20, 24, 30]
    def_num_to_test = [4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23]
    per_num_to_test = [6, 28, 496, 8128]
    ami_num_to_test = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]

    print ("Testing for Abundanct")
    for num in abun_num_to_test:
        determineGreekNumberProperty(num, debug)

    print("Testing for Deficient")
    for num in def_num_to_test:
        determineGreekNumberProperty(num, debug)

    print("Testing for Perfect")
    for num in per_num_to_test:
        determineGreekNumberProperty(num, debug)

    print("Testing for Amicable")
    for num in ami_num_to_test:
        determineGreekNumberProperty(num, debug)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_to_test", help="The number to test", default=1)
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--debug", action="store_true", default=False)
    args = parser.parse_args()

    if args.test:
        testGreekNumberProperty(debug=True)
    else:
        determineGreekNumberProperty(int(args.num_to_test), args.debug)
