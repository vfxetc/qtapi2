from .moduleproxy import ModuleProxy

import qtpy as _Qt
import qtpy.QtCore
import qtpy.QtGui
import qtpy.QtWidgets


_prefixes = ['Q', 'Qt', '']
_modules = []
Q = ModuleProxy(_prefixes, _modules)

_order = {
    'QtCore': -30,
    'QtGui': -20,
    'QtWidgets': -10
}

for name in sorted(dir(_Qt), key=lambda name: _order.get(name, 0)):
    module = getattr(_Qt, name)
    _modules.append(module)
    setattr(Q, name[2:], ModuleProxy(_prefixes, (module, )))

_modules.append(_Qt.QtCore.Qt)
Q.t = ModuleProxy(_prefixes, (_Qt.QtCore.Qt, ))
