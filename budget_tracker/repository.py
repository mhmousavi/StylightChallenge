from base_repository.repository import RepositoryManger


class BudgetRepository(RepositoryManger):

    def get_all_percent_spent_budget_in_list(self, lst, percent, current_month):
        cursor = self.connection.cursor()
        not_in_query = (
            " AND a_id IN {}".format(tuple(lst))
        ) if lst != [] else ""
        query = (
                    "SELECT * FROM t_budgets WHERE a_amount_spent >= {} * a_budget_amount AND a_month = {}".format(
                        percent, current_month
                    )
                ) + not_in_query
        cursor.execute(query)
        ret = []
        for _ in cursor:
            ret.append({
                'a_shop_id': _[0],
                'a_month': _[1],
                'a_budget_amount': _[2],
                'a_amount_spent': _[3],
                'a_id': _[4],
            })
        return ret
