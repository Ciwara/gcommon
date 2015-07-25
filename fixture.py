#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Fadiga

from __future__ import (unicode_literals, absolute_import, division,
                        print_function)

import os, sys; sys.path.append(os.path.abspath('../'))

from models import Stores
from Common.fixture import AdminFixture


class fixt_init(AdminFixture):
    """docstring for fixt_init"""
    def __init__(self):
        super(AdminFixture, self).__init__()
        self.LIST_CREAT.append(Stores(name=u"magasin N°1", stock_maxi=5000),)
