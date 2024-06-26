from PyQt6.QtWidgets import QMessageBox, QTreeWidgetItem

def loadDataToTreeWidget(treeWidget, load_data_function):
    data = load_data_function()
    treeWidget.clear()
    for row in data:
        parent_item = QTreeWidgetItem()
        for i in range(len(row)):
            parent_item.setText(i, str(row[i]))
        treeWidget.addTopLevelItem(parent_item)

def handleAdd(treeWidget, add_function, load_data_function, input_widgets, tab):
    inputs = [widget.currentText().strip() if hasattr(widget, 'currentText') else widget.text().strip() for widget in input_widgets]
    
    if not all(inputs):
        QMessageBox.warning(tab, "Thông báo", "Vui lòng nhập đầy đủ thông tin!")
        return
    
    if not add_function(*inputs):
        QMessageBox.warning(tab, "Thông báo", "ID đã tồn tại!")
        for widget in input_widgets:
            widget.clear()
        return
    
    QMessageBox.information(tab, "Thông báo", "Thêm thành công!")
    loadDataToTreeWidget(treeWidget, load_data_function)
    
    for widget in input_widgets:
        widget.clear()

def handleUpdate(treeWidget, update_function, load_data_function, input_widgets, tab):
    inputs = [widget.currentText().strip() if hasattr(widget, 'currentText') else widget.text().strip() for widget in input_widgets]

    if not all(inputs):
        QMessageBox.warning(tab, "Thông báo", "Vui lòng nhập đầy đủ thông tin!")
        return

    if update_function(*inputs):
        QMessageBox.information(tab, "Thông báo", "Cập nhật thành công!")
        loadDataToTreeWidget(treeWidget, load_data_function)
        for widget in input_widgets:
            widget.clear()
    else:
        QMessageBox.warning(tab, "Thông báo", "Cập nhật thất bại!")

def handleDelete(treeWidget, delete_function, load_data_function, tab):
    selected_items = treeWidget.selectedItems()

    if not selected_items:
        QMessageBox.warning(tab, "Thông báo", "Vui lòng chọn dòng cần xóa!")
        return

    id = selected_items[0].text(0)

    reply = QMessageBox.question(treeWidget, 'Xác nhận xóa', 
            f'Bạn có chắc chắn muốn xóa ID {id}?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
            QMessageBox.StandardButton.No)

    if reply == QMessageBox.StandardButton.Yes:
        if delete_function(id):
            loadDataToTreeWidget(treeWidget, load_data_function)
            QMessageBox.information(treeWidget, 'Thông báo', 'Xóa thành công!')
        else:
            QMessageBox.critical(treeWidget, 'Lỗi', 'Không thể xóa!')

def handleSearch(treeWidget, search_function, load_data_function, search_input, tab):
    keyword = search_input.text().strip()

    if keyword:
        search_results = search_function(keyword)
        treeWidget.clear()
        for row in search_results:
            item = QTreeWidgetItem()
            for i in range(len(row)):
                item.setText(i, str(row[i]))
            treeWidget.addTopLevelItem(item)
    else:
        QMessageBox.warning(tab, "Thông báo", "Vui lòng nhập từ khóa để tìm kiếm!")
        loadDataToTreeWidget(treeWidget, load_data_function)

def handleInputChanged(treeWidget, load_data_function, text):
    if not text:
        loadDataToTreeWidget(treeWidget, load_data_function)
