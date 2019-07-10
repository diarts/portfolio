def add_button_child(child_list):
    buttons_list = []
    for child in child_list:
        if child.child_buttons:
            child_list = [child, ]
            child_list.append(add_button_child(child.child_buttons))
            buttons_list.append(child_list)
        else:
            buttons_list.append(child)

    return buttons_list
