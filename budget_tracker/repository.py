from base_repository.repository import RepositoryManger


class BudgetRepository(RepositoryManger):

    def get_all_percent_spent_budget_in_list(self, lst, percent, current_month):
        cursor = self.connection.cursor()
        if len(lst) == 0:
            return []
        query = (
            """
            SELECT t_budgets.a_id, t_budgets.a_shop_id, t_budgets.a_month, t_budgets.a_budget_amount, t_budgets.a_amount_spent
            FROM  t_budgets
            LEFT OUTER JOIN t_shops ON t_budgets.a_shop_id = t_shops.a_id
            WHERE t_budgets.a_amount_spent >= {} * t_budgets.a_budget_amount 
            AND t_budgets.a_month = '{}' 
            AND t_shops.a_online = TRUE
            AND t_budgets.a_id IN {}
            """.format(percent, current_month, tuple(lst))
        )
        cursor.execute(query)
        ret = []
        for _ in cursor:
            ret.append({
                'a_id': _[0],
                'a_shop_id': _[1],
                'a_month': _[2],
                'a_budget_amount': _[3],
                'a_amount_spent': _[4],
            })
        return ret
