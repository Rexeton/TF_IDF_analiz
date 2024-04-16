from django.shortcuts import render
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import re
import json
from .models import Analiz_one_dok, Analiz_doks
import math

def word_count(f):
    # не нашел вариант без промежуточного файла, upload_to не срабатывает в form TODO сделать без промежуточного файла
    path = default_storage.save('tmp/text.txt', ContentFile(f.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    dict_of_word = {}
    object_list = {}
    with open(tmp_file, "r", encoding="utf-8") as text:
        for elem in text:
            words = re.findall('[a-zа-яё]+', elem.lower(),
                               flags=re.IGNORECASE)  # нашел на просторах, вариант для чистых слов, без сокращений
            for word in words:
                if word in dict_of_word:
                    dict_of_word[word] += 1
                    object_list[word][0] += 1
                else:
                    dict_of_word[word] = 1
                    object_list[word] = [1, 0]
    os.remove(tmp_file)
    return dict_of_word, object_list

def template_view(request):
    if request.method == "GET":
        object_list0 = None
        return render(request, 'app_text_analiz/template_form.html', context=object_list0)
    if request.method == "POST":
        files = request.FILES.getlist('file')
        if 'add_file' in request.POST:
            if files:
                error_list = []
                for f in files:
                    try:
                        all_words = Analiz_doks.objects.filter(id=1).values('dic_words')[0]
                        if len(all_words) == 0:
                            all_words = {}
                        else:
                            all_words = json.loads(all_words['dic_words'])
                        all_doc = Analiz_one_dok.objects.count()
                        dict_of_word, object_list = word_count(f)
                        dict_of_word_json = json.dumps({k: dict_of_word[k] for k in sorted(dict_of_word)},
                                                       ensure_ascii=False)  # сортировка чтоб не учитывать повторные загрузки документа
                        k_t = 0  # для учета повторов
                        if not Analiz_one_dok.objects.filter(words=dict_of_word_json):
                            analiz_one_dok = Analiz_one_dok(words=dict_of_word_json)
                            analiz_one_dok.clean_fields()
                            analiz_one_dok.save()  # запись в базу данных
                            k_t = 1
                        for el in dict_of_word:
                            if el in all_words:
                                all_words[el][0] += k_t
                                all_words[el][1] = math.log10((all_doc + k_t) / all_words[el][0])
                                object_list[el][0] = round(object_list[el][0] / len(dict_of_word), 3)
                                object_list[el][1] = round(all_words[el][1], 3)
                            else:
                                all_words[el] = [1, 0]
                        all_words = json.dumps(all_words, ensure_ascii=False)
                        Analiz_doks.objects.filter(id=1).update(dic_words=all_words)
                        object_list = sorted(object_list.items(), key=lambda x: x[1][0], reverse=True)[
                                      0:min(len(object_list), 50)]
                        object_list0 = {
                            'object_list0': [{'name': el_d[0], 'tf': el_d[1][0], 'idf': el_d[1][1]} for el_d in
                                             object_list]}
                        return render(request, 'app_text_analiz/template_form.html', context=object_list0)
                    except Exception as e:
                        error_list.append(str(e))
                        print(f'errrrrrrrooooooooooooooorrrrrrrrrrrrrrrrrrrrrrr {e}')
        elif 'recount' in request.POST:
            analiz_one_dok = Analiz_one_dok.objects.all()
            all_doc = Analiz_one_dok.objects.count()
            all_words = {}
            for elem in analiz_one_dok.values('words'):
                elem_json = json.loads(elem['words'])
                for el in elem_json:
                    if el in all_words:
                        all_words[el][0] += 1
                        all_words[el][1] = math.log10((all_doc) / all_words[el][0])
                    else:
                        all_words[el] = [1, 0]
            print(all_words)
            all_words = json.dumps(all_words, ensure_ascii=False)
            Analiz_doks.objects.filter(id=1).update(dic_words=all_words)

        return render(request, 'app_text_analiz/template_form.html')
