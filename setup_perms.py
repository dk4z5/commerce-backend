from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

emp, created = Group.objects.get_or_create(name='empregados')

perm_add_venda = Permission.objects.get(codename='add_venda')
perm_view_venda = Permission.objects.get(codename='view_venda')

perm_view_estoque = Permission.objects.get(codename='view_estoque')

perm_view_produto = Permission.objects.get(codename='view_produto')

emp.permissions.add(perm_add_venda)
emp.permissions.add(perm_view_venda)
emp.permissions.add(perm_view_estoque)
emp.permissions.add(perm_view_produto)