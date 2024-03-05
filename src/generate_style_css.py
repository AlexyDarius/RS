def generate_style_css(directory_path, bg_color, color):
    css_code = f'''.rs-button {{
    color: red;
    background-color: {bg_color};
    color: {color};
    padding: 10px 20px;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    margin-bottom: 12px;
}}
'''

    with open(f"{directory_path}/rs/css/style.css", "w") as js_file:
        js_file.write(css_code)
        print("style.css generated !")
