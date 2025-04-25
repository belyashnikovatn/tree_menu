from django.shortcuts import render
from django.http import Http404


def generic_view(request, template_name):
    """Общее представление для рендеринга шаблонов."""
    try:
        return render(request, f'{template_name}.html')
    except:
        raise Http404(f"Шаблон {template_name}.html не найден.")
