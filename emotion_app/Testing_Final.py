import time
import cv2
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
print(os.getcwd())


##################################################################################
# Preprocessing
#################################################################################
#%%
def getImagePath(image):
    TEST_IMAGES_DIR = os.path.dirname(__file__) + '/test_images/' + image
    print("test" + TEST_IMAGES_DIR)
    return main(TEST_IMAGES_DIR)


def main(image_path):

    sigLev = 3
    pd.options.display.precision = sigLev
    figWidth = figHeight = 9
    fullImageFilename = image_path
    # chosenImage = Image.open(fullImageFilename)
    #
    # idealWidth = 1050
    # idealHeight = 600
    # resizedChosenImage = chosenImage.resize((idealWidth,idealHeight),Image.NEAREST)
    # resizedChosenImage  =np.array(resizedChosenImage)
    # resizedChosenImage=cv2.imread(image_path)
    # greyChosenImage = cv2.cvtColor(resizedChosenImage, cv2.COLOR_BGR2GRAY)
    #
    #
    # cv2.imwrite(os.getcwd() + "../static/" + "resizedChosenImage.jpg",resizedChosenImage)
    # cv2.imwrite(os.getcwd() + "../static/" + "greyChosenImage.jpg",greyChosenImage)

    # #Thersolding of grey image
    #
    #
    # image = cv2.imread(fullImageFilename)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # # convert the image to grayscale
    # gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # _, binary = cv2.threshold(gray, 100, 150, cv2.THRESH_BINARY_INV)
    # # show the image
    # #plt.imshow(binary, cmap="gray")
    # plt.savefig( "thresholding.png")#os.getcwd() + "../static/" +
    #
    # import cv2
    # import numpy as np
    # from matplotlib import pyplot as plt

    # img = cv2.imread(fullImageFilename,0)
    #
    # # hist,bins = np.histogram(img.flatten(),256,[0,256])
    #
    # cdf = hist.cumsum()
    # cdf_normalized = cdf * hist.max()/ cdf.max()
    #
    # plt.plot(cdf_normalized, color = 'b')
    # plt.hist(img.flatten(),256,[0,256], color = 'r')
    # plt.xlim([0,256])
    # plt.legend(('cdf','histogram'), loc = 'upper left')
    # plt.savefig( "Normalization.png")#os.getcwd() + "/static/" +
    #
    # img = cv2.imread(fullImageFilename)
    # color = ('b','g','r')
    # for i,col in enumerate(color):
    #     histr = cv2.calcHist([img],[i],None,[256],[0,256])
    #     plt.plot(histr,color = col)
    #     plt.xlim([0,256])
    # plt.savefig("histogram.png")#os.getcwd() + "/static/" +




    ####################################################################################



    # Read the image_data
    image_data = tf.io.gfile.GFile(image_path, 'rb').read()
    # Loads label file, strips off carriage return
    letter = []
    s = []
    label_lines = [line.rstrip() for line
               in tf.io.gfile.GFile(os.path.dirname(__file__) +'/logs/trained_labels.txt')]
    # Unpersists graph from file
    with tf.io.gfile.GFile(os.path.dirname(__file__)+'/logs/trained_graph.pb', 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.compat.v1.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]


        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            letter.append(human_string)
            print(letter)
            s.append(score)
                #d = {label_lines[node_id]: predictions[0][node_id]}
                # print('%s (score = %.5f)' % (human_string, score))

            image = cv2.imread(image_path)
           # writeResultOnImage(image, letter[0].upper() + ", " + "{0:.2f}".format(s[0] * 100) + "% Confidence")
            scale_percent = 200

            # calculate the 50 percent of original dimensions
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)

            # dsize
            dsize = (width, height)

            # resize image
            image = cv2.resize(image, dsize)

            cv2.imwrite( "result.jpg", image)#os.getcwd() + "/static/" +
            print(letter[0], ':', s[0])

    return letter[0], s[0]




def writeResultOnImage(openCVImage, resultText):
    # ToDo: this function may take some further fine-tuning to show the text well given any possible image size

    imageHeight, imageWidth, sceneNumChannels = openCVImage.shape

    # choose a font
    fontFace = cv2.FONT_HERSHEY_TRIPLEX

    # chose the font size and thickness as a fraction of the image size
    fontScale = 0.1
    fontThickness = 0.5

    # make sure font thickness is an integer, if not, the OpenCV functions that use this may crash
    fontThickness = int(fontThickness)

    upperLeftTextOriginX = int(imageWidth * 0.005)
    upperLeftTextOriginY = int(imageHeight * 0.005)

    textSize, baseline = cv2.getTextSize(resultText, fontFace, fontScale, fontThickness)
    textSizeWidth, textSizeHeight = textSize

    # calculate the lower left origin of the text area based on the text area center, width, and height
    lowerLeftTextOriginX = upperLeftTextOriginX
    lowerLeftTextOriginY = upperLeftTextOriginY + textSizeHeight
    SCALAR_BLUE = (255.0, 255.0, 255.0)
    # write the text on the image
    cv2.putText(openCVImage, resultText, (lowerLeftTextOriginX, lowerLeftTextOriginY), fontFace, fontScale, SCALAR_BLUE,
                fontThickness)
