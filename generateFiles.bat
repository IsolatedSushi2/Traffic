pyrcc5 qtresources.qrc -o qtresources_rc.py
pyrcc5 cameraSelector.qrc -o cameraSelector_rc.py
pyuic5 -x ui/mainwindow.ui -o src/ui/ui.py
pyuic5 -x ui/cameraSelector.ui -o src/ui/camSelectui.py
pyuic5 -x ui/legendSelector.ui -o src/ui/legendSelector.py
