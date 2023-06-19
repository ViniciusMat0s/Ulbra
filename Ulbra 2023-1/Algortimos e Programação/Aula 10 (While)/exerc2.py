#2. Faça um programa que mostre as tabuadas dos números de 1 a 10.
i = 1
form = 1

while form <= 10 and i <= 10:
    print(f"{i} X {form} = {i * form}")
    form += 1
    if form > 10:
        form = 1
        i += 1
        if i <= 10:
            print(f"==============\nTabuada do {i}\n--------------")