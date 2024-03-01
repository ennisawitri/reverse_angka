# function untuk mengecek apakah bilangan prima
def bil_prima(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % n == 0:
                return False
        return True 

# function dengan aturan sesuai perintah
def list_angka():
    hasil = []
    for i in range(1, 101):
        if bil_prima(i):
            continue
        elif i % 3 == 0 and i % 5 == 0:
            hasil.append("FooBar")
        elif i % 3 == 0:
            hasil.append("Foo")
        elif i % 5 == 0:
            hasil.append("Bar")
        else:
            hasil.append(i)
    return hasil

# function untuk membuat urutan terbalik dengan format menyamping
def list_terbalik(urutan):
    list_reverse = list(reversed(urutan))
    string_output = ", ".join(map(str, list_reverse))
    print(string_output)


# generate list angka yang diinginkan
generated_list = list_angka()

# print hasil ururtan terbalik
list_terbalik(generated_list)