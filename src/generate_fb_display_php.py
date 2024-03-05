def generate_fb_display_php(directory_path):
    php_code = f'''<?php

include_once $_SERVER['DOCUMENT_ROOT']. '/modules/rs/requires/reader.php';

$fb_json_file = $_SERVER['DOCUMENT_ROOT']. '/modules/rs/facebook_posts.json';
$fb_test_data = file_get_contents($fb_json_file);
$fb_posts = read_json_file($fb_json_file);

?>

<section style="padding-top: 12px; padding-bottom: 12px; font-family: 'Advent Pro', sans-serif;">
    <div class="container">
        <div class="row">
            <?php foreach ($fb_posts as $fb_post): ?>
            <div class="col text-center"><iframe src="<?php echo $fb_post['url']; ?>" width="350" height="577" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe></div>
            <?php endforeach; ?>
        </div>
    </div>
</section>

'''

    with open(f"{directory_path}/rs/requires/fb_display.php", "w") as php_file:
        php_file.write(php_code)
        print("fb_display.php generated !")
