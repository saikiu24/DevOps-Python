from locust import User, task, between

#NeedseveralattributesforaUserclasstowork
#task
#method

class MyUser(User):

    wait_time = between(1,2)

    @task
    def login_url(self):
        print(f'IamloggingintoURL!')

    #classMyUser(User):
    #@task
    #defmy_task(self):
    #print(f'Performingmytask')