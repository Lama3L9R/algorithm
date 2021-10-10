import math

def log(base, power, accuracy=3):
    if accuracy > 15:
        return high_acc_log(base, power, accuracy)
    if base % 2 == 0 and power < 0:
        raise RuntimeError('imaginaries are not supported')
        
    result = 0
    exp = 0
    p = power
    for i in range(0, accuracy + 1):
        while p >= base:
            p /= base
            exp += 1
        result += exp * (10 ** -i)
        p **= 10
    return result

def high_acc_log(base, power, accuracy=3):
    if base % 2 == 0 and power < 0:
        raise RuntimeError('imaginaries are not supported')

    result = []
    exp = 0
    p = power
    for i in range(0, accuracy + 1):
        if p <= 1:
            result.append(0)
        else:
            while p >= base:
                p /= base
                exp += 1
            result.append(exp)
            p **= 10
    return result

def main():
    print("log_2(32) lama impl        : " + str(log(2, 32, accuracy=25)))
    print("log_2(32) python math impl : " + str(math.log2(32)))

main()