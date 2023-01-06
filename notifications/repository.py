from base_repository.repository import RepositoryManger


class NotificationRepository(RepositoryManger):
    HALF = 1
    FULL = 2

    def get_not_notified_budgets(self, current_month):
        cursor = self.connection.cursor()
        query = (
            """
            SELECT t_budgets.a_id
            FROM t_budgets
            LEFT OUTER JOIN t_notifications ON t_budgets.a_id = t_notifications.a_budget_id 
            WHERE t_notifications.a_notification_type IS NULL AND t_budgets.a_month = '{}'
            """.format(current_month)
        )
        cursor.execute(query)
        ret = []
        for _ in cursor:
            ret.append(_[0])

        return ret

    def get_notified_budgets_with_type(self, type, current_month):
        cursor = self.connection.cursor()
        query = (
            """
            SELECT t_budgets.a_id
            FROM t_budgets
            LEFT OUTER JOIN t_notifications ON t_budgets.a_id = t_notifications.a_budget_id 
            WHERE t_notifications.a_notification_type = {} AND t_budgets.a_month = '{}'
            """.format(type, current_month)
        )
        cursor.execute(query)
        ret = []
        for _ in cursor:
            ret.append(_[0])

        return ret

    def create_notification(self, budget_id, type):
        cursor = self.connection.cursor()
        query = (
            """
            INSERT INTO t_notifications (a_budget_id, a_notification_type)
            VALUES ({}, {})
            """.format(budget_id, type)
        )
        cursor.execute(query)
        self.connection.commit()
