def json_entity(db, orm):
    class JSONEntity(db.Entity):
        _table_ = 'json_table'
        id = orm.PrimaryKey(int, auto=True)
        first_name = orm.Required(str, 40, nullable=False, )
        second_name = orm.Required(str, 40, nullable=False, )
        age = orm.Optional(int)
        iban = orm.Optional(str)
        credit_card_number = orm.Optional(str)
        credit_card_security_code = orm.Optional(int)
        credit_card_start_date = orm.Optional(str)
        credit_card_end_date = orm.Optional(str)
        address_post_code = orm.Optional(str)
        address_main = orm.Optional(str)
        address_city = orm.Optional(str)
        debt = orm.Optional(str)

    return JSONEntity
