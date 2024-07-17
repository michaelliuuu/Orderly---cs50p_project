from project import get_menu_from_csv, main_menu, display_menu

def test_get_menu_from_csv():
    assert(get_menu_from_csv()) == {'Ha Gao (4 pc)': 4.25, 'Siu Mai (4 pc)': 4.25, 'BBQ Pork Bun': 2.45, 'Steamed Shrimp Rice Roll': 5.25}

def test_main_menu():
    assert(main_menu()) == "Welcome to Orderly!\n1. Returning Customer\n2. New Customer\n3. Exit"

def test_display_menu():
    assert(display_menu()) == """+--------------------------+---------+
| Item                     | Price   |
+==========================+=========+
| Ha Gao (4 pc)            | $4.25   |
+--------------------------+---------+
| Siu Mai (4 pc)           | $4.25   |
+--------------------------+---------+
| BBQ Pork Bun             | $2.45   |
+--------------------------+---------+
| Steamed Shrimp Rice Roll | $5.25   |
+--------------------------+---------+"""
