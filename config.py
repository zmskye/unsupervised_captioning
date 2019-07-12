import os

from absl import flags

flags.DEFINE_integer('vocab_size', 18669, 'vocab size')

flags.DEFINE_integer('start_id', 0, 'SOS')

flags.DEFINE_integer('end_id', 1, 'EOS')

# HOME = os.getenv('HOME')
HOME = '/DATA/dist1/zhangming6/projects/'
TF_MODELS_PATH = HOME + '/unsupervised_caption/tf_models'
COCO_PATH = HOME + '/unsupervised_caption/coco-caption'

NUM_DESCRIPTIONS = 2282457
