import json
import video
import image

class Json:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path ,'r') as myfile:
            data = myfile.read()

        json_obj = json.loads(data)
        print('file read')

        for i in json_obj:
            if i['type'] == 'image':
                self.download_url = i['download_url']
                print(self.download_url)
                self.duration = i['duration']
                obj_image = image.Image(self.download_url, self.duration)
                obj_image.show()
                print('image object created')
            elif i['type'] == 'video':
                print('video entered')
                self.download_url = i['download_url']
                print(self.download_url)
                self.duration = i['duration']
                print(self.duration)
                obj_video = video.Video(self.download_url, self.duration)
                obj_video.play()
                print('video object created')

if __name__ == '__main__':
    obj = Json('example_2.json')
    obj.read()