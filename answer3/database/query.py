from database.connection import connect
from database.config import Config
from model.MedicalImage import MedicalImage, DevicesDict

class Query:
    config: Config

    def __init__(self, config: Config):
        self.config = config

    def probar(self):
        conn = connect(config=self.config)
        print("SIIU")

    def get_elements(self):
        try:
            conn = connect(config=self.config)
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM medical_images')
            rows = cursor.fetchall()
            
            result = []
            for row in rows:
                image =  MedicalImage(id=row[0], data=row[1], deviceName=row[2])
                result.append(image)
            
            return result

        except Exception as ex:
            print(ex)

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
    
    def get_element_by_id(self, id: str):
        try:
            conn = connect(config=self.config)
            cursor = conn.cursor()

            params = (id,)
            print(params)
            cursor.execute('SELECT * FROM medical_images WHERE id=%s', params)
            result = cursor.fetchone()
            if result is not None:
                return MedicalImage(id=result[0], data=result[1], deviceName=result[2])

            return None

        except Exception as ex:
            print(ex)

            return None
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def create_images(self, devices_images: DevicesDict):
        try:
            conn = connect(self.config)
            cursor = conn.cursor()

            for device in devices_images:
                params = (device["id"], device["data"], device["deviceName"])
                cursor.execute('INSERT INTO medical_images VALUES (%s, %s, %s)', params)
            
            conn.commit()
            return True

        except Exception as ex:
            print(ex)
            return False

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
    
    def update_image(self, id: str, new_image: MedicalImage):
        try:
            conn = connect(self.config)
            cursor = conn.cursor()

            params = (new_image["id"], new_image["data"], new_image["deviceName"], id)
            cursor.execute('UPDATE medical_images SET id=%s, data=%s, device_name=%s  WHERE id=%s', params)

            conn.commit()
            return True

        except Exception as ex:
            print(ex)

            return False

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def delete_element(self, id: str):
        try:
            conn = connect(self.config)
            cursor = conn.cursor()

            params = (id,)
            cursor.execute('DELETE FROM medical_images WHERE id=%s', params)

            conn.commit()
            return True

        except Exception as ex:
            print(ex)

            return False

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()