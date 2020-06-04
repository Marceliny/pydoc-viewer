import inspect
import importlib
import pkgutil
from googletrans import Translator


func_indexes = []


def list_modules(ui):
    x = [i[1] for i in pkgutil.iter_modules(None)]
    x = sorted(x)
    ui.all_modules.addItems(x)

        # ui.all_modules.addItem(i[1])


def list_functions(ui):
    if ui.all_funcs.size() != 0:
        ui.all_funcs.clear()
    if func_indexes:
        func_indexes.clear()
    ui.english_doc.clear()
    ui.turkish_doc.clear()

    items = ui.all_modules.selectedItems()
    if not items:
        return

    m = items[0].text()
    ui.statusbar.showMessage(m)

    module = importlib.import_module(m)
    all_functions = inspect.getmembers(module, inspect.isfunction)
    ui.all_funcs.addItems([x[0] for x in all_functions])
    func_indexes.extend([x[1] for x in all_functions])


def print_doc(ui):
    items = ui.all_funcs.selectedIndexes()
    if not items:
        return
    m = func_indexes[items[0].row()]
    en_doc = m.__doc__
    ui.english_doc.setText(en_doc)
    if en_doc:
        print_doc_tr(ui, en_doc)


def print_doc_tr(ui, en_doc):
    translator = Translator()
    doc_tr = translator.translate(en_doc, dest='tr', src='en')
    ui.turkish_doc.setPlainText("\n    "+doc_tr.text)
