primeiro, obter o projeto:

$ git clone https://github.com/eldioschalm/colaborador.git

criar o ambiente virtual:

$ virtualenv colaborador

instalar os pacotes básicos requeridos pelo projeto:

pacotes básicos para python-ldap
$ sudo aptitude install libsasl2-dev python-dev libldap2-dev libssl-dev

instalar pacotes do projeto:

$ pip install -r requirements.txt

rodar migração do projeto:

$ python manage.py migrate
