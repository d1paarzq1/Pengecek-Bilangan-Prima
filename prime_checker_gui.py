import tkinter as tk
from tkinter import ttk, messagebox

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime():
    try:
        number = int(entry.get())
        is_prime_number = is_prime(number)
        result = "Prima" if is_prime_number else "Bukan Prima"

        # Menambahkan hasil ke dalam tabel
        tree.insert('', 'end', values=(number, result))

        # Menghapus input setelah pengecekan
        entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Masukkan bilangan yang valid.")

# Membuat jendela utama
window = tk.Tk()
window.title("Prime Number Checker")
window.geometry("500x400")
window.configure(bg="#2c3e50")  # Mengatur warna latar belakang

# Custom style untuk Treeview
style = ttk.Style()
style.configure("mystyle.Treeview", 
                font=('Times New Roman', 12),  # Mengatur font utama
                rowheight=25,        # Tinggi baris
                background="#ecf0f1",# Warna latar belakang baris
                foreground="#2c3e50")# Warna teks
style.configure("mystyle.Treeview.Heading", 
                font=('Times New Roman, Black', 13, 'bold'), # Font heading
                background="#34495e",            # Warna latar belakang heading
                foreground="white")              # Warna teks heading

# Membuat frame untuk input
frame = ttk.Frame(window, padding="10", style="mystyle.TFrame")
frame.pack(pady=5)

# Label dan Entry untuk input bilangan
label = ttk.Label(frame, text="Masukkan sebuah bilangan:", font=('Times New Roman', 12, 'bold'), background="#2c3e50", foreground="white")
label.grid(row=0, column=0, pady=5)

entry = ttk.Entry(frame, font=('Times New Roman', 12))
entry.grid(row=0, column=1, pady=5)

# Tombol untuk mengecek bilangan prima
check_button = ttk.Button(frame, text="Cek Bilangan", command=check_prime, style="TButton")
check_button.grid(row=0, column=2, padx=5, pady=5)  # Baris ini telah diperbaiki

# Membuat tabel menggunakan Treeview dengan style custom
tree = ttk.Treeview(window, columns=("Bilangan", "Hasil"), show="headings", height=8, style="mystyle.Treeview")
tree.heading("Bilangan", text="Bilangan")
tree.heading("Hasil", text="Hasil")
tree.column("Bilangan", width=200, anchor=tk.CENTER)
tree.column("Hasil", width=200, anchor=tk.CENTER)
tree.pack(pady=20)

# Menjalankan aplikasi
window.mainloop()