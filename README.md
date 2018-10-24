qtapi2
======

An honest representation of the Qt API, provided by [Qt.py][qt.py].

This project is born of [a blog post][blog] I wrote.

Most tutorials and examples for PyQt/PySide replicate the feeling of the static code by importing everything into the global namespace:

```
import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)
hello = QPushButton("Hello world!")
hello.show()
exit(app.exec_())
```

This is an anti-pattern, as we know that `from whatever import *` is bad.

`qtapi2` dynamically locates the symbols you likely meant to use, providing something much more akin to writing Qt in C++:

```
import sys
from qtapi2 import Q

app = Q.Application(sys.argv)
hello = Q.PushButton("Hello world!")
hello.show()
exit(app.exec_())
```

If you need a specific symbol that collides, you can refer to them through their module:

```
Q.Widgets.Dialog
# vs
Q.t.Dialog
```

or their full names:

```
Q.Widgets.QDialog
# vs
Q.t.WindowType.Dialog
```


[qt.py]: https://github.com/mottosso/Qt.py
[blog]: https://mikeboers.com/blog/2015/07/04/static-libraries-in-a-dynamic-world
