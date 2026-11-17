class DatabaseRouter:

    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'homwork6':
            return 'homework'

        return 'default'

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'homwork6':
            return 'homework'

        return 'default'

    def allow_relation(self, obj1, obj2, **hints):

        db_list = ('default', 'homework')

        if obj1._state.db in db_list and obj2._state.db in db_list:
            return obj1._state.db == obj2._state.db

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'homwork6':
            return db == 'homework'

        if app_label == 'classwork6':
            return db == 'default'

        return None