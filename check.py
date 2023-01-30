# fungsi cek order
try:
    def check_order(self):
        """Fungsi untuk menampilkan order yang sudah ada di keranjang"""
        if self.transaction != None:
            print('Pemesanan sudah benar')
        elif self.transaction == None:
            print('Terdapat kesalahan input data')
        print(self.transaction)
except:
    print("Format belum sesuai")