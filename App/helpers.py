username_text = """
MDTextField:
    hint_text: "Enter Username"
    pos_hint:{"center_x": 0.5, "center_y" : 0.6}
    size_hint_x:(0.7)
    width:500
    required: True
"""
pass_text = """
MDTextField:
    hint_text: "Enter Password"
    helper_text: "if you forgot your password contact your bank"
    helper_text_mode:"on_focus"
    pos_hint:{"center_x": 0.5, "center_y" : 0.5}
    size_hint_x:(0.7)
    width:500
    required:True
"""
amount = """
MDTextField:
    hint_text: "Enter amount"
    pos_hint:{"center_x": 0.5, "center_y" : 0.7}
    helper_text: "Enter amount to be paid"
    helper_text_mode:"persistent"
    size_hint_x:(0.7)
    size_hint_y:(0.08)
    input_filter: 'float'
    width:500
    required: True
"""
bottom_toolbar = '''
MDBoxLayout:
    MDBottomAppBar:
        MDToolbar:
            icon: "git"
            type: "bottom"
'''
