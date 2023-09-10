def second_power (number):
      try:
        int_number = int(number)
        return int_number ** 2
      except ValueError:
        print(f'{number} is not number')

print(second_power("ahoh"))