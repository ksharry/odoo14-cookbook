# This function invoked only if system already have 14.0.0 version installed
def migrate(cr, version):
    cr.excute("""
    ALTER TABLE library_book 
    RENAME COLUMN date_release TO date_release_char""")
