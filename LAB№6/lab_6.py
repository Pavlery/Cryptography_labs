def fast_power_mod (base, exp, mod):
    current_base = base
    current_power = base
    step = 1
    count = 0
    count_mod = 0
    result = 1
    result_pow = pow(base, exp, mod)
    print(f"Вычислить {base}^{exp} mod{mod}")

    while exp > 0:
        print(f"{current_base}^{step}  \t{current_power}\t", end="")
        current_power %= mod
        print(f"{current_power}\t", end="")

        if exp & 1:
            print("1\t", end="")
            count_mod += 1
            result = result * current_power

            if count == 0:
                print(" \t", end="")
            else:
                print(f"{result}\t", end="")
            result %= mod
            print(f"{result}", end="")
        else:
            print("0\t-\t-", end="")

        print("")
        current_power *= current_power
        exp >>= 1
        step *= 2
        count += 1

    print()
    print(f"Результат вычислений = {result}")
    print(f"Результат вычислений через pow = {result_pow}")
    print(f"Кол-во операций = {count_mod}")

if __name__ == "__main__":
    base = 8
    exponent = 10
    mod = 11
    fast_power_mod(base, exponent, mod)
