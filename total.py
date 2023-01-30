# fungsi total harga
try:
    def total_price(self):
        """Fungsi menghitung total belanja item final"""
        total_harga = 0
        for i in range(len(self.list_nama_item)):
            total_harga = total_harga + self.transaction[self.list_nama_item[i]][2]
            if total_harga > 500000:
                total_bayar = total_harga * 0.9 # apabila total belanja >500_000, diskon 10%
            elif total_harga > 300000:
                total_bayar = total_harga * 0.92 # apabila total belanja >300_000, diskon 8%
            elif total_harga > 200000:
                total_bayar = total_harga * 0.95 # apabila total belanja >200_000, diskon 5%
            else:
                total_bayar = total_harga
            
        print(f'Item yang dibeli adalah {self.transaction}')
        print(f'Total Belanja yang harus dibayarkan adalah Rp. {total_bayar}')
except:
    print("Format tidak sesuai")