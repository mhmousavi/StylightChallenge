ALTER TABLE t_budgets DROP PRIMARY KEY;
ALTER TABLE t_budgets ADD a_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY;

CREATE TABLE t_notifications (
    a_id                INT(11)       NOT NULL AUTO_INCREMENT,
    a_budget_id         INT(11)       NOT NULL REFERENCES t_budgets (a_id),
    a_notification_type INT(11)       NOT NULL,
    PRIMARY KEY (a_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
