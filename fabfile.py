
from fabric import task
from fabric import Connection

c = Connection(
        user='ec2-user',
        host='ec2-52-30-194-199.eu-west-1.compute.amazonaws.com',
        connect_kwargs={'key_filename': 'basil.pem'}
    )

CMD = 'python3 /home/ec2-user/tweego/tweego/twitter_push.py'

@task
def hello(context):
    print('Hello')

@task
def install(context):
    c.run('sudo yum install python3')
    c.run('sudo yum install git')
    c.run('git clone https://www.github.com/realtweego/tweego.git')
    c.run('pip3 install --user -r tweego/requirements.txt')
    # c.copy('config.py', 'tweego/tweego/config.py')
    c.run(f'sudo echo "30 * * * * ec2-user {CMD}" >> /etc/crontab')

@task
def tweego(context):
    c.run(f'python3 {CMD}')




