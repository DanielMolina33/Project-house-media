from rolepermissions.roles import AbstractUserRole

class Seller(AbstractUserRole):
    available_permissions = {
        'add_item' : True,
        'change_item': True,
        'delete_item': True,
        'view_item': True,
    }

class Buyer(AbstractUserRole):
    available_permissions = {
        'add_item' : False,
        'change_item': False,
        'delete_item': False,
        'view_item': True,
    }