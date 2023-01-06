class NotificationPrint:
    def output_in_stdout(self, date, shop_id, cur_month_budget, cur_month_expenditure):
        print("######## notification message ########")
        print("current date: ", date)
        print("shop id: ", shop_id)
        print("current month budget: ", cur_month_budget)
        print("current month expenditure: ", cur_month_expenditure)
        print("percentage: ", cur_month_expenditure / cur_month_budget * 100)
        print("######## end message ########")
