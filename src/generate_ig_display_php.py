def generate_ig_display_php(directory_path):
    php_code = f'''<?php

include_once $_SERVER['DOCUMENT_ROOT']. '/modules/rs/requires/reader.php';

$ig_json_file = $_SERVER['DOCUMENT_ROOT']. '/modules/rs/instagram_posts.json';
$ig_test_data = file_get_contents($ig_json_file);
$ig_posts = read_json_file($ig_json_file);

?>

<section style="padding-top: 12px; padding-bottom: 12px; font-family: 'Advent Pro', sans-serif;">
    <div class="container">
        <div class="row">
            <?php foreach ($ig_posts as $ig_post): ?>
            <div class="col text-center"><iframe src="<?php echo $ig_post['url']; ?>" allowtransparency="true" frameborder="0" scrolling="no" width="320" height="550"></iframe></div>
            <?php endforeach; ?>
        </div>
    </div>
</section>
'''

    with open(f"{directory_path}/rs/requires/ig_display.php", "w") as php_file:
        php_file.write(php_code)
        print("ig_display.php generated !")
