from django import template
from tree_items.models import MenuItem
from django.utils.safestring import mark_safe
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path
    try:
        current_url_name = resolve(current_path).url_name
    except:
        current_url_name = None

    items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    items_dict = {}

    for item in items:
        items_dict[item.id] = {
            'item': item,
            'children': [],
            'parent_id': item.parent_id
        }

    tree = []
    for item_id, node in items_dict.items():
        if node['parent_id']:
            items_dict[node['parent_id']]['children'].append(node)
        else:
            tree.append(node)

    def is_active(item):
        return item.get_absolute_url() == current_path or item.named_url == current_url_name

    active_path = []

    def find_active_path(nodes):
        for node in nodes:
            if is_active(node['item']):
                active_path.append(node['item'])
                return True
            if find_active_path(node['children']):
                active_path.append(node['item'])
                return True
        return False

    find_active_path(tree)

    def render_menu(nodes, level=0):
        html = '<ul>'
        for node in nodes:
            item = node['item']
            children = node['children']
            active = is_active(item)
            expanded = item in active_path or level == 0

            html += f"<li>{'<strong>' if active else ''}<a href='{item.get_absolute_url()}'>{item.name}</a>{'</strong>' if active else ''}"
            if children and expanded:
                html += render_menu(children, level + 1)
            html += '</li>'
        html += '</ul>'
        return html

    return mark_safe(render_menu(tree))
