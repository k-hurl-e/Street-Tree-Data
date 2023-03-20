import matplotlib.pyplot as plt
from PIL import Image
from treedata import nta_pie_data

colors_custom = ['#4e4376', '#E09D00', '#50A7C2', '#A1BE37', '#8F4311', "grey"]

def makecroppedpie(file_name, labels_lst, values_lst, colors_lst):
        plt.rcParams['font.family'] = 'monospace'
        plt.rcParams['text.color'] = 'black'
        labels = labels_lst
        sizes = values_lst
        explode = (0, 0, 0, 0, 0, 0)  # tells which slice to "explode"
        colors_list = colors_lst
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90, colors= colors_list)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        # plt.title(title, color = 'white', fontweight = 'bold', fontsize = '20')
        plt.savefig('static/' + file_name + '.png', transparent=True, dpi=300)
        # imgPath = 'static/' + file_name + '.png'
        # img = Image.open(imgPath)
        # width, height = img.size
        # box = ((width / 8 - width / 32), (height / 8), (width - width / 8 + width / 32), (height - height / 8))
        # croppedImage = img.crop(box)
        # croppedImage.save('static/' + file_name + '_cropped.png')

check = nta_pie_data('Bedford')
makecroppedpie('test6', check[0], check[1], colors_custom)