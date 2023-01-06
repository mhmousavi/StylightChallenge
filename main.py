from datetime import datetime

from budget_tracker.repository import BudgetRepository
from notifications.notification_manager import NotificationPrint
from notifications.repository import NotificationRepository
from shops.repository import ShopRepository

notifications_repo_singleton = NotificationRepository()
budgets_repo_singleton = BudgetRepository()
shops_repo_singleton = ShopRepository()


def send_notification_to_half(current_day):
    current_month = str(current_day.replace(day=1).date())

    not_notified_budgets = notifications_repo_singleton.get_not_notified_budgets(
        current_month
    )

    to_notify_list = budgets_repo_singleton.get_all_percent_spent_budget_in_list(
        not_notified_budgets,
        0.5,
        current_month
    )
    for item in to_notify_list:
        notifications_repo_singleton.create_notification(
            item['a_id'],
            notifications_repo_singleton.HALF
        )
        NotificationPrint().output_in_stdout(
            str(current_day.date()),
            item['a_id'],
            item['a_budget_amount'],
            item['a_amount_spent'],
        )


############################

def send_notification_to_full(current_day):
    current_month = str(current_day.replace(day=1).date())

    half_notified_budgets = notifications_repo_singleton.get_notified_budgets_with_type(
        notifications_repo_singleton.FULL,
        current_month
    )

    to_notify_list = budgets_repo_singleton.get_all_percent_spent_budget_in_list(
        half_notified_budgets,
        1,
        current_month
    )

    for item in to_notify_list:
        notifications_repo_singleton.create_notification(
            item['a_id'],
            notifications_repo_singleton.FULL
        )
        shops_repo_singleton.deactivate_shop(item['a_shop_id'])
        NotificationPrint().output_in_stdout(
            str(current_day.date()),
            item['a_id'],
            item['a_budget_amount'],
            item['a_amount_spent'],
        )


send_notification_to_half(datetime.today())
send_notification_to_full(datetime.today())
