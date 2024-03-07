from django.template.defaultfilters import slugify
from transliterate import translit

title = 'Анджелина Джоли'
title_en = translit(title,'ru', reversed=True)
slug = slugify(title_en)
print(slug)
