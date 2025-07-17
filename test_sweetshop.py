import unittest
from database import get_db_connection, init_db

class TestSweetShop(unittest.TestCase):
    def setUp(self):
        init_db()

    def test_add_sweet(self):
        conn = get_db_connection()
        conn.execute("INSERT INTO sweets (name, category, price, quantity) VALUES (?, ?, ?, ?)",
                     ("Kaju Katli", "Nut-Based", 50, 20))
        conn.commit()
        sweets = conn.execute("SELECT * FROM sweets WHERE name='Kaju Katli'").fetchall()
        self.assertEqual(len(sweets), 1)
        conn.close()

if __name__ == '__main__':
    unittest.main()
