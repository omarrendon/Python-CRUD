import psycopg2

create_table = '''CREATE TABLE IF NOT EXISTS IMPRESORA (ID SERIAL PRIMARY KEY NOT NULL, 
                  NOMBRE_IMPRESORA TEXT NOT NULL, MODELO TEXT NOT NULL, 
                  MARCA TEXT NOT NULL, FECHA_COMPRADA DATE NOT NULL, ULTIMO_MANTENIMIENTO TEXT NOT NULL,
                  UBICACION_FISICA TEXT NOT NULL, NOMBRE_RESPONSABLE TEXT NOT NULL, CORREO_RESPONSABLE TEXT NOT NULL,
                  IP TEXT NOT NULL)'''

class DBConfig:
    def __init__(self):
        pass

    def config_data_base(self):
        try:
            connection=psycopg2.connect(# conexion db
                user= 'agavesoft',
                password = 'becarios2020',
                host='3.237.20.227',
                port='5432',
                database='Omar'
            )
            print('Conexión exitosa')
            return connection
        except(Exception,psycopg2.Error) as error:#
            return ('Error de conexión',error)

    def desconect_database(self, connection):
        try:
            connection.close()
            return print('Base de datos desconectado')
        except (Exception, psycopg2.Error) as error:
            return ('Error de conexión', error)

    def create_record(self, connection, nombre_impresora, modelo, marca,
                        fecha_comprada, ultimo_mantenimiento, ubicacion_fisica,
                        nombre_responsable, correo_responsable, ip):
        try:
            cursor = connection.cursor()
            query_insert = """INSERT INTO impresora(nombre_impresora, modelo, marca, fecha_comprada, 
                            ultimo_mantenimiento, ubicacion_fisica, nombre_responsable, correo_responsable, ip)  
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (nombre_impresora, modelo, marca, fecha_comprada, ultimo_mantenimiento, ubicacion_fisica, nombre_responsable, correo_responsable, ip)

            cursor.execute(query_insert, values)
            connection.commit()
            count = cursor.rowcount
            cursor.close()

            print("\nSE AGREGO ", count, " NUEVA FILA") 
            return count

        except (Exception, psycopg2.Error) as error:
            return ("Fallo insercion a la tabla", error)

    def select_records(self, connection):
        try:
            cursor = connection.cursor()
            query_select = """ SELECT * FROM impresora"""
            cursor.execute(query_select)

            impresoras = cursor.fetchall()
            connection.commit()

            cursor.close()
            return impresoras

        except (Exception, psycopg2.Error) as error:
            return ("Fallo select a la tabla", error)

    def delete_record(self, connection, id):
        try:
            cursor = connection.cursor()

            query_delete = """DELETE FROM impresora WHERE id = %s"""
            cursor.execute(query_delete, (id,))

            count = cursor.rowcount
            connection.commit()

            return count

        except (Exception, psycopg2.Error) as error:
            return ("Fallo eliminar fila ", error)

    def select_by_name(self, connection, id):
        try:
            cursor = connection.cursor()
            sql_by_name = """SELECT * FROM impresora WHERE id = %s"""

            cursor.execute( sql_by_name, (id,) )
            impresora_nombre = cursor.fetchone()
            connection.commit()

            return impresora_nombre
            cursor.close()

        except (Exception, psycopg2.Error) as error:
            print("ERROR AL SELECCIONAR LA IMPRESORA", error)

    def update_record(self, connection,  nombre_impresora, modelo, marca,
                      fecha_comprada, ultimo_mantenimiento, ubicacion_fisica,
                      nombre_responsable, correo_responsable, ip, id):
        if(nombre_impresora):
            try:
                cursor = connection.cursor()
                # print("Registro antes de ser modificado")
                # sql_record = "SELECT * FROM impresora WHERE id = %s"
                # cursor.execute(sql_record, (id))
                # record = cursor.fetchone()
                # print(record)

                # Update single record now
                sql_update_query = """UPDATE impresora SET nombre_impresora = %s, modelo = %s, 
                                    marca = %s, fecha_comprada = %s, ultimo_mantenimiento = %s,
                                    ubicacion_fisica = %s, nombre_responsable = %s, correo_responsable = %s, ip = %s
                                    WHERE id =%s"""
                cursor.execute(sql_update_query, ( nombre_impresora, modelo, marca, fecha_comprada, ultimo_mantenimiento,
                            ubicacion_fisica, nombre_responsable, correo_responsable, ip, id))
                connection.commit()
                count = cursor.rowcount
                print("\n", count, "REGISTRO ACTUALIZADO CORRECTAMENTE!")

                # print("Tabla despues de ser actualizada")
                # sql_select_query = """SELECT * FROM impresora WHERE id = %s"""
                # cursor.execute(sql_select_query, (id))
                # record = cursor.fetchone()
                # print(record)

            except (Exception, psycopg2.Error) as error:
                print('Algo salio mal al actualizar el registro', error)
