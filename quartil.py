
def find_Quartil(data: list):

    data.sort()

    for i in range(1, 4):

        quartil = i
        n = len(data)
        # data length is even
        if n % 2 == 0:

            # find quartil 2 with data length can divided by 4 or data length can't divided by 4
            if (n % 4 == 0 or n % 4 != 0) and quartil == 2:

                formula = (n / 2) + (n / 2) + 1
                x = formula / 2
                result = (data[int(x)] + data[int(x)-1]) / 2

                print(f"Quartil - {quartil} : {result}")

            # find quartil 1 3 with data length can divided by 4
            elif n % 4 == 0:

                formula = (quartil * n) / 4 + (quartil * n) / 4 + 1
                x = formula / 2
                result = (data[int(x)] + data[int(x)-1]) / 2

                print(f"Quartil - {quartil} : {result}")

            # find quartil 1 3 with data length can't divided by 4
            elif n % 4 != 0:

                formula = (quartil * n) + 2
                x = formula / 4
                result = data[int(x)-1]

                print(f"Quartil - {quartil} : {result}")

        # data length is odd
        elif n % 2 != 0:

            # find quatril 2 with data length + 1 can divided by 4 or can't divided by 4
            if ((n + 1) % 4 == 0 or (n + 1) % 4 != 0) and quartil == 2:

                formula = quartil * (n + 1)
                x = formula / 4
                result = data[int(x)-1]

                print(f"Quartil - {quartil} : {result}")

            # find quartil 1 3 with data length + 1 can divided by 4
            elif (n + 1) % 4 == 0:

                formula = quartil * (n + 1)
                x = formula / 4
                result = data[int(x)-1]

                print(f"Quartil - {quartil} : {result}")

            # find quartil 1 3 with data length + 1 can't divided by 4
            elif (n + 1) % 4 != 0:

                if quartil == 1:

                    formula = (quartil * n - 1) / 4 + (quartil * n + 3) / 4
                    x = formula / 2
                    result = (data[int(x)] + data[int(x)-1]) / 2

                    print(f"Quartil - {quartil} : {result}")

                else:

                    formula = (quartil * n + 1) / 4 + (quartil * n + 5) / 4
                    x = formula / 2
                    result = (data[int(x)] + data[int(x)-1]) / 2

                    print(f"Quartil - {quartil} : {result}")
