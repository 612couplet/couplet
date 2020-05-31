# -*- coding: utf-8 -*-
import string

from django.shortcuts import render
from django.views.decorators import csrf
import Couplet.searchfind
from Couplet.model import Model
import logging
vocab_file = 'data/dl-data/couplet/vocabs'

model_dir = 'data/dl-data/models/tf-lib/output_couplet'
m = Model(

    None, None, None, None, vocab_file,

    num_units=1024, layers=4, dropout=0.2,

    batch_size=32, learning_rate=0.0001,

    output_dir=model_dir,
    restore_model=True, init_train=False, init_infer=True)


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        resource = request.POST['q']
        resource = resource + '\n'
        result = Couplet.searchfind.find(resource)
        if result == '':
            result = m.infer(' '.join(resource))
            result = ''.join(result.split(' '))
        ctx['rlt'] = resource
        ctx['rlt1'] = result
        print(resource)
        print(result)
    return render(request, "post.html", ctx)
