def json_xml_combine_entity(db, orm):
    class UnifyJsonXml(db.Entity):
        _table_ = 'unify_json_xml_table'
        first_name = orm.Required(str, 40, nullable=False)
        second_name = orm.Required(str, 40, nullable=False)
        age = orm.Optional(int)
        address_post_code = orm.Optional(str)

    return UnifyJsonXml
