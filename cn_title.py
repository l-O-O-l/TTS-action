def write_voice_from_title():
    voice_id = ''
    try:
        with open('./__title__.txt', 'rt') as f:
            lines = f.readlines()
        title = lines[0]
        voice_end_char_position=title.find('$')
        if voice_end_char_position < 0:
            return default_val
        num = int(title[7:voice_end_char_position])
        voice_id = num if num > 0 and num <= 30 else default_val
    except Exception:
        pass
    with open('./__voice__.txt', 'wt') as f:
        f.write(str(voice_id))

write_voice_from_title()
