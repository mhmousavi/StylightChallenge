# StylightChallenge


docker compose to have mysql without password is provided. 

```bash 
docker-compose build
docker-compose up -d
```

to have initial database, you can use initial.sh

```bash 
bash initial.sh
```

to run migration, you can use migration.sh

```bash 
bash migration.sh
```

migration changes:

index was added to t_budgets to have foreign key on notification.
I just wanted to prevent changes in t_shops and t_budgets. 

also, t_notifications was added to record what type of notification(half, full) that we sent for any budget.


in each round, we should query first to find budgets which are not notified. as we insert a row for any notification, we can prevent faults in sending notifs.

this query use a left outer join on budget to find not notified budget shops.

at last, we just require a query to select which rows should be notified now. we create a notification row as well as printing notif on stdout.


as the assignment said. this python program doesn't need to be awake to get commands, so we can run this task with a task scheduler once a while


to run the python task : 

note: it's better to have virtual environment with :

```bash 
python3.9 -m venv /path/to/new/virtual/environment
```

activate venv :

```bash 
cd /path/to/new/virtual/environment
source bin/activate  
```


install requirements: 
```bash 
pip install requirements.txt
```

and finally run command : 

```bash 
python main.py
```