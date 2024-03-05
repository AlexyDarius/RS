def generate_reader_php(directory_path):
    php_code = f'''<?php
function read_json_file($file) {{
    if (!file_exists($file)) {{
        return [];
    }}
    $json_data = file_get_contents($file);
    return json_decode($json_data, true);
}}
?>
'''

    with open(f"{directory_path}/rs/requires/reader.php", "w") as php_file:
        php_file.write(php_code)
        print("reader.php generated !")
