import os
from glob import glob
import pandas as pd


def make_dataset_folder(folder):
    """
    Create Filename list for images in the provided path

    input: path to directory with *only* images files
    returns: items list with None filled for mask path
    """
    filename_train = "drive360challenge_train.csv"
    filename_valid = "drive360challenge_validation.csv"

    df = pd.read_csv(os.path.join(folder, filename_train), usecols=['cameraFront'])
    l = df.size
    li = []
    for i in range(int(l/20)):
        li = li + list(range(i*20, i*20 + 4))

    df = df.iloc[li]
    df = df.reset_index(drop=True)

    # df = df.iloc[::10]
    # df = df.reset_index(drop=True)

    df['cameraFront'] = folder + '/' + df['cameraFront']
    df['mask'] = ''
    
    items = list(df.to_records(index=False))

    # items = [y for x in os.walk(folder) for y in glob(os.path.join(x[0], '*.jpg'))]

    # items = os.listdir(folder)
    # items = [(os.path.join(folder, f), '') for f in items]
    # items = sorted(items)

    print(f'Found {len(items)} folder imgs')

    """
    orig_len = len(items)
    rem = orig_len % 8
    if rem != 0:
        items = items[:-rem]

    msg = 'Found {} folder imgs but altered to {} to be modulo-8'
    msg = msg.format(orig_len, len(items))
    print(msg)
    """

    return items
