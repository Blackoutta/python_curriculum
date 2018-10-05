def sillycase(string):
    half = len(string)//2
    first_half_lower = string[0:half].lower()
    second_half_upper = string[half:].upper()
    final_number = first_half_lower + second_half_upper
    print(final_number)

sillycase("treehouse")
sillycase("huyangyi")
sillycase("helloworld")
sillycase("o.o")
