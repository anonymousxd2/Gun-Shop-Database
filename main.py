import mysql.connector

# Database connection function
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gun_shop_db"
    )

# Nayi Gun add karne ka function
def add_weapon():
    conn = connect_to_db()
    cursor = conn.cursor()
    print("\n--- Enter Weapon Details ---")
    model = input("Model: ")
    brand = input("Brand: ")
    price = input("Price: ")
    
    query = "INSERT INTO weapons (model_name, brand, price) VALUES (%s, %s, %s)"
    cursor.execute(query, (model, brand, price))
    conn.commit()
    print("Gun successfully saved in Database!")
    conn.close()

# Saari Guns dekhne ka function
def view_weapons():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weapons")
    print("\n--- Current Inventory ---")
    for x in cursor.fetchall():
        print(x)
    conn.close()

if __name__ == "__main__":
    while True:
        print("\n1. View Inventory")
        print("2. Add New Weapon")
        print("3. Exit")
        choice = input("Select Option: ")
        if choice == '1': view_weapons()
        elif choice == '2': add_weapon()
        elif choice == '3': break
