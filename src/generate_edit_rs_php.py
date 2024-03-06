def generate_edit_rs_php(directory_path, main_domain, full_body_tag):
    php_code = f'''<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';
?>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/head.php'
?>

    <title>Votre gestonnaire de réseaux sociaux</title>
    <link rel="stylesheet" type="text/css" href="https://{main_domain}/modules/rs/css/style.css">
</head>

<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/rs/requires/editor.php';
?>

{full_body_tag}
<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/navbar.php'
?>

    <section style="margin-top: 24px;margin-bottom: 24px;">
        <div class="container">
            <div class="row">
                <div class="col-md-12" style="text-align: center;">
                    <h1 style="font-family: 'Advent Pro', sans-serif;font-weight: bold;font-size: 48px;">Gérez l'affichage des publications de vos réseaux sociaux</h1>
                </div>
            </div>
        </div>
        <hr>
    </section>
    
    <section style="padding-top: 12px; padding-bottom: 12px; font-family: 'Advent Pro', sans-serif;">
        <div class="container">
            <div class="row">
                <div class="col-md-12" style="text-align: center;">
                    <h2 style="font-family: 'Advent Pro', sans-serif;font-weight: bold;font-size: 32px; margin-bottom: 24px;">Publications Instagram</h2>
                </div>
            </div>
            <form action="" method="post" style="margin-bottom: 32px">
                <div class="row">
                    <?php foreach ($instagram_posts as $ig_index => $ig_post): ?>
                    <div class="col text-center post-container">
                        <iframe src="<?php echo $ig_post['url']; ?>" allowtransparency="true" frameborder="0" scrolling="no" width="320" height="550"></iframe>
                            <div>
                                <button type="submit" name="ig_delete[]" value="<?php echo $ig_index; ?>" class="rs-button" onclick="return confirm('Voulez-vous vraiment supprimer ce post ?');">Supprimer</button>
                            </div>
                            <div>
                                <input type="text" name="edit_url[<?php echo $ig_index; ?>]" value="<?php echo $ig_post['url']; ?>">
                                <button type="submit" class="rs-button" name="ig_update">Mettre à jour</button>
                            </div>
                    </div>
                    <?php endforeach; ?>
                    <?php if (count($instagram_posts) < 3): ?>
                        <h3 style="font-weight: bold; margin-top: 24px">Ajouter un nouveau post Instagram</h3>
                        <div>
                            <p style="margin-bottom: 4px">Format de l'url : "https://www.instagram.com/p/Clf6bluM4yp/embed" (rajouter le "/embed" si il n'est pas présent). Plus d'informations <a href="https://www.facebook.com/help/instagram/620154495870484#">ici</a></p>
                        </div>
                        <div>
                            <input type="text" name="ig_new_url" placeholder="Saisir l'url">
                            <button type="submit" class="rs-button" name="ig_add">Ajouter un nouveau post</button>
                            <label>(3 posts maximum)</label>
                        </div>
                    <?php endif; ?>
                </form>
            </div>
        </div>
        <hr>
    </section>

    <section style="padding-top: 12px; padding-bottom: 12px; font-family: 'Advent Pro', sans-serif;">
        <div class="container">
            <div class="row">
                <div class="col-md-12" style="text-align: center;">
                    <h2 style="font-family: 'Advent Pro', sans-serif;font-weight: bold;font-size: 32px; margin-bottom: 24px;">Publications Facebook</h2>
                </div>
            </div>
            <form action="" method="post" style="margin-bottom: 32px">
                <div class="row">
                    <?php foreach ($facebook_posts as $fb_index => $fb_post): ?>
                    <div class="col text-center post-container">
                        <iframe src="<?php echo $fb_post['url']; ?>" width="350" height="577" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>
                            <div>
                                <button type="submit" name="fb_delete[]" value="<?php echo $fb_index; ?>" class="rs-button" onclick="return confirm('Voulez-vous vraiment supprimer ce post ?');">Supprimer</button>
                            </div>
                            <div>
                                <input type="text" name="edit_url[<?php echo $fb_index; ?>]" value="<?php echo $fb_post['url']; ?>">
                                <button type="submit" class="rs-button" name="fb_update">Mettre à jour</button>
                            </div>
                    </div>
                    <?php endforeach; ?>
                    <?php if (count($facebook_posts) < 3): ?>
                        <h3 style="font-weight: bold; margin-top: 24px">Ajouter un nouveau post Facebook</h3>
                        <div>
                            <p style="margin-bottom: 4px">Format de l'url : "https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fledarius.pizzas%2Fposts%2F846898600135380&width=350&show_text=true&height=577&appId" <br>(rajouter le "/embed" si il n'est pas présent). Plus d'informations <a href="hhttps://www.facebook.com/help/www/215768235242256">ici</a></p>
                        </div>
                        <div>
                            <input type="text" name="fb_new_url" placeholder="Saisir l'url">
                            <button type="submit" class="rs-button" name="fb_add">Ajouter un nouveau post</button>
                            <label>(3 posts maximum)</label>
                        </div>
                    <?php endif; ?>
                </form>
            </div>
        </div>
        <hr>
    </section>

    <section>
        </div>
            <p style="text-align: center; font-size: 24px"><a href="https://{main_domain}/">Revenir à l'accueil</a></p>
        </div>
    </section>

</body>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/footer.php'
?>

</html>
'''

    with open(f"{directory_path}/rs/edit-rs.php", "w") as php_file:
        php_file.write(php_code)
        print("edit-rs.php generated !")
