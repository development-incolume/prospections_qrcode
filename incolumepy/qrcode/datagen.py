#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from faker import Faker
from pprint import pprint
from pathlib import Path
import json


Faker.seed(13)
fake = Faker('pt_BR')
# print(fake.ean(length=13, prefixes=('0'*4,)))
funcionarios = []


def login_form(name: str):
    l = name.casefold().split()
    login = l[0]
    for i in l[1:]:
        login += i[0]
    return login


def funcionariosgen():
    for i in range(1000):
        func = {}
        func['id'] = fake.ean(prefixes=('0'*6,))
        func['nome'] = f'{fake.first_name()} {fake.last_name()} {fake.last_name()}'
        func['login'] = login_form(func.get('nome'))
        func['email'] = f"{func.get('login')}@exemplo.com"
        # func['dnasc'] = fake.date()
        func['dnasc'] = f"{fake.date_of_birth(minimum_age=18, maximum_age=65)}"
        # func['cargo'] = fake.job()
        # func['telefone'] = fake.cellphone_number()
        func['rg'] = fake.rg()
        func['cpf'] = fake.cpf()
        funcionarios.append(func)

    # pprint(funcionarios)

    file = Path(__file__).parent/'functionaries.json'

    try:
        with open(file, 'x') as f:
            json.dump(funcionarios, f, indent=4)
    except FileExistsError as e:
        print(e)


def linksgen():
    result = {f'link{x:04}': fake.url() for x in range(1, 1001)}
    file = Path(__file__).parent/'links.json'
    try:
        with open(file, 'x') as f:
            json.dump(result, f, indent=4)
    except FileExistsError as e:
        print(e)


if __name__ == '__main__':
    funcionariosgen()
    linksgen()
