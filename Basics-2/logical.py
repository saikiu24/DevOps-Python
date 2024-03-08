is_magician = False
is_expert = True

# Check if magician AND expert: "you are a master magician"
if is_expert and is_magician:
    print(f'you are a master magician')

# check if magician but not expert:
elif is_magician and not is_expert:
    print(f'At least you\'re getting there')

# if you're not a magician: "You need magic powers"
elif not is_magician:
    print(f'you\'re not a magician')
