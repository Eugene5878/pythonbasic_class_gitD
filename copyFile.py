buffer_size = 1024

with open('WIN_20210614_16_57_33_Pro.mp4','rb')as source:
    with open('WIN_20210614_16_57_33_Pro2.mp4','wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)

print('Finish')
