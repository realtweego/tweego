
from fabric import task
from fabric import Connection
from subprocess import call

CMD = 'python3 tweego/tweego/twitter_push.py'
USER = 'ec2-user'
HOST = 'ec2-3-16-111-174.us-east-2.compute.amazonaws.com'
c = Connection(
        user= USER,
        host= HOST,
        connect_kwargs={'key_filename': 'tensor_thyme.pem'}
    )

@task
def hello(context):
    print('Hello')

@task
def install(context):
    c.run('sudo yum -y install python3') #sudo yum -y install python36 doesn't work, so use 3
    print("Installed python 3")
    c.run('sudo yum -y install git')
    print("Installed git")
    c.run('git clone https://www.github.com/realtweego/tweego.git')
    print("Cloned the git repo")
    c.run('pip3 install --user -r tweego/requirements.txt')
    print("Installed the requirements file")
    c.run('pip3 install --user -r tweego/requirements_dev.txt')
    print("Installed the requirements_dev file")
    call(['scp', '-qi', 'tensor_thyme.pem', 'tweego/config.py', f'{USER}@{HOST}:tweego/tweego/config.py'])
    #c.copy('config.py', 'tweego/tweego/config.py') #this has to be manual cos config.py is in the .gitignore, so needs to be scp moved from local machine, destination directory is still correct
    print("Transferred local config files")
    c.run('pip3 install --user -e tweego/') #this is needed cos in the code we use an import tweego statement that presuppsoes an installed tweego version
    print("Finished the installation")
    #c.run(f'sudo echo "30 * * * * ec2-user {CMD}" >> /etc/crontab')


@task
def run(context):
    c.run(f' {CMD}')
