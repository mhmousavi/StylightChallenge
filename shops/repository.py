from base_repository.repository import RepositoryManger


class ShopRepository(RepositoryManger):

    def deactivate_shop(self, shop_id):
        cursor = self.connection.cursor()
        query = (
            """
            UPDATE t_shops SET a_online = FALSE WHERE a_id = {}
            """.format(shop_id)
        )
        cursor.execute(query)
        self.connection.commit()
