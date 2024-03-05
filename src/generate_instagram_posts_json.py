def generate_instagram_posts_json(directory_path):
    json_code = f'''{[]}'''

    with open(f"{directory_path}/rs/instagram_posts.json", "w") as json_file:
        json_file.write(json_code)
        print("instagram_posts.json generated !")
