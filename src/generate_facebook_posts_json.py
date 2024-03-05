def generate_facebook_posts_json(directory_path):
    json_code = f'''{[]}'''

    with open(f"{directory_path}/rs/facebook_posts.json", "w") as json_file:
        json_file.write(json_code)
        print("facebook_posts.json generated !")
