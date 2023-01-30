# fungsi update nama barang
try:
    def update_item_name(self, nama_item, nama_baru):
        """
        Fungsi update nama item yang sudah ditambahkan menjadi nama item baru yang kita inginkan
        
        Parameter:
            nama_item (str): nama item lama yang ingin diubah
            nama_baru (str): nama baru yang diinginkan untuk mengganti nama item lama
        """
        self.transaction[nama_baru] = self.transaction.pop(nama_item)
        for i in range(len(self.list_nama_item)):
            if self.list_nama_item[i] == nama_item:
                self.list_nama_item[i] = nama_baru
except:
    print("Format tidak sesuai")
# fungsi update jumlah barang
try:
    def update_item_qty(self, nama_item, jumlah_baru):
        """
        Fungsi untuk update kuantitas dari item yang sudah kita tambahkan
        
        Parameter:
            nama_item (str): nama item yang kuantitasnya ingin diubah
            jumlah_baru (int): kuantitas baru untuk menggantikan kuantitas lama"""
        for i in range(len(self.list_nama_item)):
            if self.list_nama_item[i] == nama_item:
                self.transaction[nama_item][0] = jumlah_baru
                self.transaction[nama_item][2] = self.transaction[nama_item][0] * self.transaction[nama_item][1] 
except:
    print("Format tidak sesuai")
# fungsi update harga barang
try:
    def update_item_price(self, nama_item, harga_baru):
        """
        Fungsi untuk update harga dari item yang sudah kita tambahkan
        
        Parameter:
            nama_item (str): nama item yang harganya ingin diubah
            harga_baru (int): harga baru untuk menggantikan harga lama
        """
        for i in range(len(self.list_nama_item)):
            if self.list_nama_item[i] == nama_item:
                self.transaction[nama_item][1] = harga_baru
                self.transaction[nama_item][2] = self.transaction[nama_item][0] * self.transaction[nama_item][1]
except:
    print("Format tidak sesuai")