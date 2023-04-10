import imageio

images = []
img_dir = "/media/eslam/983CBB793CBB50CC/ImageCaption/anonymous_bench/images/"
#filenames = ['02105', '03369', '00413', '01537', '00495', '00587', '00682', '04015', '00379', '00175']
#filenames = ['03571', '00707', '00784', '00709', '00753', '03659', '00867', '03559', '00010', '00024']
#filenames = ['03930', '00370', '00027', '00032', '03815', '00708', '04012', '01094', '01034', '03335']
filenames = ['00365', '00450', '00453', '00374', '02781', '00738', '00839', '00953', '04475', '03002']

for filename in filenames:
    images.append(imageio.imread(img_dir + filename + ".png"))
imageio.mimsave('AnonymousBench4.gif', images, fps=2)