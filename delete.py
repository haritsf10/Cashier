# fungsi hapus barang
try:
    def delete_item(self, nama_item):
        """
        Fungsi untuk menghapus item yang diinginkan
        
        Parameter:
            nama_item (str): nama item yang ingin didelete
        """
        for i in range(len(self.list_nama_item)):
            if self.list_nama_item[i] == nama_item:
                del self.transaction[nama_item]
                self.list_nama_item.remove(nama_item)
                break

        print(self.transaction)
except:
    print("Item tidak tersedia di keranjang")

# fungsi reset transaksi
try:
    def reset_transaction(self):
        """Fungsi untuk menghapus semua item yang sudah ditambahkan"""
        self.transaction.clear()
        self.list_nama_item.clear()
        print('Semua item berhasil didelete!')
except:
    print("Format tidak sesuai")