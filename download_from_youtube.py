import pafy


print("Хотите скачать видео или аудио с YouTube? Просто введите URL ниже.")
url = input("Введите URL: ")


def download(url):
    try:
        v = pafy.new(url)
        streams = v.streams

        available_streams = {}
        count = 1

        for stream in streams:
            available_streams[count] = stream
            print(f"{count}: {stream}")
            count += 1

        stream_count = int(input("Введите номер: "))
        d = streams[stream_count -1].download()

        print("Скачивание успешно завершено!")

    except:
        print("Упс... Пожалуйста, проверьте данные")

download(url)