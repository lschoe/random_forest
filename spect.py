import cProfile
import sys

from mpyc.runtime import mpc

from src.dataset import ObliviousDataset, Sample
from src.output import output
from src.secint import secint as s
from src.train import train


def sample(ins, out):
    return Sample([s(i) for i in ins], s(out))


spect_samples = ObliviousDataset.create(
    sample([1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0],0),
    sample([1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0],1),
    sample([1,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1],1),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0],0),
    sample([1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0],1),
    sample([1,1,0,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1],1),
    sample([1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],1),
    sample([1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1],1),
    sample([1,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],1),
    sample([1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0],0),
    sample([1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],1),
    sample([1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,1],1),
    sample([1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1],1),
    sample([1,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1],1),
    sample([1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,1],0),
    sample([1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([1,1,0,1,0,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0,1,1],0),
    sample([1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0],0),
    sample([1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1],1),
    sample([1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0],0),
    sample([1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,0,0],0),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0],0),
    sample([1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0],0),
    sample([1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1],1),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0],1),
    sample([1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1],1),
    sample([1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1],0),
    sample([1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0],1),
    sample([1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1],1),
    sample([1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],0),
    sample([1,1,0,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1],0),
    sample([0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0],0),
    sample([0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],0),
    sample([0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],1),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0],1),
    sample([0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],0),
    sample([0,1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0],0),
    sample([0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0],0),
    sample([0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],0),
    sample([0,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1],1),
    sample([0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,0],0),
    sample([1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0],1),
    sample([1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1],0),
    sample([1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0],1),
    sample([1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1],1),
    sample([1,1,0,0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0],1),
    sample([1,1,0,0,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0],0),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,1,0,1,0,0],0),
    sample([1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0],0),
    sample([1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0],0),
    sample([1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0],1),
    sample([1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0],0),
    sample([1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,1,1,0],0),
    sample([1,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1],0),
    sample([1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,1],1),
    sample([1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0],1),
    sample([1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],0),
    sample([1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1],0),
    sample([1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0],0),
    sample([1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1],1),
    sample([1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1],0),
    sample([1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0],0),
    sample([1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0],0),
    sample([1,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1],0),
    sample([1,1,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,0,0,1,1,0],0),
    sample([1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],0),
    sample([1,1,1,0,0,1,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0],0),
    sample([1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1],0),
    sample([1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1],1),
    sample([1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],1),
    sample([1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0],0),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],1),
    sample([1,0,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],0),
    sample([1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1],1),
    sample([1,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1],1),
    sample([1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1],1),
    sample([1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,0],0),
    sample([1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1],1),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],0),
    sample([1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],1),
    sample([1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],1),
    sample([1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,1],1),
    sample([1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,0,1,1,1,0,0,1,1,0,0,0,0,1,1,1,0,0,0,1,1],0),
    sample([1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],1),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],1),
    sample([1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1],1),
    sample([1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],1),
    sample([1,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0],1),
    sample([1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1],1),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],1),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0],0),
    sample([1,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0],1),
    sample([1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,0],1),
    sample([1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0],0),
    sample([1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1],1),
    sample([1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1],1),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],0),
    sample([1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1],0),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1],1),
    sample([1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0],0),
    sample([1,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,1,0],0),
    sample([1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1],1),
    sample([1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1],1),
    sample([1,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1],1),
    sample([1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1],1),
    sample([1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],1),
    sample([1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0],0),
    sample([1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1],1),
    sample([1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1],1),
    sample([1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1],0),
    sample([1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,1],1),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1],1),
    sample([1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1],1),
    sample([1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1],1),
    sample([1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],1),
    sample([1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1],1),
    sample([1,1,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0],0),
    sample([1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],1),
    sample([1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0],0),
    sample([1,0,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0],1),
    sample([1,1,0,1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1],1),
    sample([1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1],0),
    sample([1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0],0),
    sample([1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1],1),
    sample([1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([1,0,0,1,0,0,1,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0],0),
    sample([1,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0],1),
    sample([1,0,0,0,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,0],0),
    sample([1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],1),
    sample([1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1],1),
    sample([1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1],1),
    sample([1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1],1),
    sample([1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,0,0],0),
    sample([1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,1],1),
    sample([1,1,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1],0),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0],0),
    sample([1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],0),
    sample([1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0],1),
    sample([1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0],0),
    sample([1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],0),
    sample([1,1,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],0),
    sample([1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],1),
    sample([1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0],0),
    sample([1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],0),
    sample([1,1,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1],1),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0],0),
    sample([1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1],1),
    sample([1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],1),
    sample([1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1],0),
    sample([1,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0],0),
    sample([1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,0],0),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],0),
    sample([1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],1),
    sample([1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1],0),
    sample([1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],1),
    sample([1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0],0),
    sample([1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1],1),
    sample([1,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,1,1],0),
    sample([1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,0,0,1,1],0),
    sample([1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1],1),
    sample([1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1],0),
    sample([1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1],1),
    sample([1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0],1),
    sample([1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1],1),
    sample([1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0],1),
    sample([1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,0],1),
    sample([1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],1),
    sample([1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1],1),
    sample([1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1],1),
    sample([1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,1],1),
    sample([1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,1,0],0),
    sample([1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],1),
    sample([1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,1],0),
    sample([1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,0],0),
    sample([1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1],1),
    sample([1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1],1),
    sample([1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1],0),
    sample([1,1,1,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0],0),
    sample([1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],1),
    sample([1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1],1),
    sample([1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0],0),
    sample([1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1],1),
    sample([1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1],0),
    sample([1,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1],1),
    sample([1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0],0),
    sample([1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1],0),
    sample([1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,1,0,0,1],1),
    sample([1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],1),
    sample([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0],0),
    sample([1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,1,0],0),
    sample([1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],1),
    sample([0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],0),
    sample([0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0),
    sample([0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0],0),
    sample([0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0],0),
    sample([0,1,0,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0],0),
    sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0)
)

def main():
    tree = mpc.run(output(train(spect_samples, depth=3)))
    print(tree)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'profile':
        cProfile.run('main()')
    else:
        main()
