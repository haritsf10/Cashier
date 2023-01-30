# Import function for add item
import add

# Import update for update item name/qty/price
import update

# Import delete for delete item and reset transactions
import delete

# Import check for check order
import check

# Import total for calculate total price and know the price to pay
import total

class Trnsct_123():
    def init(self):
        self.transaction = {}
        self.list_nama_item = []

transaction = Trnsct_123()
transaction.init()

# Menu - Cashier
def menu():
    print('Cashier')
    print('1 Add Item')
    print('2 Update Item')
    print('3 Delete Item')
    print('4 Reset Transaction')
    print('5 Check Order')
    print('6 Total Transaction')
    print('0 Exit')
    
    # Prompting user to enter any task above 
    pilih_menu = input('Pilih: ')

    # After user enter task no, respective task functions will be executed
    try:
        if pilih_menu == '1':
            print('Silakan tambah barang')
            nama_item = str(input('Nama: '))
            jumlah_item = int(input('Jumlah: '))
            harga_item = int(input('Harga: '))
            add.add_item(transaction, nama_item, jumlah_item, harga_item)
            menu()
        elif pilih_menu == '2':
            print('1 Update Item Name')
            print('2 Update Item Qty')
            print('3 Update Item Price')

            pilih_update = input('')
            
            if pilih_update == '1':
                nama_item_lama = str(input('Nama Item: '))
                nama_item_baru = str(input('Nama Baru: '))
                update.update_item_name(transaction,nama_item_lama, nama_item_baru)       
                menu()
            elif pilih_update == '2':
                nama_item = str(input('Nama Item: '))
                qty_baru = int(input('Qty Baru: '))
                update.update_item_qty(transaction, nama_item, qty_baru)
                menu()      
            elif pilih_update == '3':
                nama_item = str(input('Nama Item: '))
                price_baru = int(input('Price Baru: '))
                update.update_item_price(transaction, nama_item, price_baru)
                menu()
            # If user key in no outside of available inputs, will back to menu
            else:
                menu()
        elif pilih_menu == '3':
            nama_item = str(input('Delete: '))
            delete.delete_item(transaction, nama_item)
            menu()
        elif pilih_menu == '4':
            delete.reset_transaction(transaction)
            menu()
        elif pilih_menu == '5':
            check.check_order(transaction)
            menu()
        # After total transaction, will exit program
        elif pilih_menu == '6':
            total.total_price(transaction)
        # If user key in no outside of available inputs, will exit program
        else:
            pass
    except:
        print('Format tidak sesuai')


# Displaying menu when cashier.py file is executed on terminal
menu()