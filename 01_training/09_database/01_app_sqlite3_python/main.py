from database import ConnectionFactory, Model

if __name__ == "__main__":
    conn = ConnectionFactory("SQLiteConnect").make()
    conn.connect()
    model = Model(conn.connection)
    model.create()
    model.insert("Candido", "77777777777", "candido@email.com")
    model.insert("José", "97777777777", "jose@email.com")
    print(model.find_all())
    print(model.find("77777777777"))
    print(model.delete("77777777777"))
    print(model.find_all())
    conn.disconnect()
    