import db_funcs

# db_funcs.add_one("Aimen", "Gamin", "cringe@mogulmoves.com")
# db_funcs.delete_one_by_id('7')

# ppl = [
#     ('Sean', 'McDonald', 'shale@codemy.com'),
#     ('Shoru', 'Poru', 'shnoob@codemy.com'),
#     ('Dean', 'Park', 'deezpark@codemy.com'),
# ]
# db_funcs.add_many(ppl)

db_funcs.email_lookup('deezpark@codemy.com')
db_funcs.update_email(9, 'daepa@codemy.com')
db_funcs.email_lookup('deezpark@codemy.com')
db_funcs.email_lookup('daepa@codemy.com')

# db_funcs.show_all()