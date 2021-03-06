import sqlite3

def get_connection():
    path = './dapp.sqlite3'
    connection = sqlite3.connect(path)
    return connection

def set_product(id, name, price, image):
    print(f"Updating product with id {id}: name={name}, price={price}, image={image}")
    result = True
    try:
        conn = get_connection()
        sql = 'UPDATE products SET name=?, price=?, image=? WHERE _rowid_=?'
        cursor = conn.cursor()
        c = cursor.execute(sql, (name, price, image, id))
        conn.commit()
        conn.close()
        print(f"Updated product with id {id}")
    except Exception as ex:
        print('Exception in set_product function in db:- ' + ex)
        result = False
    finally:
        return result

def get_products():
    records = None
    conn = get_connection()
    sql = 'SELECT * from products'
    cursor = conn.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    products = []
    for record in records:
        products.append({
            'id': records.index(record) + 1,
            'name': record[0],
            'price': record[1],
            'image': record[2]
        })
    return products


def add_order_data(wallet_address, tx, name, invoice_id):
    result = True
    try:
        conn = get_connection()
        sql = 'INSERT INTO orders(wallet_address,tx,product_name,invoice_id) VALUES (?,?,?,?)'
        cursor = conn.cursor()
        cursor.execute(sql, (wallet_address, tx, name, invoice_id))
        conn.commit()
        conn.close()
    except Exception as ex:
        print('Exception in add_order function in db:- ' + ex)
        result = False
    finally:
        return result

def get_orders(wallet_address):
    records = None
    conn = get_connection()
    sql = 'SELECT * from orders where wallet_address = ?'
    cursor = conn.cursor()
    cursor.execute(sql, (wallet_address,))
    records = cursor.fetchall()
    return records

def remove_product(id):
    print(f"Removing product with id {id}")
    result = True
    try:
        conn = get_connection()
        sql = 'DELETE FROM products WHERE _rowid_=?'
        cursor = conn.cursor()
        cursor.execute(sql, (id))
    except Exception as ex:
        print('Exception in remove_product function in db:- ' + ex)
        result = False
    finally:
        conn.close()
        return result