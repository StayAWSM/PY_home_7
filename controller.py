import view
import import_info
import data_mod

def main_func():
    """Основной модуль"""
    a = view.interaction()
    if a[1] == 1:
        import_info.create_data(a[0])
    if a[1] == 2:
        view.res_find(data_mod.get_data(a[0]))
    if a[1] == 3:
        view.display()
    if a[1] == 4:
        view.res_find(import_info.delete_data(a[0]))
