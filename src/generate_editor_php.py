def generate_editor_php(directory_path):
    php_code = f'''<?php
    $instagram_json_file = 'instagram_posts.json';
    $facebook_json_file = 'facebook_posts.json';

    include_once $_SERVER['DOCUMENT_ROOT']. '/modules/rs/requires/reader.php';

    function read_json_file($file) {{
        if (!file_exists($file)) {{
            return [];
        }}
        $json_data = file_get_contents($file);
        return json_decode($json_data, true);
    }}

    // Function to write to JSON file
    function write_json_file($file, $data) {{
        $json_data = json_encode($data, JSON_PRETTY_PRINT);
        file_put_contents($file, $json_data);
    }}

    // Read current posts
    $instagram_posts = read_json_file($instagram_json_file);
    $facebook_posts = read_json_file($facebook_json_file);

     // Handle POST request
     if ($_SERVER['REQUEST_METHOD'] == 'POST') {{
        //IG
        if (isset($_POST['ig_add']) && !empty($_POST['ig_new_url'])) {{
            // Add new post
            if (count($instagram_posts) < 3) {{
                $instagram_posts[] = ['url' => $_POST['ig_new_url']];
                write_json_file($instagram_json_file, $instagram_posts);
                echo '<script>window.location.href = "' . $_SERVER['PHP_SELF'] . '";</script>';
            }}
        }} elseif (isset($_POST['ig_delete'])) {{
            // Delete post
            $indexToDelete = intval($_POST['ig_delete'][0]);
            array_splice($instagram_posts, $indexToDelete, 1);
            write_json_file($instagram_json_file, $instagram_posts);
            echo '<script>window.location.href = "' . $_SERVER['PHP_SELF'] . '";</script>';
        }} elseif (isset($_POST['ig_update'])) {{
            // Edit post
            foreach ($_POST['ig_edit_url'] as $ig_index => $url) {{
                $instagram_posts[$ig_index]['url'] = $url;
            }}
            write_json_file($instagram_json_file, $instagram_posts);
            echo '<script>window.location.href = "' . $_SERVER['PHP_SELF'] . '";</script>';
        //FB
        }} elseif (isset($_POST['fb_add']) && !empty($_POST['fb_new_url'])) {{
            // Add new post
            if (count($facebook_posts) < 3) {{
                $facebook_posts[] = ['url' => $_POST['fb_new_url']];
                write_json_file($facebook_json_file, $facebook_posts);
                echo '<script>window.location.href = "' . $_SERVER['PHP_SELF'] . '";</script>';
            }}
        }} elseif (isset($_POST['fb_delete'])) {{
            // Delete post
            $indexToDelete = intval($_POST['fb_delete'][0]);
            array_splice($facebook_posts, $indexToDelete, 1);
            write_json_file($facebook_json_file, $facebook_posts);
            echo '<script>window.location.href = "' . $_SERVER['PHP_SELF'] . '";</script>';
        }} elseif (isset($_POST['fb_update'])) {{
            // Edit post
            foreach ($_POST['fb_edit_url'] as $fb_index => $url) {{
                $facebook_posts[$fb_index]['url'] = $url;
            }}
            write_json_file($facebook_json_file, $facebook_posts);
            echo '<script>window.location.href = "' . $_SERVER['PHP_SELF'] . '";</script>';
        }}
        exit;
    }}
?>
'''

    with open(f"{directory_path}/rs/requires/editor.php", "w") as php_file:
        php_file.write(php_code)
        print("editor.php generated !")
