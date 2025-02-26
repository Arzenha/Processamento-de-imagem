import matplotlib.pyplot as plt

def plot_image(image):
    plt.figure(figsize=(12, 6))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12,6))
    names_lst = ['Image {}'.format(i) for i in range(1, number_images)]
    names_lst.append('Result')
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.axis('off')
        ax.imshow(image, cmap='gray')
    fig.tight_layout()
    plt.show()

def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12,6), sharex=True, sharey=True)
    color_lst = ['r', 'g', 'b']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('Histogram {}'.format(color.title()))
        ax.hist(image[:, :, index].ravel(), bins=256, range=(0, 256), color=color)
    fig.tight_layout()
    plt.show()