from django.db import connection


class ProsodyDatastore:
    @staticmethod
    def get_data_store(username, domain, store):
        data = {}
        with connection.cursor() as cursor:
            cursor.execute(
                    'SELECT key, value FROM prosody.prosody WHERE UPPER("user")=UPPER(%s) AND UPPER(host)=UPPER(%s) AND store=%s',
                    [username, domain, store]
                    )

            data = dict(cursor.fetchall())

        return data

