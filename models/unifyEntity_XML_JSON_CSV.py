def json_xml_csv_combine_entity(db, orm):
    class UnifyJsonXmlCsv(db.Entity):
        _table_ = 'unify_json_xml_csv_table'
        first_name = orm.Required(str, 40, nullable=False)
        second_name = orm.Required(str, 40, nullable=False)
        age = orm.Optional(int)
    return UnifyJsonXmlCsv
