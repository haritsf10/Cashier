# fungsi menambahkan barang  
try:
    def add_item(self, nama_item, jumlah_item, harga_per_item):
            """
            Fungsi untuk menambah jumlah item yang ingin dibeli
            
            Parameter:
                nama_item (str): nama item yang ingin dibeli
                jumlah_item (int): jumlah item yang ingin dibeli
                harga_per_item (int): harga per item yang ingin dibeli
            """
            new_item = [] # list untuk menampung parameter yang dimasukkan dan akan menjadi value di dict
            
            self.nama_item = nama_item
            self.jumlah_item = jumlah_item
            self.harga_per_item = harga_per_item
            self.harga_total = self.jumlah_item * self.harga_per_item
            
            # append nama, jumlah, dan harga ke list new_item
            new_item.append(self.jumlah_item)
            new_item.append(self.harga_per_item)
            new_item.append(self.harga_total)
            
            # new_item jadi value, nama_item jadi key
            self.transaction[self.nama_item] = new_item
            self.list_nama_item.append(nama_item)

            print(self.transaction)
except:
    print("Barang yang diinput belum sesuai")