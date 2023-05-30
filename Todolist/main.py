def showMenu(list):
    print(" TO DO LIST APP ")
    print("1. Buat tugas")
    print("2. Lihat tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def addTask(list):
    task = input("Nama tugas: ")
    list.append(task)
    print("Berhasil menambahkan tugas")

def viewTask(list):
    if len(list) == 0:
        print("Tidak ada tugas, silahkan membuat baru")
    else:
        print("List tugas: ")
        for i, tugas in enumerate(list, start=1):
            print(f"{i}. {tugas}")

def deleteTask(list):
    if len(list) == 0:
        print("Pilihan anda tidak tersedia, silahkan coba lagi")
    else:
        viewTask(list)
        taskIndex = int(input("Hapus tugas: "))
        if taskIndex < 1 or taskIndex > len(list):
            print("Tugas terpilih tidak tersedia")
        else:
            deleteIndex = list.pop(taskIndex - 1)
            print(f"Tugas '{taskIndex}' terhapus!")

def main():
    list = []
    while True:
        showMenu(list)
        masuk = input("Pilih menu: [1 - 5] : ")
        if masuk == "1":
            addTask(list)
        elif masuk == "2":
            viewTask(list)
        elif masuk == "3":
            deleteTask(list)
        elif masuk == "4":
            print("Terima kasih sudah menggunakan aplikasi ini!")
            break
        else:
            print("Menu tidak tersedia silahkan coba lagi!")

main()